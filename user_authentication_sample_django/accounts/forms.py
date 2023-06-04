from django import forms
from django.contrib.auth.models import User

class emailregistration(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter you email'}))
    password = forms.PasswordInput()
    print("ff",email)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email adress already exists")
        else:
            return email
