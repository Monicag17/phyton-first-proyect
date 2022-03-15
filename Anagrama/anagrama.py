print("Anagrama simple")

palabra1 = str(input("Por favor escribar la primera palabra  "))
palabra2 = str(input("Por vaor escriba las segunda palabra  "))


def ordenar_palabras(palabra1, palabra2):
    ordenada1 = sorted(palabra1)
    ordenada2 = sorted(palabra2)

    print("La palabra 1 ordenada se ve de la siguiente manera: ", ordenada1)
    print("La palabra 2 ordenada se ve de la siguiente manera: ", ordenada2)

    if ordenada1 == ordenada2:
        print("Las palabras son un anagrama")
    else:
        print("Las palabras no son un anagrama")

ordenar_palabras(palabra1, palabra2)
