"""
Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas 
pequeño que cumple una funcion especifica. La funcion se puede reutilizar con el simple hecho
de invocarla es decir manadarla llamar

sintaxis
def nombreDeMiFuncion(parametros):
    bloque o conjunto de instrucciones

    nombreDeMiFuncion(parametros)


Las funciones pueden ser de 4 tipos 
1- Funcion que no recibe parametros y no regresa valor

2-Funcion que no recibe parametros y regresa valor

3- Funcion que recibe parametro y no regresa valor
4-Funcion que recibe parametro y  regresa valor

"""
# #1 Funcion que no recibe parametros y no regresa valor
def sumaNumeros1():
    n1 = int(input("Numero 1:"))
    n2 = int(input("Numero 2:"))
    suma = n1 + n2
    print(f"{n1}+{n2}={suma}")

# sumaNumeros1()

# #2 Funcion que no recibe parametros y regresa valor
def sumaNumeros2():
    n1 = int(input("Numero 1:"))
    n2 = int(input("Numero 2:"))
    suma = n1 + n2
    return f"{n1}+{n2}={suma}"
print(sumaNumeros2())

# #3 Funcion que recibe parametro y no regresa valor
def sumaNumeros3(n1,n2):
    suma = n1 + n2
    print( f"{n1}+{n2}={suma}")
n1 = int(input("Numero 1:"))
n2 = int(input("Numero 2:"))
sumaNumeros3(n1,n2)

# #4 Funcion que recibe parametro y  regresa valor + USADO
def sumaNumeros4(n1,n2):
    suma = n1 + n2
    return f"{n1}+{n2}={suma}"
n1 = int(input("Numero 1:"))
n2 = int(input("Numero 2:"))
sumaNumeros4(n1,n2)

#Ejemplo: Crear un programa que solicite a traves de una funcion la siguiente informacion:
#Nombre del paciente, edad, estatura, tipo de sangre
#utilizar los 4 tipos de funciones

#1 Funcion que no recibe parametros y no regresa valor
def paciente1():
    nombre = input("Nombre del paciente: ")
    edad = int(input("Edad: "))
    estatura = float(input("Estatura: "))
    tipo_sangre = input("Tipo de sangre: ")
    print(f"Nombre del paciente: {nombre}\nEdad: {edad}\nestatura: {estatura}\ntipo de sangre: {tipo_sangre}")
paciente1()

#2 Funcion que no recibe parametros y regresa valor
def paciente2():
    nombre = input("Nombre del paciente: ")
    edad = int(input("Edad: "))
    estatura = float(input("Estatura: "))
    tipo_sangre = input("Tipo de sangre: ")
    return(f"Nombre del paciente: {nombre}\nEdad: {edad}\nestatura: {estatura}\ntipo de sangre: {tipo_sangre}")
print(paciente2())

#3 Funcion que recibe parametro y no regresa valor
def paciente3(nombre,edad,estatura,tipo_sangre):

    print(f"Nombre del paciente: {nombre}\nEdad: {edad}\nestatura: {estatura}\ntipo de sangre: {tipo_sangre}")
    nombre = input("Nombre del paciente: ")
    edad = int(input("Edad: "))
    estatura = float(input("Estatura: "))
    tipo_sangre = input("Tipo de sangre: ")
print(paciente3())

 #4 Funcion que recibe parametro y  regresa valor + USADO
def paciente4(nombre,edad,estatura,tipo_sangre):

  return f"Nombre del paciente: {nombre}\nEdad: {edad}\nestatura: {estatura}\ntipo de sangre: {tipo_sangre}"
nombre = input("Nombre del paciente: ")
edad = int(input("Edad: "))
estatura = float(input("Estatura: "))
tipo_sangre = input("Tipo de sangre: ")
  
paciente4(nombre,edad,estatura,tipo_sangre)