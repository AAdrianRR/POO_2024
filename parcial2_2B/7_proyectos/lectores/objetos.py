from clases import Estudiantes, Docentes


estudiante1 = Estudiantes(nombre="Ana Torres Guzman", direccion="Col. Centro 1500 Ote", tel=6181234567, carrera="Meca", matricula=2335678)
docente1 = Docentes(nombre="Daniel Fuentes Loera", direccion="Fracc. D. Arrieta 1400 Nte", tel=61883335678, modalidad="TI", num_empleado=123)


estudiante1.reservar()
estudiante1.entregar()

docente1.reservar()
docente1.entregar()
