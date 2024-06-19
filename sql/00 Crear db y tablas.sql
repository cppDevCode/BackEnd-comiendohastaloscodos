CREATE DATABASE IF NOT EXISTS comiendohastaloscodos;

USE  comiendohastaloscodos;

CREATE TABLE IF NOT EXISTS comiendohastaloscodos.tblClientes (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(80), apellido VARCHAR(50), email VARCHAR(120), telefono INT, direccion VARCHAR(50),
										piso INT, departamento VARCHAR(2), ciudad VARCHAR(40), provincia VARCHAR(50), pais VARCHAR(40),carnivoro BOOL, celiaco BOOL, vegano BOOL, 
										vegetariano BOOL, contrasena VARCHAR(100));
CREATE TABLE IF NOT EXISTS comiendohastaloscodos.tblReserva (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idCliente INT UNSIGNED, cantidadPersonas INT, fecha DATE, horario VARCHAR(20),
										CONSTRAINT `fk_idCliente`
											FOREIGN KEY (idCliente) REFERENCES tblClientes (id)
											ON DELETE CASCADE
											ON UPDATE RESTRICT);
CREATE TABLE IF NOT EXISTS comiendohastaloscodos.tblPlatos (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(60), descripcion VARCHAR(255), imagen VARCHAR(255), tipo VARCHAR(40));
CREATE TABLE IF NOT EXISTS comiendohastaloscodos.tblStock (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idPlato INT UNSIGNED, cantidad INT UNSIGNED,
										CONSTRAINT `fk_idPlato`
											FOREIGN KEY (idPlato) REFERENCES tblPlatos (id)
											ON DELETE CASCADE
											ON UPDATE RESTRICT);
CREATE TABLE IF NOT EXISTS comiendohastaloscodos.tblPrecio (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idPlato INT UNSIGNED, precio DECIMAL, vigencia DATE,
										CONSTRAINT `fk_idPlato2`
											FOREIGN KEY (idPlato) REFERENCES tblPlatos (id)
											ON DELETE CASCADE
											ON UPDATE RESTRICT);
CREATE TABLE IF NOT EXISTS comiendohastaloscodos.tblVentas (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idCliente INT UNSIGNED, factura VARCHAR(12), fecha DATE, idPlato INT UNSIGNED,cantidad INT UNSIGNED,
										valorUnitario DECIMAL,
										CONSTRAINT `fk_idCliente2`
											FOREIGN KEY (idCliente) REFERENCES tblClientes (id)
											ON DELETE CASCADE
											ON UPDATE RESTRICT,
										CONSTRAINT `fk_idPlato3`
											FOREIGN KEY (idPlato) REFERENCES tblPlatos (id)
											ON DELETE CASCADE
											ON UPDATE RESTRICT);
CREATE TABLE IF NOT EXISTS comiendohastaloscodos.tblEnvios (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idVentas INT UNSIGNED, idCliente INT UNSIGNED,direccionEnvio VARCHAR(150), fechaEnvio DATE,
										CONSTRAINT `fk_idCliente3`
											FOREIGN KEY (idCliente) REFERENCES tblClientes (id)
											ON DELETE CASCADE
											ON UPDATE RESTRICT,
										CONSTRAINT `fk_idVentas`
											FOREIGN KEY (idVentas) REFERENCES tblVentas (id)
											ON DELETE CASCADE
											ON UPDATE RESTRICT);