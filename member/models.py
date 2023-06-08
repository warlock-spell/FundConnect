from django.db import models
from branch.models import Branch

# Create your models here.
class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    refund_on_exit = models.DecimalField(max_digits=10, decimal_places=2)
    deposits = models.DecimalField(max_digits=10, decimal_places=2)
    loan = models.DecimalField(max_digits=10, decimal_places=2)
    share_holding = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.BooleanField(default=True)