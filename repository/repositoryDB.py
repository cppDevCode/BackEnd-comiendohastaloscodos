import mysql.connector as mysql
from sys import exit
from flask import jsonify
from json import load

class baseDeDatos:
    '''
    Clase de capa de Coneccion a BBDD
    '''
    __private_coneccion = None
    __private_cursor = None
    __private_datosConeccion = None


    def __init__(self, hostDb="127.0.0.1"):
        '''
        Inicializa y conecta al hostDb usando el usuario y contraseña almacenado en el 
        archivo setting.json
        '''
        try:
            with open("./setting.json",'r') as archivo:
                self.__private_datosConeccion = load(archivo)
            self.__private_coneccion = mysql.connect(
                host = hostDb,
                user = self.__private_datosConeccion["usuario"],
                password = self.__private_datosConeccion["contrasena"]
            )
            self.__private_cursor = self.__private_coneccion.cursor()
        except mysql.Error as error:
            print(f"Error al conectar a la base de datos: {error}")
            exit(1)
    

    def creoBaseDeDatos(self,nombreBaseDatos):
        self.__private_cursor.execute("CREATE DATABASE IF NOT EXISTS " + nombreBaseDatos)

    def creoTablas (self,nombreBaseDatos):
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblClientes (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(80) NOT NULL, apellido VARCHAR(50) NOT NULL, email VARCHAR(120) NOT NULL UNIQUE, telefono VARCHAR(20), direccion VARCHAR(50) NOT NULL, piso INT, departamento VARCHAR(2), ciudad VARCHAR(40) NOT NULL, provincia VARCHAR(50) NOT NULL, pais VARCHAR(40) NOT NULL,carnivoro BOOL, celiaco BOOL, vegano BOOL, vegetariano BOOL, contrasena VARCHAR(100) NOT NULL)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblReserva (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idCliente INT UNSIGNED NOT NULL, cantidadPersonas INT NOT NULL, fecha DATE NOT NULL, horario VARCHAR(20) NOT NULL,CONSTRAINT `fk_idCliente` FOREIGN KEY (idCliente) REFERENCES tblClientes (id)	ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblPlatos (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(60) NOT NULL, descripcion VARCHAR(255) NOT NULL, imgRuta VARCHAR(255) NOT NULL, tipo VARCHAR(40) NOT NULL)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblStock (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idPlato INT UNSIGNED NOT NULL, cantidad INT UNSIGNED NOT NULL, CONSTRAINT `fk_idPlato` FOREIGN KEY (idPlato) REFERENCES tblPlatos (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblPrecio (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idPlato INT UNSIGNED NOT NULL, precio DECIMAL(15,2) NOT NULL, vigencia DATE NOT NULL,	CONSTRAINT `fk_idPlato2` FOREIGN KEY (idPlato) REFERENCES tblPlatos (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblVentas (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idCliente INT UNSIGNED NOT NULL, factura VARCHAR(12) NOT NULL, fecha DATE NOT NULL, idPlato INT UNSIGNED NOT NULL,cantidad INT UNSIGNED NOT NULL, valorUnitario DECIMAL(15,2) NOT NULL, CONSTRAINT `fk_idCliente2` FOREIGN KEY (idCliente) REFERENCES tblClientes (id) ON DELETE CASCADE ON UPDATE RESTRICT, CONSTRAINT `fk_idPlato3` FOREIGN KEY (idPlato) REFERENCES tblPlatos (id) ON DELETE CASCADE ON UPDATE RESTRICT)')
        self.__private_cursor.execute('CREATE TABLE IF NOT EXISTS ' + nombreBaseDatos + '.tblEnvios (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, idVentas INT UNSIGNED NOT NULL, idCliente INT UNSIGNED NOT NULL,direccionEnvio VARCHAR(150) NOT NULL, fechaEnvio DATE NOT NULL, CONSTRAINT `fk_idCliente3` FOREIGN KEY (idCliente) REFERENCES tblClientes (id) ON DELETE CASCADE ON UPDATE RESTRICT, CONSTRAINT `fk_idVentas` FOREIGN KEY (idVentas) REFERENCES tblVentas (id) ON DELETE CASCADE ON UPDATE RESTRICT)')

    def getCantidadRegistrosTabla (self, nombreBaseDatos,nombreTabla):
            self.__private_cursor.execute("USE " + nombreBaseDatos)
            consulta = f'SELECT COUNT(*) FROM {nombreTabla}'
            self.__private_cursor.execute(consulta)
            return self.__private_cursor.fetchall()[0][0]
            
    
    def agregoRegistros(self, tabla, campos, valores,cantValores,nombreBaseDatos,prueba=False):
        try:
            self.__private_cursor.execute("USE " + nombreBaseDatos)
            consulta ="INSERT INTO "+ tabla + " (" + campos + ") VALUES (" + ("%s, "*cantValores)[:-2] + ")"
            self.__private_cursor.executemany(consulta,valores)
            self.__private_coneccion.commit() 
            if not prueba:
                return jsonify({"statusCode":201,"error":""}), 201
            print(f"Registros Agregados: {self.__private_cursor.rowcount}")
        except mysql.Error as e: 
                #Error Code 1062 = Mail duplicado
                if e.errno == 1062:
                    self.cierroConeccion()
                    return jsonify({"statusCode":491,"error":"Usuario ya existente (1062)"}), 491
                else:
                    self.cierroConeccion()
                    try:
                        return jsonify({"statusCode":492,"error": f"{e.msg} ( {e.errno}) "}), 492
                    except:
                        print(e)
                        return jsonify({"statusCode":491,"error": "Error en sintaxis de BBDD"}), 491

        

    def getRegistroBy(self, tabla,celdas, nroID,columna,nombreBaseDatos):
        self.__private_cursor.execute("USE " + nombreBaseDatos)
        consulta = "SELECT "+ celdas +" FROM " + tabla + " WHERE " + columna +"=%s"
        self.__private_cursor.execute(consulta,nroID)
        return self.__private_cursor.fetchall()
    
    def editarRegistroByID(self,nombreBaseDatos, tabla, modificaciones, id):
        self.__private_cursor.execute("USE " + nombreBaseDatos)
        consulta = "UPDATE " + tabla + " SET " + modificaciones + " WHERE id=%s"
        try:
            self.__private_cursor.execute(consulta,id)
            self.__private_coneccion.commit()
            self.cierroConeccion()
            return jsonify({"statusCode":201,"error":""}), 201
        except mysql.Error as e:
            print(e)
            return jsonify({"statusCode":492,"error":e.msg + "(" + e.errno +")"}), 492
    
    def borrarRegistroByID(self,tabla,nroID,nombreBaseDatos):
        self.__private_cursor.execute("USE " + nombreBaseDatos)
        consulta = "DELETE FROM " + tabla + " WHERE id=%s"
        try:
            self.__private_cursor.execute(consulta,nroID)
            self.__private_coneccion.commit()
            if self.__private_cursor.rowcount == 0:
                return jsonify({"statusCode": 493,"error":"No se ha encontrado registro con ID=" + str(nroID[0])}), 493
            else:
                return jsonify({"statusCode": 200,"error":""}), 200
        except mysql.Error as e:
            print(e)
            return jsonify({"statusCode":492,"error":e.msg + "(" + e.errno +")"}), 492
        
    def listar(self,tabla,nombreBaseDatos,campos):
        self.__private_cursor.execute("USE " + nombreBaseDatos)
        consulta = "SELECT " + campos + " FROM " + tabla
        try:
            self.__private_cursor.execute(consulta)
            return self.__private_cursor.fetchall()
        except mysql.Error as e:
            return jsonify({"statusCode":492,"error":e.msg + "(" + e.errno +")"}), 492
    
    def cierroConeccion(self):
        self.__private_coneccion.close()