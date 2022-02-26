# Código que suma, resta, multiplica o divide dos números digitados por el usuario


def mensaje_bienvenida():
    print('Calculadora')
    print('Bienevenido Este programa realiza las operaciones básicas de una calculadora')


def menu_opciones():
    print('Menú de opciones, por favor digite la operación que desea')
    print('1. Suma    2. Resta    3. Multiplicación   4. División 5. Finalizar programa  ')
    return int(input())

def menufinalizar_programa():
    print('Desea usted continuar realizando operaciones')
    print(' 1. Si     2. No')
    return int(input())

def numero_operacion():
    print('Por favor digite el número para la operación: ')
    return float(input())


def suma_numeros(numero1, numero2):
    print(f' El resultado de la suma es: {numero1 + numero2}')


def resta_numeros(numero1, numero2):
    print(f'El resultado de la resta es: {numero1 - numero2}')


def multi_numeros(numero1, numero2):
    print(f'El resultado de la multiplicación es: {numero1 * numero2}')


def divi0_numeros(numero2):
    print(f'No se puede dividir en 0, el resultado es indeterminado')


def divi_numeros(numero1, numero2):
    print(f'EL resultado de la división es: {numero1 / numero2}')


def finalizar_programa():
    print('Fin del programa')


mensaje_bienvenida()

operacion = menu_opciones()

while operacion<5:
    numero1 = numero_operacion()
    numero2 = numero_operacion()

    if operacion == 1:
        suma_numeros(numero1, numero2)

    elif operacion == 2:
        resta_numeros(numero1, numero2)

    elif operacion == 3:
        multi_numeros(numero1, numero2)

    elif operacion == 4:
        if numero2 == 0:
            divi0_numeros(numero2)
        else:
            divi_numeros(numero1, numero2)

    else:
        finalizar_programa()

    finalizar = menufinalizar_programa()

    if finalizar == 1:
        operacion = menu_opciones()

    else:
        print('Programa finalizado gracias por utilizar la calculadora')
        break










