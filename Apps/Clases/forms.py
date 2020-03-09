from django import forms

class Login(forms.Form):
    expediente = forms.CharField(label='Expediente', max_length=6, required=True, widget=forms.NumberInput(attrs={'id':'inputLogin'}))
    password = forms.CharField(label='Contraseña', max_length=20, required=True, widget=forms.PasswordInput(attrs={'id':'inputLogin'}))

    def clean(self):
        cleaned_data = super(Login, self).clean()
        expediente = cleaned_data.get('expediente')
        password = cleaned_data.get('password')
        if not expediente and not password:
            raise forms.ValidationError('Los campos no pueden estar vacios')