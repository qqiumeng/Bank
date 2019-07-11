from django import forms
from first.models import *



class Logins(forms.ModelForm):

    class Meta:
        model=UserInfo
        fields = ['username', 'password']





