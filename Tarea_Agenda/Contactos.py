from Tarea_Agenda.Agenda import Contacto


def menu_opciones():
    print("Por favor digite la opción que requiere")
    print(" 1. Buscar Contacto   2. Agregar Contacto    3. Eliminar contacto")
    return int(input())


Agendamiento = [
         Contacto("Monica", "Gutierrez", "Guti", 3219885780),
         Contacto("Pedro", "Rojas", "Pedrito", 3259638877),
         Contacto("Edwar", "Aparicio", "Apa", 3143426804),
         Contacto("Camila", "Gonzalez", "Cami", 3123675528),
         Contacto("Angela", "Gaitan", "Angelita", 3142518101)
]
menu_opciones()

for contacto in Agendamiento:
    print(contacto.nombre_contacto(), contacto.apellido_contacto(), contacto.apodo_contacto(), contacto.numero_contacto())