from conexionBD import *

micursor=conexion.cursor()
sql="delete from clientes where id=1"

micursor.execute(sql)
conexion.commit()

if micursor:
    print("Registro Eliminado Correctamente")