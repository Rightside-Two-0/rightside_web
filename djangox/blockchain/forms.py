from django import forms

class TransactionForm(forms.Form):
    date = forms.DateTimeField()
    from_account = forms.CharField(max_length=30)
    to_account = forms.CharField(max_length=30)
    amount = forms.FloatField()
    notes = forms.CharField(max_length=255)

class Input_GoalForm(forms.Form):
    goal = forms.FloatField()
