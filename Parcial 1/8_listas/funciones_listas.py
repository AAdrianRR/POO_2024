paises=["Mexico","USA","Brasil","Japon"]
numeros=[23,100,3.1416,0.100]
varios=["Hola",True,100,10.22]

#ordenar la lista

print(paises)
paises.sort()
print(paises)

print(numeros)
paises.sort()
print(numeros)
#VARIOS NO PUEDE PASAR

#Agregar elementos ala lista
print(numeros)
numeros.insert(len(numeros),100)
print(numeros)
numeros.append(100)

#Eliminar elementos de la lista
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(100)

#buscar dentro de una lista
encontrar="Brasil" in paises
print(encontrar)

#Dar la vuelta 
print(varios)
varios.reverse()
print(varios)

#Unir listas
print(paises)
paises.extend(numeros)

#Vacir el contenido de una lista
print(varios)
varios.clear()
print(varios)