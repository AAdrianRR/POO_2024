class Vehiculo:
    def __init__(self, placa, marca, modelo, tipo=None):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

class Auto(Vehiculo):
    def __init__(self, placa, marca, modelo, puertas, tipo="Auto"):
        super().__init__(placa, marca, modelo, tipo)
        self.puertas = puertas

class Cliente:
    def __init__(self, nombre, telefono=None):
        self.nombre = nombre
        self.telefono = telefono

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Ticket:
    def __init__(self, id_ticket, fecha_entrada, fecha_salida=None, costo=None):
        self.id_ticket = id_ticket
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.costo = costo

    def calcular_costo(self, tarifa_por_hora):
        if self.fecha_salida:
            tiempo_estacionado = (self.fecha_salida - self.fecha_entrada).total_seconds() / 3600.0
            self.costo = tiempo_estacionado * tarifa_por_hora
        else:
            self.costo = 50.0
        return self.costo
