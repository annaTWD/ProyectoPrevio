from email_validator import validate_email, EmailNotValidError

def clean_email_text(text):
    """
    Limpia el texto de un correo electrónico eliminando espacios y caracteres especiales no deseados.
    """
    return text.strip()

def validate_email_address(email):
    """
    Valida la dirección de correo electrónico.
    """
    try:
        v = validate_email(email) 
        return v["email"]
    except EmailNotValidError as e:
        return str(e)
