import string

from django.core.exceptions import ValidationError


def validate_no_null_chars(value):
    value = value.strip()
    raw = value.strip(string.punctuation)
    if not raw or len(raw) < 2:
        raise ValidationError("Invalid input provided")
