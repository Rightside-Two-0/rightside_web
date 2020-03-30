from django.db import models

# Create your models here.
class Statement(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    income = models.CharField(max_length=25)
    expenses = models.CharField(max_length=25)
    assets = models.CharField(max_length=25)
    liabilities = models.CharField(max_length=25)
    passive = models.CharField(max_length=25)
    cashflow = models.CharField(max_length=25)
