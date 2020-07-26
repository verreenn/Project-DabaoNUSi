from django.contrib.auth import get_user_model,authenticate
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError, ModelForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(LoginForm, self).clean(*args, **kwargs)
    


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email Address')
    phone = forms.CharField(label='Contact Number')
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Password Confirmation')

    #if username and email and phone and password1 and password2:
    #    email2 = self.cleaned_data['email']
    #    if not email2.endswith('@u.nus.edu'):
    #        raise forms.ValidationError('Only NUSNET email addresses allowed')
        

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "phone"]

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@u.nus.edu'):
            raise forms.ValidationError("Only NUSNET email addresses allowed")
        elif User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists")
        return email