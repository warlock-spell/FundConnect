from django.db import models
from member.models import Member
from django.core.validators import RegexValidator


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
        ('INTEREST', 'Interest'),
        ('ADJUSTMENT', 'Adjustment'),
        ('CHEQUE', 'Cheque'),
        ('SERVICE_FEE', 'Service Fee'),
        ('OTHER', 'Other'),
    ]

    date = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    fund_type = models.CharField(max_length=20, choices=FUND_TYPES)
    refund_on_exit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deposits_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    cashbook = models.ForeignKey(Cashbook, on_delete=models.CASCADE, related_name='entries')

    def __str__(self):
        return f"{self.date}-{self.month}-{self.year}: {self.fund_type}, {self.member.id} {self.member.name}"

    def save(self, *args, **kwargs):
        # Automatically determine the cashbook based on the financial year
        months_of_prev_financial_year = ['01', '02', '03']
        if self.month in months_of_prev_financial_year:
            financial_year = f"{int(str(self.year)[:4]) - 1}-{str(self.year)[2:]}"
        else:
            financial_year = f"{str(self.year)[:4]}-{int(str(self.year)[2:]) + 1}"

        cashbook, created = Cashbook.objects.get_or_create(
            financial_year=financial_year,
            member=self.member
        )
        self.cashbook = cashbook
        super().save(*args, **kwargs)
