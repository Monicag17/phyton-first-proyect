class GrupoContactos:
    nombre_grupo = ""
    lista_personas = []

    def __init__(self, nombre_grupo, lista_personas):
        self.nombre_grupo = nombre_grupo
        self.lista_personas = lista_personas

    def nombre_grupito(self):
        return self.nombre_grupo

    def listar_personis(self):
        return self.lista_personas

    def exportar1(self):
        return [{"nombre_grupo": self.nombre_grupo, "Contactos": self.lista_personas}]
