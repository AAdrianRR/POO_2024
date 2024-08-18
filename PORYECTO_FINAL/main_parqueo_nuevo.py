import tkinter as tk
from tkinter import messagebox
from database_parqueo_nuevo import Database
from models_parqueo_nuevo import Auto, Cliente, Empleado
from datetime import datetime


db = Database()

def registrar_auto():
    placa = entrada_placa.get()
    marca = entrada_marca.get()
    modelo = entrada_modelo.get()
    puertas = entrada_puertas.get()
    nombre_empleado = entrada_nombre_empleado.get()

    if placa and marca and modelo and nombre_empleado:
        auto = Auto(placa, marca, modelo, puertas)
        db.registrar_auto_cliente_ticket(auto, Cliente(cliente_nombre.get(), cliente_telefono.get()))
        db.insertar_empleado(Empleado(nombre_empleado))
        messagebox.showinfo("Éxito", "Auto registrado correctamente.")
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")

def registrar_salida():
    placa = entrada_placa_salida.get()

    if placa:
        ticket = db.obtener_ticket_por_placa(placa)
        if ticket:
            fecha_salida = datetime.now()
            tiempo_estacionado = (fecha_salida - ticket[1]).total_seconds() / 3600.0
            tarifa = float(db.obtener_tarifa_por_hora())  
            costo = tiempo_estacionado * tarifa
            db.registrar_salida(placa, fecha_salida, costo)
            nombre_cliente = ticket[2]  
            messagebox.showinfo("Éxito", f"Salida registrada correctamente.\nCliente: {nombre_cliente}\nCosto: ${costo:.2f}")
        else:
            messagebox.showwarning("Error", "No se encontró un ticket para esa placa.")
    else:
        messagebox.showwarning("Error", "Debe ingresar la placa del vehículo.")

def consultar_autos():
    autos = db.consultar_autos_en_estacionamiento()
    if autos:
        mensaje = "Autos en el estacionamiento:\n"
        for auto in autos:
            mensaje += f"Placa: {auto[0]}, Marca: {auto[1]}, Modelo: {auto[2]}\n"
        messagebox.showinfo("Consulta", mensaje)
    else:
        messagebox.showinfo("Consulta", "No hay autos en el estacionamiento.")
    mostrar_pantalla('menu')

def registrar_empleado():
    nombre = entrada_nombre_empleado.get()

    if nombre:
        empleado = Empleado(nombre)
        db.insertar_empleado(empleado)
        messagebox.showinfo("Éxito", "Empleado registrado correctamente.")
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")


ventana = tk.Tk()
ventana.title("Sistema de Estacionamiento")
ventana.configure(bg='#1E3D59')


estilo_label = {'bg': '#1E3D59', 'fg': '#F5F5F5', 'font': ('Arial', 12)}
estilo_entry = {'bg': '#4B77A1', 'fg': '#FFFFFF', 'font': ('Arial', 12)}
estilo_button = {'bg': '#1A5276', 'fg': '#FFFFFF', 'font': ('Arial', 12), 'activebackground': '#5499C7'}

entrada_placa = None
entrada_marca = None
entrada_modelo = None
entrada_puertas = None
cliente_nombre = None
cliente_telefono = None
entrada_placa_salida = None
entrada_nombre_empleado = None

