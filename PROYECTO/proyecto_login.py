import contrasena_usuario


def login_complete():

    contrasena_usuario.bienvenida_programa()
    usuario = 'moniks.17@hotmail.com'
    contrasena = '3219885780empanadas'

    print("Por favor digite su Usuario")
    user = input('Correo: ')
    print('Por favor digite su Contraseña')
    password = input('Contraseña: ')
    validacion = user.find("@hotmail.com")
    contrasena_usuario.validar_correo(user, validacion, usuario)
    contrasena_usuario.validar_contrasena(password, contrasena)
    contrasena_usuario.validacion_completa(user, usuario, contrasena, password)


login_complete()
