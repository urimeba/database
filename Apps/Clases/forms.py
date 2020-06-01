from django import forms

class formLogin(forms.Form):
    username = forms.CharField(
        max_length=6, 
        label='Expediente', 
        required=True,  
        widget=forms.TextInput(attrs={})
        )
    password = forms.CharField(
        max_length=20, 
        label='Contraseña', 
        required=True, 
        widget=forms.PasswordInput(attrs={})
        )