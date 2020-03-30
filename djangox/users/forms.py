#  ___ __ ._`.*.'_._ ____ רףאל
#  . +  * .\   o.* `.`. +.  א .
# *  .ת' '  \^/|  `. * .  * `
#           \V/ . +
#  יהוה     /_\  .`.
# ======== _/W\_ =אדני:By: Two.0:.*
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')
