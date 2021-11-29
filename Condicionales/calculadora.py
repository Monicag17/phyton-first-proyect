# Código que suma, resta, multiplica o divide dos números digitados por el usuario


print('Calculadora')

print('Menú de opciones, por favor digite la operación que desea')
print('1. Suma    2. Resta    3. Multiplicación   4. División')

operacion = int(input())

if operacion == 1:
    print ('La operación que eligió fue suma, por favor digite el primer número a sumar')
    numero1 = float(input())
    print ('Por favor, digite el segundo número ')
    numero2 = float(input())
    suma = numero1 + numero2
    print (f'El resultado de la suma de los dos números es: {suma} ')

elif operacion == 2:
    print('La operación que eligió fue resta, por favor digite el primer número a restar (Minuendo)')
    numero1 = float(input())
    print('Por favor, digite el segundo número (Sustraendo)')
    numero2 = float(input())
    resta = numero1 - numero2
    print(f'El resultado de la resta de los dos números es: {resta} ')

elif operacion == 3:
    print('La operación que eligió fue multiplicación, por favor digite el primer número a multiplicar')
    numero1 = float(input())
    print('Por favor, digite el segundo número ')
    numero2 = float(input())
    multi = numero1 * numero2
    print(f'El resultado de la multiplicacion de los dos números es: {multi} ')

elif operacion == 4:
    print('La operación que eligió fue división, por favor digite el primer número a dividir (Dividendo)')
    numero1 = float(input())
    print('Por favor, digite el segundo número (Divisor)')
    numero2 = float(input())
    divi = numero1 / numero2
    print(f'El resultado de la división de los dos números es: {divi} ')

else:
    print('El número no está entre las opciones del menú, no se puede realizar ninguna operación')