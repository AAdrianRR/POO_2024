


nombre=input("nombre del trabjo")
horas=int(input("horas trabajas"))
sueldo=int(input("ingrese sueldo"))

Paga=horas * sueldo
semanas= Paga*5
mes=semanas*4
print ("el sueldo por semana es", semanas) 
print("el sueldo por mes es", mes)
if mes <=10000:
    print("obrero tipo a")
elif mes <=15000:
    print("el obrero es tipo b")
else: 
    print( "sin categorita")



