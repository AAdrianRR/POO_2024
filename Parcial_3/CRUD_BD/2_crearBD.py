import mysql.connector

try:
    #crear la conexion con la BD
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)
except:
    print(f"no fue posible")


else:
    print(f"se conecto corrrectamente")
#verificar la conexcion


#crear otro objeto para ejecturar las instrucion

micursor=conexion.cursor()

sql= "create database bd_python"
micursor.execute(sql)

if micursor:
    print("se creo la base de datos")

micursor.exacute("show databases")

for x in micursor:
    print(x)