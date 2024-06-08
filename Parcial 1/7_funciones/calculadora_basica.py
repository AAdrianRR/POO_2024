# opcion=True
# while opcion:
#     print(".:: CALCULADORA BÁSICA ::. \n 1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División \n 5.-SALIR")
#     opcion=input("\t Elige una opción: ").upper()

#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#         n1=int(input("Número #1: "))
#         n2=int(input("Número #2: "))
#         suma=n1+n2
#         print(f"{n1}+{n2}={suma}")
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#         n1=int(input("Número #1: "))
#         n2=int(input("Número #2: "))
#         resta=n1-n2
#         print(f"{n1}-{n2}={resta}")
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#         n1=int(input("Número #1: "))
#         n2=int(input("Número #2: "))
#         multi=n1*n2
#         print(f"{n1}X{n2}={multi}")
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
#         n1=int(input("Número #1: "))
#         n2=int(input("Número #2: "))
#         divi=n1/n2
#         print(f"{n1}/{n2}={divi}")
#     else:
#         print("Terminaste la ejecución del SW")
#         opcion=False

from os import system
def solicitarNumeros():
  global n1,n2  
  n1=int(input("Numero #1: "))
  n2=int(input("Numero #2: "))
  

def operacionAritmetica(num1,num2,opcion):  
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
      return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
     return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
     return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
     return f"{n1}/{n2}={n1/n2}"  



opcion=True    
while opcion:
 print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
 opcion=input("\t Elige una opción: ").upper()
 
 if opcion!="5":
    solicitarNumeros()
    print(operacionAritmetica(n1,n2,opcion))
 else:
   opcion=False
   print("Terminaste la ejecución del SW")