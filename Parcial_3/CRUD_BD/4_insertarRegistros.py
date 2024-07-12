 #1er forma

# import conexionBD

# micursor=conexionBD.conexion.cursor() 

# sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Daniel Contreras', 'Col. centro', '6181234567')"
# micursor.execute(sql)
# #Es necesario para que al final se complete el Execute(sql) y finalice la consulta SQL
# conexionBD.conexion.commit() 

# if micursor:
#     print(f"Registro Insertado con Exito")


#2da forma

from conexionBD import *
try:
    micursor=conexion.cursor()

    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Daniel Contreras', 'Col. centro', '6181234567')"
    micursor.execute(sql)
#Es necesario para que al final se complete el Execute(sql) y finalice la consulta SQL
    conexion.commit() 

except:
    print(f"ocurriio un probelma con el servidor porfavor intetelo mas tarde")
else:
    print(f"registro insetado correctamente")
