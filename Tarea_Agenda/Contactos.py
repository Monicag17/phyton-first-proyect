from Tarea_Agenda.Agenda import Contacto

Agendamiento = [
         Contacto("Monica", "Gutierrez", "Guti", 3219885780),
         Contacto("Pedro", "Rojas", "Pedrito", 3259638877),
         Contacto("Edwar", "Aparicio", "Apa", 3143426804),
         Contacto("Camila", "Gonzalez", "Cami", 3123675528),
         Contacto("Angela", "Gaitan", "Angelita", 3142518101)
]

for contacto in Agendamiento:
    print(contacto.nombre_contacto(), contacto.apellido_contacto(), contacto.apodo_contacto(), contacto.numero_contacto())

