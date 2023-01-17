# necessary imports
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation


def pasFacil():
    """Crea un pass de 6 digitos numericos"""

    pwd_length = 6
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(digits))

    return pwd

def pasMedio():
    """Crea un pass de 8 digitos numeros/letras"""
    pwd_length = 8
    pwd = ''

    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(letters + digits))

    return pwd

def pasDificil():
    """Crea un pass de 12 digitos numeros/letras/caracteres"""

    pwd_length = 12
    pwd = ''

    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(letters + digits + special_chars))

    return pwd


print (pasFacil())
print (pasMedio())
print (pasDificil())