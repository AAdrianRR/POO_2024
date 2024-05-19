
aprobados = 0
reprobados = 0


for i in range(1, 16):
    calificacion = float(input(f"Introduce la calificación del alumno {i}: "))
    
 
    if calificacion >= 80:
        aprobados += 1
    else:
        reprobados += 1


print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")