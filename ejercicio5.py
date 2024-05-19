numero1=int(input("ingrese numero"))
numero2=int(input("ingrese segundo numero"))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1
    print(f"los numeros dentro de el rango son {numero1} y {numero2} son")
    for numero in range (numero1, numero2 + 1):
        print (numero)