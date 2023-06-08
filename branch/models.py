from django.db import models


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    manager = models.CharField(max_length=100, blank=True)
