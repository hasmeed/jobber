from django.core.exceptions import ValidationError

USERNAME_NOT_USER = ['Admin', 'Fuck', 'Sex', 'Porn']


def username_validate(value):
    username = value
    if username.capitalize() in USERNAME_NOT_USER:
        raise ValidationError(
            "Sorry we do not allow the word {} in our system".format(username.upper()))


# def accountType_validator()
