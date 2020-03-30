from django.db import models
import binascii

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

# Create your models here.
class Transaction(models.Model):
    date = models.DateTimeField()
    from_account = models.CharField(max_length=20)
    to_account = models.CharField(max_length=20)
    amount = models.FloatField()
    notes = models.CharField(max_length=255)

    def __str__(self):
        return self.notes

class StepImage(models.Model):
    step_image = models.ImageField(upload_to='images/')

class Input_Goal(models.Model):
    goal = models.FloatField()
