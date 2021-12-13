import re


def bienvenida_programa():
    print('Bienvenida, este programa simula el proceso de Login usando Phyton')
    print('Bienvenida, Señorita Monica')


def validar_correo(user, validacion, usuario):
    if len(user) == 0:
        print('El usuario está vacío. Usuario No Valido')
    elif validacion != -1:
        print('Email encontrado')
        if user == usuario:
            print('Usuario Correcto')
        else:
            print('Usuario Incorrecto')
    else:
        print('Email no encontrado. Usuario No Valido')


def validar_contrasena(password, contrasena):
    if len(password) == 0:
        print('La contraseña está vacía. Contraseña no valida')
    elif 8 <= len(password) <= 20:
        if re.search('[a-z]', contrasena) and re.search('[0-9]', contrasena):
            if contrasena == password:
                print('Contraseña Correcta')
            else:
                print('Contrasena Incorrecta')
    elif len(password) < 8:
        print('Contraseña Incorrecta. Tú contraseña no cuenta con el mínimo de 8 dígitos')


def validacion_completa(usuario, user, contrasena, password):
    if usuario == user and contrasena == password:
        print('Bienvenida al sistema, tu Login está completo')
    elif usuario == user and contrasena != password:
        print('Tu contraseña es incorrecta, intenta de nuevo')
    elif usuario != user and contrasena == password:
        print('Tu Email es incorrecto, intenta de nuevo')
    else:
        print('Tu email y contraseña son incorrectos, intenta de nuevo')
