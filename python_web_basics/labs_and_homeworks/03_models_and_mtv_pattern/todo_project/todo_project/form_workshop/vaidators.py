from django.core.exceptions import ValidationError


def validate_name(name):
    if not name[0].isupper():
        raise ValidationError("The name must start with an uppercase letter.")


def validate_age(age):
    if age < 0:
        raise ValidationError("The age cannot be less than zero.")


def validate_password(password):
    if any(el for el in password if not el.isalnum()):
        raise ValidationError("Enter a valid password.")


def validate_bot_catcher(value):
    if value:
        raise ValidationError("This form was created by a bot")
