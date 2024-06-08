contador = 0  

while True:
    peso = int(input("Ingrese peso "))
    altura = float(input("Ingrese altura (en metros): "))
    
    IMC = peso / (altura * altura)
    print(f"IMC: {IMC:.2f}")
    
    if IMC >= 30.0:
        print("obesidad")
    elif 25.0 <= IMC < 30.0:
        print("sobrepeso")
    elif 18.5 <= IMC < 25.0:
        print("normal")
    else:
        print("bajo")
    
    contador += 1  # Incrementamos el contador

    continuar = input("¿Desea continuar? si o no:")
    if continuar != 'si':
        break

print(f"Se realizaron {contador} cálculos de IMC.")
