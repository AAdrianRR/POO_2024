import mysql.connector
try:
#crear la conexion con la BD
    conexion=mysql.conector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
    )
except:
    print(f"Ocurrio un problema con el servidor ... por favor intentalo más tarde...")

# #comprobar conexion

# if conexion.is_connected():
#     print("Se conecto con la BD")
else:
    #Crear una tabla en un BD ya existente
    sql="""Create table 
    clientes (id int primary key auto_increment,
    nombre varchar(60),
    direccion varchar(60),
    tel varchar(120));"""

    micursor=conexion.cursor()

    micursor.execute(sql)
    
    print("Se creo la tabla con éxito")

