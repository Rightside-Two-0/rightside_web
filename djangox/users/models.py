from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    address = models.CharField(max_length=60, default='')
    city = models.CharField(max_length=30, default='')
    state = models.CharField(max_length=30, default='')
    zipcode = models.CharField(max_length=20, default='')

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
