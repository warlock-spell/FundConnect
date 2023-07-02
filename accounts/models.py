from django.db import models
from member.models import Member
from django.core.validators import RegexValidator
from dashboard.models import Controller
from .calculations import helper_functions


class Cashbook(models.Model):
    financial_year_validator = RegexValidator(
        regex=r'^\d{4}-\d{2}$',
        message="Financial year must be in the format 'YYYY-YY'"
    )

    financial_year = models.CharField(
        max_length=7,
        validators=[financial_year_validator]
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='cashbooks')

    def __str__(self):
        return f"{self.financial_year} - {self.member.id} {self.member.name}"


class CashBookEntry(models.Model):
    FUND_TYPES = [
        ('OPENING BALANCE', 'Opening_Balance'),
        ('CLOSING BALANCE', 'Closing_Balance'),
        ('INTEREST', 'Interest'),
        ('DIVIDEND', 'Dividend'),
        ('SALARY', 'Salary'),
        ('DEPOSIT', 'Deposit'),
        ('ADJUSTMENT', 'Adjustment'),
        ('CHEQUE', 'Cheque'),
        ('SERVICE_FEE', 'Service Fee'),
        ('OTHER', 'Other'),
        ('LOAN', 'Loan'),
        ('SHARES', 'Shares'),
    ]

    date = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    fund_type = models.CharField(max_length=20, choices=FUND_TYPES)
    refund_on_exit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deposits_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shares_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    cashbook = models.ForeignKey(Cashbook, on_delete=models.CASCADE, related_name='entries')
    remittance_posted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date}-{self.month}-{self.year}: {self.fund_type}, {self.member.id} {self.member.name}"

    def save(self, *args, **kwargs):
        # Automatically determine the cashbook based on the financial year
        financial_year = helper_functions.get_financial_year(self.month, self.year)

        cashbook, created = Cashbook.objects.get_or_create(
            financial_year=financial_year,
            member=self.member
        )

        if self.fund_type not in ['OPENING BALANCE', 'CLOSING BALANCE', 'LOAN', 'SHARES']:
            self.member.refund_on_exit += self.refund_on_exit_amount
            self.member.deposits += self.deposits_amount
            self.member.loan += self.loan_amount
            self.member.share_holding += self.shares_amount
            self.member.save()

        self.cashbook = cashbook
        super().save(*args, **kwargs)


class Loan(models.Model):
    date = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    ask_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    allotted_loan_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    allotted_to_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='loans')
    number_of_installments = models.IntegerField(default=120)
