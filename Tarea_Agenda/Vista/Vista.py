from Modelo.Contacto import Contacto


class Vista:

    def seleccion_menu(self):
        print("Por favor digite la opción que requiere")
        print("1. Agregar Contacto")
        print("2. Exportar Contacto")
        print("3. Listar Contactos")
        print("4. Cargar contacto")
        print("5. Buscar contacto")
        print("6. Agregar numero de telefono")
        print("7. Crear grupo de contactos")
        print("8. Generar copia de seguridad")
        print("9. Saber si algún contacto cumple años")
        print("10. Salir del programa")
        return int(input("Ingrese la opción que desee    "))

    def datos_contacto(self):
        nombre = str(input("Ingrese el nombre"))
        apellido = str(input("Ingrese el apellido"))
        apodo = str(input("Ingrese el apodo"))
        telefono = self.agregar_telefonos()
        correo = str(input("Ingrese el correo electrónico, incluyendo @"))
        cumple = str(input("Ingrese su fecha de cumpleaños"))
        return Contacto(nombre, apellido, apodo, telefono, correo, cumple)

    def agregar_telefonos(self):
        telefonos = []
        mostrar_menu = True
        while mostrar_menu:
            telefono = int(input('Ingrese numero de telefono'))
            telefonos.append(telefono)
            mostrar_menu = self.agregar_telefono_menu()
        return telefonos
        

    def agregar_telefono_menu(self):
        print('1. Agregar telefono')
        print('2. No agregar mas numeros')
        return int(input('Seleccione una opcion')) == 1
    

    def contacto_creado_correctamente(self):
        print("Contacto creado de forma correcta")

    def nombre_de_carpeta(self):
        return str(input("Digite el nombre del archivo a donde quiere asignar su contacto "))

    def accion_correcta(self):
        print("Accion realizada correctamente")

    def accion_incorrecta(self):
        print("Accion no realizada")

    def buscar_contacto(self):
        return str(input("Digite el nombre del contacto que desea obtener  "))

    def cumple_contacto(self):
        return str(input("Digite el nombre de la persona que busca"))

    def imprimir_resultados(self, contactos):
        for contacto in contactos:
            print(contacto.exportar())
        self.espera()

    def espera(self):
        input("Enter para continuar")

    def salir_programa(self):
        print("Hasta pronto, FIN DEL PROGRAMA")



