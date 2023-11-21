import string
import secrets
import os

os.system("cls")

def contiene_mayusculas(password)->bool:
    for letra in password:
        if letra.isupper():
            return True
        return False
    
def contiene_simbolos(password)->bool:
    for letra in password:
        if letra in string.punctuation:
            return True
        return False
    
def generar_password(longitud, tiene_simbolos, tiene_mayusculas)->str:
    combinacion=string.ascii_lowercase + string.digits

    if tiene_simbolos:
        combinacion += string.punctuation

    if tiene_mayusculas:
        combinacion += string.ascii_uppercase

    longitud_combinacion=len(combinacion)

    nuevo_password = ""

    for _ in range(longitud):
        nuevo_password += combinacion[secrets.randbelow(longitud_combinacion)]

    return nuevo_password

if __name__ == "__main__":
    nueva=generar_password(longitud=12, tiene_simbolos=False,  tiene_mayusculas=False)
    
    print(f"Tiene mayúsculas:{contiene_mayusculas(nueva)}")
    print(f"Tiene símbolos:{contiene_simbolos(nueva)}")
    print(nueva)

    