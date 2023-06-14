from django.db import models


# Create your models here.
class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    manager = models.CharField(max_length=100, blank=True)
