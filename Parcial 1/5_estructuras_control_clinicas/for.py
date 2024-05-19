# El for es una estructura de control repetitiva o ciclica que funciona con iteraciones X veces de acuerdo a los valores numericos enteros que contenga

# Sintaxi: 

# for variable in elemento_iterable(list, range, etc):
#     bloque instrucciones

#Ejemplo 1 Crear un programa que imprima 5 veces el caracter @

# for contador in range(1,6):
#     print("@")
 
#Ejemplo 2 Crear un programa que imprima los numeros del 1 a 5, los sume e imprima la suma al final
# suma=0
# for contador in range(1,6):
#     print(contador)
#     suma+=contador
# print(f"La suma es: {suma}")


# Ejemplo 3 Crear un programa que solicite un numero entero y apartir de este numero genere e imprima la tabla de multiplicar correspondiente

numero=int(input("Ingrese un numero: "))

multi=0
for i in range(1,11):
    multi=numero*i
    print(f"{numero} X {i} = {multi}")