from models import Auto, Moto, Ticket, Estacionamiento
from database import Database
from datetime import datetime

def main():
    # Conexión a la base de datos
    db = Database(host="localhost", user="root", password="", database="estacionamiento")  # Usa tu configuración de XAMPP
    db.create_tables()

    # Crear instancia de estacionamiento
    estacionamiento = Estacionamiento(nombre="Mi Estacionamiento", direccion="Calle Falsa 123", capacidad=50)

    while True:
        print("\nMenú:")
        print("1. Agregar vehículo")
        print("2. Eliminar vehículo")
        print("3. Ver disponibilidad")
        print("4. Consultar y cobrar ticket de un vehículo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de vehículo (auto/moto): ").lower()
            placa = input("Placa: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")

            if tipo == "auto":
                tipo_combustible = input("Tipo de combustible: ")
                auto = Auto(placa=placa, marca=marca, modelo=modelo, tipo_combustible=tipo_combustible)
                db.add_vehiculo(auto)
                estacionamiento.agregar_vehiculo(auto)
                ticket = Ticket(numero=1, hora_entrada=datetime.now(), vehiculo=auto)
                db.add_ticket(ticket)
            elif tipo == "moto":
                tipo_casco = input("Tipo de casco: ")
                moto = Moto(placa=placa, marca=marca, modelo=modelo, tipo_casco=tipo_casco)
                db.add_vehiculo(moto)
                estacionamiento.agregar_vehiculo(moto)
                ticket = Ticket(numero=1, hora_entrada=datetime.now(), vehiculo=moto)
                db.add_ticket(ticket)
            else:
                print("Tipo de vehículo no reconocido.")

        elif opcion == "2":
            placa = input("Placa del vehículo a eliminar: ")
            if estacionamiento.vehiculo_existe(placa):
                estacionamiento.remover_vehiculo(placa)
                db.remove_vehiculo(placa)
                print("Vehículo eliminado.")
            else:
                print("Vehículo no encontrado en el estacionamiento.")

        elif opcion == "3":
            disponibilidad = estacionamiento.obtener_disponibilidad()
            print(f"Disponibilidad: {disponibilidad} espacios")

        elif opcion == "4":
            placa = input("Ingrese la placa del vehículo: ")
            ticket_info = db.get_ticket_by_placa(placa)
            if ticket_info:
                hora_entrada = ticket_info[1]
                hora_salida = datetime.now()
                
                # Actualizamos la hora de salida en la base de datos
                db.update_ticket_hora_salida(placa, hora_salida)
                
                # Calculamos el tiempo de estadía y el costo
                tiempo_estadia = db.calcular_tiempo_estadia(hora_entrada, hora_salida)
                costo = db.calcular_costo(tiempo_estadia)
                
                print(f"\nDetalles del Ticket:")
                print(f"Ticket Número: {ticket_info[0]}")
                print(f"Hora de Entrada: {hora_entrada}")
                print(f"Hora de Salida: {hora_salida}")
                print(f"Tiempo de Estadia: {tiempo_estadia:.2f} horas")
                print(f"Total a pagar: ${costo:.2f}")
                
                # Remover vehículo del estacionamiento después del cobro
                estacionamiento.remover_vehiculo(placa)
            else:
                print("No se encontró ticket para la placa proporcionada.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida.")

    db.close()

if __name__ == "__main__":
    main()
