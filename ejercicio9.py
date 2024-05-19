# Iniciar un bucle infinito
while True:
    # Solicitar al usuario que introduzca un número
    numero = int(input("Introduce un número (111 para salir): "))
    
    # Verificar si el número es 111
    if numero == 111:
        print("Número 111 introducido, finalizando el programa.")
        break  # Salir del bucle
    else:
        # Si no es 111, mostrar el número introducido
        print(f"Número introducido: {numero}")