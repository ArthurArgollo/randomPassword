import secrets
import string

letras = string.ascii_letters
digitos = string.digits
caracteres_especiais = string.punctuation
alfabeto = letras + digitos + caracteres_especiais

pwd_length = 12
pwd = ''
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alfabeto))

print(pwd)

while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alfabeto))
    if (any(char in caracteres_especiais for char in pwd) and
        sum(char in digitos for char in pwd)>=2):
            break
print(pwd)