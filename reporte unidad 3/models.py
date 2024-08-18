from datetime import datetime

class Vehiculo:
    def __init__(self, placa, marca, color):
        self.placa = placa
        self.marca = marca
        self.color= color

    def obtener_detalles(self):
        return f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.color}"

class Auto(Vehiculo):
    def __init__(self, placa, marca, color,):
        super().__init__(placa, marca, color)
        

    def obtener_detalles(self):
        detalles_base = super().obtener_detalles()
        return f"{detalles_base}, Tipo de Combustible: {self.tipo_combustible}"

class Moto(Vehiculo):
    def __init__(self, placa, marca, modelo, tipo_casco):
        super().__init__(placa, marca, modelo)
        self.tipo_casco = tipo_casco

    def obtener_detalles(self):
        detalles_base = super().obtener_detalles()
        return f"{detalles_base}, Tipo de Casco: {self.tipo_casco}"

class Ticket:
    def __init__(self, numero, hora_entrada, vehiculo):
        self.numero = numero
        self.hora_entrada = hora_entrada
        self.hora_salida = None
        self.vehiculo = vehiculo

    def calcular_tiempo_estadia(self):
        if self.hora_salida:
            delta = self.hora_salida - self.hora_entrada
            return delta.total_seconds() / 3600  # horas
        return 0

    def calcular_costo(self, tarifa_por_hora):
        tiempo_estadia = self.calcular_tiempo_estadia()
        return tiempo_estadia * tarifa_por_hora

class Estacionamiento:
    def __init__(self, nombre, direccion, capacidad):
        self.nombre = nombre
        self.direccion = direccion
        self.capacidad = capacidad
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        if len(self.vehiculos) < self.capacidad:
            self.vehiculos.append(vehiculo)
        else:
            raise Exception("Capacidad máxima alcanzada")

    def remover_vehiculo(self, vehiculo):
        if vehiculo in self.vehiculos:
            self.vehiculos.remove(vehiculo)
        else:
            raise Exception("Vehículo no encontrado")

    def obtener_disponibilidad(self):
        return self.capacidad - len(self.vehiculos)
