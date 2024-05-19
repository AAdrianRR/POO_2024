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
# Esta estructura de contro evalua una condicion si la condicion se cumple se ejecuta la o las instrucciones contenidas dentro de ella 

# Esta estructura tiene 4 varientes
# 1.- if simple
# 2.- if compuesto
# 3.- if anidado
# 4.- if con el elif

#ejemplo 1 if simple

 #color="rojo"

 #if color=="rojo":
 # print("Soy el color rojo")

#ejemplo 2 if compuesto

# color="rojo"

# if color=="rojo":
#     print("Soy el color rojo")
# else:
#     print("No soy el color rojo")   


#ejemplo 3 if anidado

# color="rojo"

# if color=="rojo":
#     print("Soy el color rojo")
#     if color!="rojo":
#       print("No soy rojo color rojo")
# else:
#     print("No soy el color rojo")   

#ejemplo 4 if y elif 

color=input("Ingresa el color: ")

if color=="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo")   
elif color=="azul":
    print("Soy el color azul")    
elif color=="negro":
    print("Soy el color negro")   
else:
     print("No soy ninguno de los colores anteriores")