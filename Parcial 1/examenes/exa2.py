
while: True
peso=int(input("ingrese peso"))
altura=float(input("ingrese altura"))

IMC= peso / altura * altura
print(IMC)
if IMC >=30.0:
    print("obesidad")
elif IMC <=29.99:
    print ("peso normal")

if IMC <=24.9:
    print("nomral")
elif IMC <=18.5:
    print ("inferioir")


