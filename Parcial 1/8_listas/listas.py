''''
List(Array)
son collecciones o conjuntos de datos/valores bajo
un mismo nombre,para acceder a los valores se
hace con un indice numerico

Nota:sus valores si son modificables

La lista ees una coleccion ordenada y modificable.
Permite miembors duplicados.
'''
# # #Ejemplo 1 crear una lista de numeros e imprimir el contenido
# numeros=[23,34]
# print("Contenido de la lista")
# for numero in numeros:
#  print(numero)
# #recorrer la lsita con ciclo for
# for numero in numeros:
#      print(numero)

# #Recorrer la lista con el ciclo while
# numero=0
# tamanio=len(numeros)
# print(tamanio)
# while numero<=len(numeros)-1:
#     print(numeros[numero])
#     numero+=1
# #Ejemplo2
# #crear una lista de palabras, posteriormente buscar la coincidencia de una palabra
# palabra = ["hola","utd", "como", "estas", "ok", "ok", "naranja"]
# palabra_buscar = input("inserta palabra a buscar: ")

# encontrada=False
# posicion=0
# while not encontrada and posicion < len(palabra):
#    if palabra[posicion]==palabra_buscar:
#       encontrada=True
#    else:
#     posicion +=1
#    if encontrada:
#       print(f"{palabra_buscar} esta en la lista y se encontro en la posicion {posicion}")
#    else:
#       print(f"{palabra_buscar} no se encontro en la lista")
# #EJEMPLO WHILE
# palabra = ["hola", "utd", "como", "estas", "ok", "naranja"]
# palabra_buscar = input("Inserta una palabra a buscar: ")
# i = 0
# while i < len(palabra):
#     if palabra[i] == palabra_buscar:
#         print(f"Encontré la palabra en la posición {i}")
#         break  
#     i += 1
# else:
#     print("No encontré la palabra en la lista")

# #if palabra_buscar in palabra:
# #    for i, p in enumerate(palabra):
# #        if p == palabra_buscar:
# #            print(f"Encontré la palabra en la posición {i}")
# #else:
# #    print("No encontré la palabra en la lista")

# #EJEMPLO 3 AGREGAR Y ELIMINAR ELEMENTOS DE UNA LISTA
# #OS.SYSTEM("CLEAR")
# numeros=[23,34,23]
# print(numeros)
# #agregar un elemento
# numeros.append(100)
# print(numeros)
# numeros.insert(3,200)
# print(numeros)
# #Eliminar un elemento
# numeros.remove(100)#indicar el elemento a borrar
# print(numeros)
# numeros.pop(2)#Indicar la posicion del elemento a borrar
# print(numeros)
# #Ejemplo 4 Crear una lista multilinea (matriz) para agregar los nombres y numeros telefonicos
# agenda=[
#    ["Carlos",6181234567],
#    ["Leo",6181234568],
#    ["Sebastian",6181234569],
#    ["Pedro",6181234560]
# ]
# print(agenda)
# for i in agenda:
#    print(f"{agenda.index(i)+1}.-{i}")
#EJEMPLO 5 CREAR UN PROGRAMA QUE PERMITA GESTIONAR (ADMINISTRAR) PELICULAS, COLOCAR UN MENU DE OPCIONES PARA AGREGAR,REMOVER,CONSULTAR PELICULAS.
#NOTAS:
#1.-UTILIZAR FUNCIONES Y MANDAR LLAMAR DESDE OTRO ARCHIVO
#2.-UTILIZAR LSITAS PARA ALMACENAR LOS NOMBRES DE LAS PELICULAS
'''
from peliculas_funciones import *
def menu():
 print("\n\t..::: PELICULAS PIRATAS 4K  :::...\n 1.-AGREGAR PELICULAS\n 2.-REMOVER PELICULA\n 3.-CONSULTAR CATALOGO\n 4.- SALIR")
if __name__=="__menu__":
 menu()
while True:
 menu()
 opcion=input("QUE OPCION ELEGIRAS HOY:")
 if opcion=="1":
  nombre_pelicula=input("INGRESA EL NOMBRE DE LA PELICULA:")
  agregar_peliculas(nombre_pelicula)
 elif opcion=="2":
  nombre_pelicula=input("INGRESA LA PELICULA QUE DESEAS REMOVER:")
  remover_pelicula(nombre_pelicula)
 elif opcion=="3":
  consultar_pelicula()
 elif opcion=="4":
  print("PTM NO ME SALE")
  break
 else:
  print("LA OPCION QUE INGRESASTE NO EXISTE")
  '''
import os
import msvcrt
from peliculas_funciones import *

def mostrar_menu():
    print("\n\t....::::PeLiCuLaS PiRaTaS 4k::::....")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Actualizar película")
    print("5. Buscar película")
    print("6. Salir")

def pausa():
    print("\nPRESIONA UNA TECLA PARA CONTINUAR...")
    msvcrt.getch()

if __name__ == "__main__":
    while True:
        os.system("cls")
        mostrar_menu()
        opcion = input("QUE OPCION ELEGIRAS HOY: ")
        if opcion == "1":
            os.system("cls")
            nombre_pelicula = input("Ingresa el nombre de la película: ")
            agregar_pelicula(nombre_pelicula)
            pausa()
        elif opcion == "2":
            os.system("cls")
            nombre_pelicula = input("Ingresa el nombre de la película a remover: ")
            remover_pelicula(nombre_pelicula)
            pausa()
        elif opcion == "3":
            os.system("cls")
            consultar_peliculas()
            pausa()
        elif opcion == "4":
            os.system("cls")
            nombre_actual = input("Ingresa el nombre de la película a actualizar: ")
            nombre_nuevo = input("Ingresa el nuevo nombre de la película: ")
            actualizar_pelicula(nombre_actual, nombre_nuevo)
            pausa()
        elif opcion == "5":
            os.system("cls")
            nombre_buscar = input("Ingresa el nombre de la película a buscar: ")
            buscar_pelicula(nombre_buscar)
            pausa()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("LA OPCION QUE INGRESASTE NO EXISTE")
            pausa()
