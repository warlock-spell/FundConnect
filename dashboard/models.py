from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Controller(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    refund_on_exit = models.DecimalField(max_digits=10, decimal_places=2)
    dividend_interest = models.DecimalField(max_digits=10, decimal_places=2,
                                            validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    pay_off_period_of_dividend = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])
    loan_interest = models.DecimalField(max_digits=10, decimal_places=2,
                                        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    loan_interest_period = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])
    service_fee_interest = models.DecimalField(max_digits=10, decimal_places=2,
                                               validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    service_fee_period = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])

    def __str__(self):
        return self.name
