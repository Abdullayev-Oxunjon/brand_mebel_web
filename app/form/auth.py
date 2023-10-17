from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.db.transaction import atomic

from app.models import User


class RegisterModelForm(forms.Form):
    username = forms.CharField(max_length=155)
    phone_number = forms.CharField(max_length=25)
    password = forms.CharField(max_length=128)
    confirm_password = forms.CharField(max_length=128)

    def clean_phone_number(self):
        phone_number = self.data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('This phone_number already exists')
        return phone_number

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Confirm password is wrong")
        return password

    @atomic
    def save(self):
        user = User.objects.create_user(
            phone_number=self.cleaned_data.get('phone_number'),
        )
        user.set_password(self.cleaned_data.get('password'))
        user.save()


class LoginModelForm(AuthenticationForm):
    username = forms.CharField(required=False)
    phone_number = forms.CharField()
    password = forms.CharField(max_length=128)

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        if phone_number and password:
            self.user_cache = authenticate(self.request,
                                           phone_number=phone_number,
                                           password=password)
            if self.user_cache:
                self.confirm_login_allowed(self.user_cache)
            else:
                raise self.get_invalid_login_error()

        return self.cleaned_data
