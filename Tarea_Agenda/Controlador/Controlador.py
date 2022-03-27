from Modelo.Contacto import Contacto
import json
from Vista.Vista import Vista
from Modelo.GrupoContactos import GrupoContactos



class Controlador:

    def __init__(self):
        self.opcion_seleccionada = 0
        self.nombre_contacto = ""
        self.vista = Vista()
        self.contactos = []
        self.telefono = []
        self.lista_grupo = []


    def opciones(self):
        while self.opcion_seleccionada != 8:
            self.opcion_seleccionada = self.vista.seleccion_menu()

            if self.opcion_seleccionada == 1:
                self.agregar_contacto()

            if self.opcion_seleccionada == 2:
                self.exportar_contacto()

            if self.opcion_seleccionada == 3:
                self.listar_contactos()

            if self.opcion_seleccionada == 4:
                self.cargar_contactos()

            if self.opcion_seleccionada == 5:
                self.buscar_contacto()

            if self.opcion_seleccionada == 6:
                self.crear_grupo()

            if self.opcion_seleccionada == 7:
                self.exportar_grupo()

            if self.opcion_seleccionada == 8:
                self.salir_del_programa()

    def agregar_contacto(self):
        contacto_nuevo = self.vista.datos_contacto()
        self.contactos.append(contacto_nuevo)
        self.vista.contacto_creado_correctamente()

    def exportar_contacto(self):
        nombre_carpeta = self.vista.nombre_de_carpeta()
        lista_exportacion = []
        for contacto_nuevo in self.contactos:
            lista_exportacion.append(contacto_nuevo.exportar())

        with open(f"datos/{nombre_carpeta}.json", "w") as fp:
            json.dump(lista_exportacion, fp)

        self.vista.accion_correcta()

    def listar_contactos(self):
        for contacto_nuevo in self.contactos:
            print(contacto_nuevo.exportar())

    def cargar_contactos(self):
        try:
            with open("datos/contactos.json", "r") as fp:
                datos = json.load(fp)

            for contacto_nuevo in datos:
                self.contactos.append(
                    Contacto(
                        nombre=contacto_nuevo["nombre"],
                        apellido=contacto_nuevo["apellido"],
                        apodo=contacto_nuevo["apodo"],
                        telefono=contacto_nuevo["telefono"],
                        correo=contacto_nuevo["correo"],
                        cumple=contacto_nuevo["cumple"]
                    )
                )

        except Exception as e:
            self.vista.accion_correcta(e)

    def buscar_contacto(self):
        resultados = []
        nombre_contacto = self.vista.buscar_contacto()
        for contacto in self.contactos:
            if contacto.nombre == nombre_contacto:
                resultados.append(contacto)
                break
        self.vista.imprimir_resultados(resultados)

    def crear_grupo(self):
        grupo_nuevo = self.vista.grupos()
        self.lista_grupo.append(grupo_nuevo)
        self.vista.accion_correcta()

    def exportar_grupo(self):
        nombre_carpeta = self.vista.nombre_de_carpeta()
        grupo_exportacion = []
        for grupo_nuevo in self.lista_grupo:
            grupo_exportacion.append(nombre_carpeta.exportar1())

        with open(f"datos/{nombre_carpeta}.json", "w") as fp:
            json.dump(grupo_exportacion, fp)

        self.vista.accion_correcta()

    def cumple_contactos(self):
        pass

    def salir_del_programa(self):
        self.vista.salir_programa()
