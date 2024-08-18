import mysql.connector
from models import Auto, Moto

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculo (
            placa VARCHAR(10) PRIMARY KEY,
            marca VARCHAR(50),
            modelo VARCHAR(50)
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS auto (
            placa VARCHAR(10),
            tipo_combustible VARCHAR(20),
            FOREIGN KEY (placa) REFERENCES vehiculo(placa)
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS moto (
            placa VARCHAR(10),
            tipo_casco VARCHAR(20),
            FOREIGN KEY (placa) REFERENCES vehiculo(placa)
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS ticket (
            numero INT AUTO_INCREMENT PRIMARY KEY,
            hora_entrada DATETIME,
            hora_salida DATETIME,
            vehiculo_placa VARCHAR(10),
            FOREIGN KEY (vehiculo_placa) REFERENCES vehiculo(placa)
        )
        """)
        self.connection.commit()

    def add_vehiculo(self, vehiculo):
        self.cursor.execute("INSERT INTO vehiculo (placa, marca, modelo) VALUES (%s, %s, %s)", (vehiculo.placa, vehiculo.marca, vehiculo.modelo))
        if isinstance(vehiculo, Auto):
            self.cursor.execute("INSERT INTO auto (placa, tipo_combustible) VALUES (%s, %s)", (vehiculo.placa, vehiculo.tipo_combustible))
        elif isinstance(vehiculo, Moto):
            self.cursor.execute("INSERT INTO moto (placa, tipo_casco) VALUES (%s, %s)", (vehiculo.placa, vehiculo.tipo_casco))
        self.connection.commit()

    def add_ticket(self, ticket):
        self.cursor.execute("INSERT INTO ticket (hora_entrada, vehiculo_placa) VALUES (%s, %s)", (ticket.hora_entrada, ticket.vehiculo.placa))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
