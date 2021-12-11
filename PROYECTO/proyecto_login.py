import re


def bienvenida_programa():
    print('Bienvenida, este programa simula el proceso de Login usando Phyton')
    print('Bienvenida, Señorita Monica')


def validar_correo(Usuario1, validacion, Usuario):
    if len(Usuario1) == 0:
        print('El usuario está vacío. Usuario No Valido')
    elif validacion != -1:
        print('Email encontrado')
        if Usuario1 == Usuario:
            print('Usuario Correcto')
        else:
            print('Usuario Incorrecto')
    else:
        print('Email no encontrado. Usuario No Valido')


def validar_contrasena(Contrasena1, Contrasena):
    if len(Contrasena1) == 0:
        print('La contraseña está vacía. Contraseña no valida')
    elif 8 <= len(Contrasena1) <= 20:
        if re.search('[a-z]', Contrasena) and re.search('[0-9]', Contrasena):
            if Contrasena == Contrasena1:
                print('Contraseña Correcta')
            else:
                print('Contrasena Incorrecta')
    elif len(Contrasena1) < 8:
        print('Contraseña Incorrecta. Tú contraseña no cuenta con el mínimo de 8 dígitos')


def validacion_completa(Usuario, Usuario1, Contrasena, Contrasena1):
    if Usuario == Usuario1 and Contrasena == Contrasena1:
        print('Bienvenida al sistema, tu Login está completo')
    elif Usuario == Usuario1 and Contrasena != Contrasena1:
        print('Tu contraseña es incorrecta, intenta de nuevo')
    elif Usuario != Usuario1 and Contrasena == Contrasena1:
        print('Tu Email es incorrecto, intenta de nuevo')
    else:
        print('Tu email y contraseña son incorrectos, intenta de nuevo')


def login_complete():

    bienvenida_programa()
    Usuario = 'moniks.17@hotmail.com'
    Contrasena = '3219885780empanadas'

    print("Por favor digite su Usuario")
    Usuario1 = input('Correo: ')
    print('Por favor digite su Contraseña')
    Contrasena1 = input('Contraseña: ')
    validacion = Usuario1.find("@hotmail.com")
    validar_correo(Usuario1, validacion, Usuario)
    validar_contrasena(Contrasena1, Contrasena)
    validacion_completa(Usuario1, Usuario, Contrasena, Contrasena1)


login_complete()
