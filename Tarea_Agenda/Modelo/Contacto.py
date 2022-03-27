print("Agenda de Contactos")


class Contacto:

    nombre = ""
    apellido = ""
    apodo = ""
    telefono = ""
    correo = ""
    cumple = ""

    def __init__(self, nombre, apellido, apodo, telefono, correo, cumple):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono
        self.correo = correo
        self.cumple = cumple

    def nombre_contacto(self):
        return self.nombre

    def apellido_contacto(self):
        return self.apellido

    def apodo_contacto(self):
        return self.apodo

    def numero_contacto(self):
        return self.telefono

    def correo_contacto(self):
        return self.correo

    def cumple_contacto(self):
        return self.cumple

    def exportar(self):
        return [{"nombre": self.nombre, "apellido": self.apellido,
                "apodo": self.apodo, "numero": self.telefono,
                "correo": self.correo, "cumple": self.cumple}]







