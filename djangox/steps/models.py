from django.db import models

# Create your models here.
class Step(models.Model):
    step_number = models.CharField(max_length=15, unique=True)
    pass

    def __str__(self):
        return self.step_number
