from venv import create
import mysql.connector

try:
    conexion=mysql.connector.connect(
    host='root',
    password='',
    database='bd_python'

    )
except:
    print(f"no fue posible")


else:
    print(f"se conecto corrrectamente")

#crear tabala

sql="create table clientes(id int primary key auto_increment) nombre vanchar(60), direccion varchar (120), tel verchar(10))"

micursor=conexion.cursor()

micursor.exacute(sql)

if micursor:
    print("se creo la tabla con exito")