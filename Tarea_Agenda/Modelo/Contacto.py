print("Agenda de Contactos")


class Contacto:

    nombre = ""
    apellido = ""
    apodo = ""
    numero = ""
    correo = ""
    cumple = ""

    def __init__(self, nombre, apellido, apodo, numero, correo, cumple):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.numero = numero
        self.correo = correo
        self.cumple = cumple

    def nombre_contacto(self):
        return self.nombre

    def apellido_contacto(self):
        return self.apellido

    def apodo_contacto(self):
        return self.apodo

    def numero_contacto(self):
        return self.numero

    def correo_contacto(self):
        return self.correo

    def cumple_contacto(self):
        return self.cumple

    def exportar(self):
        return {"nombre": self.nombre, "apellido": self.apellido,
                "apodo": self.apodo, "numero": self.numero,
                "correo": self.correo, "cumple": self.cumple}
