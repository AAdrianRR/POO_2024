from conexionBD import *

micursor=conexion.cursor()

sql="update clientes set tel='6181112233' where id='4'"
micursor.execute(sql)
conexion.commit()

if micursor:
   print(f"Registro Actualizado Correctamente")