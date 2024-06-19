import mariadb
import sys

class baseDeDatos:
    __private_coneccion = None
    __private_cursor = None

    def __init__(self, usuario, contrasena, hostDb="127.0.0.1", puerto=3306):
        try:
            self.__private_coneccion = mariadb.connect(
                user = usuario,
                password = contrasena,
                host = hostDb,
                port=puerto
            )
            self.__private_cursor = self.__private_coneccion.cursor()
        except mariadb.Error as error:
            return f"Error al conectar a la base de datos: {error}"
            sys.exit(1)
    

    def creoBaseDeDatos(self,nombreBaseDatos):
        self.__private_cursor.execute("CREATE DATABASE IF NOT EXISTS " + nombreBaseDatos)

    def creoTablas (self,nombreBaseDatos):
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblClientes (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(80), apellido VARCHAR(50), email VARCHAR(120), telefono INT, direccion VARCHAR(50), piso INT, departamento VARCHAR(2), ciudad VARCHAR(40), provincia VARCHAR(50), pais VARCHAR(40),carnivoro BOOL, celiaco BOOL, vegano BOOL, vegetariano BOOL, contrasena VARCHAR(100))')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblReserva (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idCliente INT UNSIGNED, cantidadPersonas INT, fecha DATE, horario VARCHAR(20),CONSTRAINT `fk_idCliente` FOREIGN KEY (idCliente) REFERENCES tblClientes (id)	ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblPlatos (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(60), descripcion VARCHAR(255), imagen VARCHAR(255), tipo VARCHAR(40))')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblStock (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idPlato INT UNSIGNED, cantidad INT UNSIGNED, CONSTRAINT `fk_idPlato` FOREIGN KEY (idPlato) REFERENCES tblPlatos (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblPrecio (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idPlato INT UNSIGNED, precio DECIMAL, vigencia DATE,	CONSTRAINT `fk_idPlato2` FOREIGN KEY (idPlato) REFERENCES tblPlatos (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblVentas (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idCliente INT UNSIGNED, factura VARCHAR(12), fecha DATE, idPlato INT UNSIGNED,cantidad INT UNSIGNED, valorUnitario DECIMAL, CONSTRAINT `fk_idCliente2` FOREIGN KEY (idCliente) REFERENCES tblClientes (id) ON DELETE CASCADE ON UPDATE RESTRICT, CONSTRAINT `fk_idPlato3` FOREIGN KEY (idPlato) REFERENCES tblPlatos (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblEnvios (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idVentas INT UNSIGNED, idCliente INT UNSIGNED,direccionEnvio VARCHAR(150), fechaEnvio DATE, CONSTRAINT `fk_idCliente3` FOREIGN KEY (idCliente) REFERENCES tblClientes (id) ON DELETE CASCADE ON UPDATE RESTRICT, CONSTRAINT `fk_idVentas` FOREIGN KEY (idVentas) REFERENCES tblVentas (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
    
    def agregoRegistro(self, tabla, campos, valores):
        try:
            consulta ="INSERT INTO "+ tabla + " (" + campos + ") VALUES (" + valores + ")"
            self.__private_cursor.execute(consulta)
        except mariadb.Error as e: 
                print(f"Error: {e}")
        self.__private_coneccion.commit() 
        print(f"Last Inserted ID: {self.__private_cursor.lastrowid}")

    def cierroConeccion(self):
        self.__private_coneccion.close()