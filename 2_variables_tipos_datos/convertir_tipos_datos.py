#convertir los tipos de datos
#nota: solo es posible en una concatencion concaterar entre tipos de datos iguales

texto= "soy una cadena"
numero= 23
print(texto)
print (numero)

print (texto+" y soy una cadena2")
print(numero+34)

#converitr un tipo de datos int a str
numero_str=str(numero)
print(texto+numero_str)

print (texto+"" +str (numero))

#convertir un STR a INT
n1=33
suma=int('23')+n1
print(suma)
#convertir a un float a Int
n1=33
n2=33.0
suma=n1+n2
print (suma)

print (f"lasuma es: {suma}")
