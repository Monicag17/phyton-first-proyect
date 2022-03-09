print("Agenda de Contactos")


class Contacto:

    nombre = ""
    apellido = ""
    apodo = ""
    numero = ""

    def __init__(self, nombre, apellido, apodo, numero):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.numero = numero

    def nombre_contacto(self):
        return self.nombre

    def apellido_contacto(self):
        return self.apellido

    def apodo_contacto(self):
        return self.apodo

    def numero_contacto(self):
        return self.numero


