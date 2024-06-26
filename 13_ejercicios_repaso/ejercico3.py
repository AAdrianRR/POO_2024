def llenar_lista(lista):
    while True:
        palabra = input("Ingrese una palabra o frase para agregar a la lista (o ingrese 'fin' para terminar): ")
        if palabra.lower() == 'fin':
            break
        lista.append(palabra)

def imprimir_en_mayusculas(lista):
    print("Contenido de la lista en mayúsculas:")
    for palabra in lista:
        print(palabra.upper())


lista_palabras = []


if not lista_palabras:
    print("La lista está vacía.")
    llenar_lista(lista_palabras)


imprimir_en_mayusculas(lista_palabras)
