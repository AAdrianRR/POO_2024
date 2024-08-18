import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="parqueo_gui_nuevo_db"
        )
        self.cursor = self.connection.cursor()

    def insertar_empleado(self, empleado):
        query = "INSERT INTO empleados (nombre) VALUES (%s)"
        self.cursor.execute(query, (empleado.nombre,))
        self.connection.commit()

    def registrar_auto_cliente_ticket(self, vehiculo, cliente):
        query_auto = "INSERT INTO autos (placa, marca, modelo, tipo) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query_auto, (vehiculo.placa, vehiculo.marca, vehiculo.modelo, vehiculo.tipo))
        self.connection.commit()

        auto_id = self.cursor.lastrowid

        query_cliente = "INSERT INTO clientes (nombre, telefono) VALUES (%s, %s)"
        self.cursor.execute(query_cliente, (cliente.nombre, cliente.telefono))
        self.connection.commit()

        cliente_id = self.cursor.lastrowid

        query_ticket = "INSERT INTO tickets (auto_id, cliente_id, fecha_entrada) VALUES (%s, %s, NOW())"
        self.cursor.execute(query_ticket, (auto_id, cliente_id))
        self.connection.commit()

        ticket_id = self.cursor.lastrowid
        return ticket_id

    def consultar_autos_en_estacionamiento(self):
        query = """
        SELECT a.placa, a.marca, a.modelo
        FROM autos a
        JOIN tickets t ON a.id = t.auto_id
        WHERE t.fecha_salida IS NULL
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def obtener_ticket_por_placa(self, placa):
        query = """
        SELECT t.id, t.fecha_entrada, c.nombre
        FROM tickets t
        JOIN autos a ON t.auto_id = a.id
        JOIN clientes c ON t.cliente_id = c.id
        WHERE a.placa = %s AND t.fecha_salida IS NULL
        """
        self.cursor.execute(query, (placa,))
        return self.cursor.fetchone()

    def obtener_tarifa_por_hora(self):
        query = "SELECT precio_por_hora FROM tarifas WHERE id = 1"
        self.cursor.execute(query)
        tarifa = self.cursor.fetchone()
        return tarifa[0] if tarifa else 0

    def registrar_salida(self, placa, fecha_salida, costo):
        query = """
        UPDATE tickets t
        JOIN autos a ON t.auto_id = a.id
        SET t.fecha_salida = %s, t.costo = %s
        WHERE a.placa = %s AND t.fecha_salida IS NULL
        """
        self.cursor.execute(query, (fecha_salida, costo, placa))
        self.connection.commit()
