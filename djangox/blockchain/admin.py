from django.contrib import admin

# Register your models here.
from .models import StepImage
from .models import Transaction

admin.site.register(Transaction)
admin.site.register(StepImage)
