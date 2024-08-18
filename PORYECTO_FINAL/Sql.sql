
CREATE DATABASE IF NOT EXISTS parqueo_gui_nuevo_db;
USE parqueo_gui_nuevo_db;


CREATE TABLE IF NOT EXISTS empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS autos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(255) NOT NULL,
    marca VARCHAR(255) NOT NULL,
    modelo VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) DEFAULT 'Auto'
);


CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    telefono VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    auto_id INT NOT NULL,
    cliente_id INT NOT NULL,
    fecha_entrada DATETIME NOT NULL,
    fecha_salida DATETIME,
    costo DECIMAL(10, 2),
    FOREIGN KEY (auto_id) REFERENCES autos(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);


CREATE TABLE IF NOT EXISTS tarifas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    precio_por_hora DECIMAL(10, 2) NOT NULL
);


INSERT INTO tarifas (precio_por_hora) VALUES (10.00);
