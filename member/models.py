from django.db import models
from branch.models import Branch


# Create your models here.
class Member(models.Model):
    id = models.IntegerField(primary_key=True)  # Membership number
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='members')
    position = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    wish_to_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    refund_on_exit = models.DecimalField(max_digits=10, decimal_places=2)
    deposits = models.DecimalField(max_digits=10, decimal_places=2)
    loan = models.DecimalField(max_digits=10, decimal_places=2)
    share_holding = models.DecimalField(max_digits=10, decimal_places=2)
    active_user = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.name}"
