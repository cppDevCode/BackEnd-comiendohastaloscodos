import mysql.connector as mysql
from sys import exit

class baseDeDatos:
    __private_coneccion = None
    __private_cursor = None

    def __init__(self, usuario, contrasena, hostDb="127.0.0.1"):
        try:
            self.__private_coneccion = mysql.connect(
                host = hostDb,
                user = usuario,
                password = contrasena
            )
            self.__private_cursor = self.__private_coneccion.cursor()
        except mysql.Error as error:
            print(f"Error al conectar a la base de datos: {error}")
            exit(1)
    

    def creoBaseDeDatos(self,nombreBaseDatos):
        self.__private_cursor.execute("CREATE DATABASE IF NOT EXISTS " + nombreBaseDatos)

    def creoTablas (self,nombreBaseDatos):
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblClientes (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(80), apellido VARCHAR(50), email VARCHAR(120), telefono VARCHAR(20), direccion VARCHAR(50), piso INT, departamento VARCHAR(2), ciudad VARCHAR(40), provincia VARCHAR(50), pais VARCHAR(40),carnivoro BOOL, celiaco BOOL, vegano BOOL, vegetariano BOOL, contrasena VARCHAR(100))')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblReserva (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idCliente INT UNSIGNED, cantidadPersonas INT, fecha DATE, horario VARCHAR(20),CONSTRAINT `fk_idCliente` FOREIGN KEY (idCliente) REFERENCES tblClientes (id)	ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblPlatos (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(60), descripcion VARCHAR(255), imgRuta VARCHAR(255), tipo VARCHAR(40))')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblStock (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idPlato INT UNSIGNED, cantidad INT UNSIGNED, CONSTRAINT `fk_idPlato` FOREIGN KEY (idPlato) REFERENCES tblPlatos (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblPrecio (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idPlato INT UNSIGNED, precio DECIMAL(15,2), vigencia DATE,	CONSTRAINT `fk_idPlato2` FOREIGN KEY (idPlato) REFERENCES tblPlatos (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblVentas (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idCliente INT UNSIGNED, factura VARCHAR(12), fecha DATE, idPlato INT UNSIGNED,cantidad INT UNSIGNED, valorUnitario DECIMAL(15,2), CONSTRAINT `fk_idCliente2` FOREIGN KEY (idCliente) REFERENCES tblClientes (id) ON DELETE CASCADE ON UPDATE RESTRICT, CONSTRAINT `fk_idPlato3` FOREIGN KEY (idPlato) REFERENCES tblPlatos (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblEnvios (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idVentas INT UNSIGNED, idCliente INT UNSIGNED,direccionEnvio VARCHAR(150), fechaEnvio DATE, CONSTRAINT `fk_idCliente3` FOREIGN KEY (idCliente) REFERENCES tblClientes (id) ON DELETE CASCADE ON UPDATE RESTRICT, CONSTRAINT `fk_idVentas` FOREIGN KEY (idVentas) REFERENCES tblVentas (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
    
    def agregoRegistros(self, tabla, campos, valores,cantValores,nombreBaseDatos):
        try:
            self.__private_cursor.execute("USE " + nombreBaseDatos)
            consulta ="INSERT INTO "+ tabla + " (" + campos + ") VALUES (" + ("%s, "*cantValores)[:-2] + ")"
            self.__private_cursor.executemany(consulta,valores)
        except mysql.Error as e: 
                print(f"Error: {e}")
        self.__private_coneccion.commit() 
        print(f"Registros Agregados: {self.__private_cursor.rowcount}")

    def getRegistroBy(self, tabla, nroID,columna,nombreBaseDatos):
        self.__private_cursor.execute("USE " + nombreBaseDatos)
        consulta = "SELECT * FROM " + tabla + " WHERE " + columna +"=%s"
        self.__private_cursor.execute(consulta, nroID)
        return self.__private_cursor.fetchall()
    
    def editarRegistroByID(self,nombreBaseDatos, tabla, modificaciones, id):
        self.__private_cursor.execute("USE " + nombreBaseDatos)
        consulta = "UPDATE " + tabla + " SET " + modificaciones + " WHERE id=%s"
        try:
            self.__private_cursor.execute(consulta,id)
            self.__private_coneccion.commit()
        except mysql.Error as e:
            print(e)
            return e
    
    def borrarRegistroByID(self,tabla,nroID,nombreBaseDatos):
        self.__private_cursor.execute("USE " + nombreBaseDatos)
        consulta = "DELETE FROM " + tabla + " WHERE id=%s"
        try:
            self.__private_cursor.execute(consulta,nroID)
            self.__private_coneccion.commit()
            if self.__private_cursor.rowcount == 0:
                return "No se ha encontrado registro con ID=" + str(nroID[0])
            else:
                return ""
        except mysql.Error as e:
            print(e)
            return e
        
    def listar(self,tabla,nombreBaseDatos,campos):
        self.__private_cursor.execute("USE " + nombreBaseDatos)
        consulta = "SELECT " + campos + " FROM " + tabla
        try:
            self.__private_cursor.execute(consulta)
            return self.__private_cursor.fetchall()
        except mysql.Error as e:
            return e
    
    def cierroConeccion(self):
        self.__private_coneccion.close()