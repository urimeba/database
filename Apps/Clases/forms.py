from django import forms
from Apps.Clases import models as models_clases

class formLogin(forms.Form):
    expediente = forms.CharField(label='Expediente', required=True, max_length=6, widget=forms.NumberInput(attrs={'id':'inputLogin'}))
    password = forms.CharField(label='Contraseña', required=True, max_length=20, widget=forms.PasswordInput(attrs={'id':'inputLogin'}))

    def clean(self):
        cleaned_data = super(formLogin, self).clean()
        expediente = cleaned_data.get('expediente')
        password = cleaned_data.get('password')
        if not expediente and not password:
            raise forms.ValidationError('Los campos no pueden estar vacios')