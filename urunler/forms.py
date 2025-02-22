from django import forms
from .models import Mesaj

class MesajForm(forms.ModelForm):
    class Meta:
        model = Mesaj
        fields = ['ad', 'email', 'telefon', 'mesaj']  # Telefon alanı eklendi