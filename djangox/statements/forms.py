from django.forms import ModelForm
from .models import Statement

class StatementForm(ModelForm):
    class Meta:
        model = Statement
        field = ['income', 'expenses', 'assets', 'liabilities', 'passive', 'cashflow']
