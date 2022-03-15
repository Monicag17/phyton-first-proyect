from Modelo.Contacto import Contacto


class Vista:

    def seleccion_menu(self):
        print("Por favor digite la opción que requiere")
        print("1. Agregar Contacto")
        print("2. Exportar Contacto")
        print("3. Listar Contactos")
        print("4. Cargar contacto")
        print("5. Buscar contacto")
        print("6. Agregar otro número de teléfono a un mismo contacto")
        print("7. Crear grupo de contactos")
        print("8. Generar copia de seguridad")
        print("9. Saber si algún contacto cumple años")
        print("10. Salir del programa")
        return int(input("Ingrese la opción que desee    "))

    def datos_contacto(self):
        nombre = str(input("Ingrese el nombre"))
        apellido = str(input("Ingrese el apellido"))
        apodo = str(input("Ingrese el apodo"))
        numero = int(input("Ingrese el numero"))
        correo = str(input("Ingrese el correo electrónico, incluyendo @"))
        cumple = str(input("Ingrese su fecha de cumpleaños"))
        return Contacto(nombre, apellido, apodo, numero, correo, cumple)

    def contacto_creado_correctamente(self):
        print("Contacto creado de forma correcta")

    def nombre_de_carpeta(self):
        return str(input("Digite el nombre del grupo de amigos o familiar que desea  "))

    def accion_correcta(self):
        print("Accion realizada correctamente")

    def accion_incorrecta(self):
        print("Accion no realizada")

    def salir_programa(self):
        print("Hasta pronto, FIN DEL PROGRAMA")



