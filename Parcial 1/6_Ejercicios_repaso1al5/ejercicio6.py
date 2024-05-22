
def tabla(numero):
    print(f"la Tabala (){numero}:")
    for q in range(1, 11):
        print(f"{numero} x {q} = {numero * q}")
    print()

for num in range(1, 11):
    tabla(num)