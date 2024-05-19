

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1


print(f"Números impares entre {num1} y {num2}:")
for num in range(num1, num2 + 1):
    if num % 2 != 0:
        print(num)