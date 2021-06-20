from django import forms
from django.core.validators import MinLengthValidator, EmailValidator

from todo_project.form_workshop.vaidators import validate_name, validate_age, validate_password, validate_bot_catcher


class WorkshopForm(forms.Form):
    name = forms.CharField(
        validators=[
            MinLengthValidator(6),
            validate_name,
        ])
    age = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[
            validate_age,
        ])
    email = forms.EmailField(
        widget=forms.EmailInput,
        validators=[
            EmailValidator(),
        ])
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            MinLengthValidator(8),
            validate_password,
        ])
    text = forms.CharField(widget=forms.Textarea)

    bot_catcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[
            validate_bot_catcher,
        ])
