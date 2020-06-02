from django import forms

class formLogin(forms.Form):
    username = forms.CharField(
        label='Expediente', 
        required=True,  
        widget=forms.TextInput(attrs={}),
        )
    password = forms.CharField(
        label='Contraseña', 
        required=True, 
        widget=forms.PasswordInput(attrs={})
        )