import mysql.connector
try:
#conectar cn la bd MysQl
    conexion=mysql.connector.connect(
    host='localhost',
    user='rooy',
    pasword='',
    database='bd_pyhton'
)

except:
    print(f"no fue posible")


