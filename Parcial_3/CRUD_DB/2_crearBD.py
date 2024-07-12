import mysql.connector
try:
#crear la conexion con la BD
    conexion=mysql.conector.connect(
        host='localhost',
        user='root',
        password='',
    )
except:
     print(f"Ocurrio un problema con el servidor ... por favor intentalo más tarde...")
else:
#Verificar la conexión
    if conexion.is_connected():
        print("se creo la conexión con éxito.")
    else:
        print("No fue posible conectarse.")
    
#crear otro objeto para ejecutar las instrucciones
    micursor=conexion.cursor()

#crear BD desde python
    sql="create database bd_python"
    micursor.execute (sql)

#verificar que se creo la BD
    if micursor:
        print('Se creo la BD exitosamente')
    
#Mostrar las BD que existen en mi servidor MySQL
    micursor.execute("show databases")

    for x in micursor:
        print(x)
        