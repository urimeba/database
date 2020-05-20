from django import forms

class formLogin(forms.Form):
    username = forms.CharField(max_length=6, label='Expediente', required=True,  widget=forms.NumberInput(attrs={}))
    password = forms.CharField(max_length=20, label='Contraseña', required=True, widget=forms.PasswordInput(attrs={}))

    def clean(self):
        cleaned_data = super(formLogin, self).clean()
        expediente = cleaned_data.get('expediente')
        password = cleaned_data.get('password')
        if not expediente and not password:
            raise forms.ValidationError('Los campos no pueden estar vacios')
        return cleaned_data