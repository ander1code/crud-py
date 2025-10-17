import re
from datetime import datetime, date
from services.crud import Crud

def validate_name(name):
    if not name:
        return "Name is empty."
    if len(name) >= 1 and len(name) < 4:
        return "Invalid name."
    return None

def validate_email(email):
    if not email:
        return "E-mail is empty."
    email = email.strip().lower()
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not re.match(email_regex, email):
        return "Invalid e-mail format."
    if not Crud().is_email_not_registered(email):
        return "E-mail is already registered."
    return None

def validate_salary(salary):
    if salary is None or salary == "":
        return "Salary is empty."
    try:
        salary = float(salary)
    except ValueError:
        return "Salary must be a number."
    if salary < 0:
        return "Salary cannot be negative."
    return None 

def validate_birthday(birthday):
    if not birthday:
        return "Birthday is empty."
    try:
        birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
    except ValueError:
        return "Birthday format is invalid. Use YYYY-MM-DD."
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    if age < 18:
        return "Must be at least 18 years old."
    return None 

def validate_gender(gender):
    if not gender:
        return "Birthday is empty."
    if not gender in ['M','F','O']:
        return "Invalid gender."
    return None 
