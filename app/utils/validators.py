import re
from email_validator import validate_email, EmailNotValidError

def validate_email_format(email):
    try:
        validate_email(email)
        return True, None
    except EmailNotValidError as e:
        return False, str(e)

def validate_password(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters long"
    return True, None

def validate_item(name, description):
    if not name or len(name.strip()) == 0:
        return False, "Name is required"
    if len(name) > 100:
        return False, "Name must be less than 100 characters"
    if description and len(description) > 500:
        return False, "Description must be less than 500 characters"
    return True, None