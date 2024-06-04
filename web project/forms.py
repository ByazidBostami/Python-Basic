# forms.py

from django import forms
from .models import SecretMessage

class SecretMessageForm(forms.ModelForm):
    """
    A form for creating new secret messages.
    """
    class Meta:
        model = SecretMessage
        fields = ['message']