def mostrar_pantalla(opcion):
    global entrada_placa, entrada_marca, entrada_modelo, entrada_puertas
    global cliente_nombre, cliente_telefono
    global entrada_placa_salida, entrada_nombre_empleado

    for widget in ventana.winfo_children():
        widget.grid_forget()

    if opcion == 'menu':
        tk.Button(ventana, text="Registrar Auto", command=lambda: mostrar_pantalla('auto'), **estilo_button).grid(row=0, column=0, padx=20, pady=10)
        tk.Button(ventana, text="Registrar Salida del Vehículo", command=lambda: mostrar_pantalla('salida'), **estilo_button).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(ventana, text="Registrar Empleado", command=lambda: mostrar_pantalla('empleado'), **estilo_button).grid(row=2, column=0, padx=20, pady=10)
        tk.Button(ventana, text="Consultar Autos en el Estacionamiento", command=lambda: mostrar_pantalla('consulta'), **estilo_button).grid(row=3, column=0, padx=20, pady=10)
        tk.Button(ventana, text="Salir", command=ventana.quit, **estilo_button).grid(row=4, column=0, padx=20, pady=10)
    
    elif opcion == 'auto':
        tk.Label(ventana, text="Registrar Auto", **estilo_label).grid(row=0, column=0, columnspan=2)
        tk.Label(ventana, text="Placa:", **estilo_label).grid(row=1, column=0)
        entrada_placa = tk.Entry(ventana, **estilo_entry)
        entrada_placa.grid(row=1, column=1)

        tk.Label(ventana, text="Marca:", **estilo_label).grid(row=2, column=0)
        entrada_marca = tk.Entry(ventana, **estilo_entry)
        entrada_marca.grid(row=2, column=1)

        tk.Label(ventana, text="Modelo:", **estilo_label).grid(row=3, column=0)
        entrada_modelo = tk.Entry(ventana, **estilo_entry)
        entrada_modelo.grid(row=3, column=1)

        tk.Label(ventana, text="Puertas:", **estilo_label).grid(row=4, column=0)
        entrada_puertas = tk.Entry(ventana, **estilo_entry)
        entrada_puertas.grid(row=4, column=1)

        tk.Label(ventana, text="Nombre Cliente:", **estilo_label).grid(row=5, column=0)
        cliente_nombre = tk.Entry(ventana, **estilo_entry)
        cliente_nombre.grid(row=5, column=1)

        tk.Label(ventana, text="Teléfono Cliente (opcional):", **estilo_label).grid(row=6, column=0)
        cliente_telefono = tk.Entry(ventana, **estilo_entry)
        cliente_telefono.grid(row=6, column=1)

        tk.Label(ventana, text="Nombre Empleado:", **estilo_label).grid(row=7, column=0)
        entrada_nombre_empleado = tk.Entry(ventana, **estilo_entry)
        entrada_nombre_empleado.grid(row=7, column=1)

        tk.Button(ventana, text="Registrar Auto", command=registrar_auto, **estilo_button).grid(row=8, column=0, columnspan=2)
        tk.Button(ventana, text="Volver al Menú", command=lambda: mostrar_pantalla('menu'), **estilo_button).grid(row=9, column=0, columnspan=2)
    
    elif opcion == 'salida':
        tk.Label(ventana, text="Registrar Salida del Vehículo", **estilo_label).grid(row=0, column=0, columnspan=2)
        tk.Label(ventana, text="Placa:", **estilo_label).grid(row=1, column=0)
        entrada_placa_salida = tk.Entry(ventana, **estilo_entry)
        entrada_placa_salida.grid(row=1, column=1)

        tk.Button(ventana, text="Registrar Salida", command=registrar_salida, **estilo_button).grid(row=2, column=0, columnspan=2)
        tk.Button(ventana, text="Volver al Menú", command=lambda: mostrar_pantalla('menu'), **estilo_button).grid(row=3, column=0, columnspan=2)

    elif opcion == 'empleado':
        tk.Label(ventana, text="Registrar Empleado", **estilo_label).grid(row=0, column=0, columnspan=2)
        tk.Label(ventana, text="Nombre:", **estilo_label).grid(row=1, column=0)
        entrada_nombre_empleado = tk.Entry(ventana, **estilo_entry)
        entrada_nombre_empleado.grid(row=1, column=1)

        tk.Button(ventana, text="Aceptar", command=registrar_empleado, **estilo_button).grid(row=2, column=0, columnspan=2)
        tk.Button(ventana, text="Volver al Menú", command=lambda: mostrar_pantalla('menu'), **estilo_button).grid(row=3, column=0, columnspan=2)

    elif opcion == 'consulta':
        consultar_autos()
        tk.Button(ventana, text="Volver al Menú", command=lambda: mostrar_pantalla('menu'), **estilo_button).grid(row=4, column=0, columnspan=2)


mostrar_pantalla('menu')


ventana.mainloop()
