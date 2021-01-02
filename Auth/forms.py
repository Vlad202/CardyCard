from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="Логин", max_length=100)
    password = forms.CharField(label="Пароль", max_length=64)

class UserSignUpForm(forms.Form):
    username = forms.CharField(label="Логин", max_length=100)
    email = forms.CharField(label="Почта", max_length=100)
    password1 = forms.CharField(label="Пароль", max_length=64)
    password2 = forms.CharField(label="Пароль", max_length=64)