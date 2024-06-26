
tabla_lista = [
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]


tabla_diccionario = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

# Imprimimos la lista y el diccionario
print("Lista:")
for fila in tabla_lista:
    print(fila)

print("\nDiccionario:")
for categoria, peliculas in tabla_diccionario.items():
    print(f"{categoria}: {peliculas}")
