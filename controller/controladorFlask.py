
#Importacion de Libs
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from sys import path
from os import path as osPath
from flask import jsonify
from json import loads

#Importacion de Capa de Servicio
path.insert(0,osPath.dirname(osPath.dirname(__file__)))
import service.clienteService as clienteService
import service.enviosService as EnviosService
import service.platosService as PlatosService
import service.preciosService as PreciosService
import service.ventaService as VentaService
import service.reservaService as ReservaService
import service.stockService as StockService



class AppFlask:
    '''
    Controlador Flask de enrutamiento:
    '''
    __private_app =  Flask(__name__)
    __private_cors = CORS(__private_app)
    __private_app.config['CORS_HEADERS'] = 'Content-Type'


    @__private_app.route('/cliente', methods=['GET','POST','DELETE','PUT'])
    def cliente():
        '''
            Metodo GET, requiere de variable idcliente y retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 499
            Metodo Post, agrega el JSON recibido en la DB a traves de clienteService
            Metodo PUT, modifica el cliente con ID = PARAMETRO ID
            Metodo DELETE, borra el registro de acuerdo al ID suministrado
        '''
        clienteS = clienteService.ClienteService()
        if request.method == 'GET':
            #127.0.0.1/cliente?idcliente=150
            idCliente = request.args.get('idcliente',default=None,type=int)
            if idCliente != None:
                return clienteS.getCliente([idCliente])
        elif request.method == 'POST':
            if request.is_json:
                if type(request.get_json()) == dict:
                    return clienteS.agregarCliente([request.get_json()])   
                else:
                    return clienteS.agregarCliente(request.get_json())
            else:
                return (jsonify({"statusCode": 499,"error": "No se recibio un Archivo JSON"})), 499
        elif request.method == 'DELETE':
            #127.0.0.1/cliente?borrarid=150
            idCliente = request.args.get('borrarid',default=None,type=int)
            return clienteS.deleteCliente(idCliente)
        elif request.method == 'PUT':
            #127.0.0.1/cliente?editarid=150
            idCliente = request.args.get('editarid',default=None,type=int)
            return clienteS.modificarByID(idCliente,request.get_json())

    @__private_app.route('/envios',methods=['GET','POST','DELETE','PUT'])
    def envios():
        '''
            Metodo GET, retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 499
            Metodo Post, agrega el JSON recibido en la DB a traves de servicio
            Metodo PUT, modifica el registro con ID = PARAMETRO ID
            Metodo DELETE, borra el registro de acuerdo al ID suministrado
        '''
        enviosS = EnviosService.EnviosService()
        if request.method == 'GET':
            #127.0.0.1/envios?idcliente=150
            idCliente = request.args.get('idcliente',default=None,type=int)
            return enviosS.getEnviosByIDCliente([idCliente])
        elif request.method == 'POST':
            if request.is_json:
                return enviosS.postEnvios(request.get_json())
            else: return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
        elif request.method == 'DELETE':
            #127.0.0.1/envios?borrarid=150
            idEnvio = request.args.get('borrarid',default=None,type=int)
            return enviosS.borrarEnvioByID(idEnvio)
        elif request.method == 'PUT':
            #127.0.0.1/envios?editarid=150
            idEnvio = request.args.get('editarid',default=None,type=int)
            return enviosS.editarEnvioByID(idEnvio,request.get_json())
        
    @__private_app.route('/platos',methods=['GET','POST','DELETE','PUT'])
    @cross_origin()
    def platos():
        '''
            Metodo GET, retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 499
            Metodo Post, agrega el JSON recibido en la DB a traves de servicio
            Metodo PUT, modifica el registro con ID = PARAMETRO ID
            Metodo DELETE, borra el registro de acuerdo al ID suministrado
        '''
        platosS = PlatosService.PlatosService()
        if request.method == 'GET':
            #127.0.0.1/platos?idplato=150
            idPlato = request.args.get('idplato',default=None,type=int)
            if idPlato != None:
                return platosS.getPlatoByID([idPlato])
            else:
              traerTodos = request.args.get('traertodos',default=None,type=int)
              if traerTodos == 1:
                  return platosS.listar()  
        elif request.method == 'POST':
            if request.is_json:
                platosS.agregoPlato(request.get_json())
            else:return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
        elif request.method == 'DELETE':
            #127.0.0.1/platos?borrarid=150
            idPlato = request.args.get('borrarid',default=None,type=int)
            return platosS.borrarPlatoById(idPlato)
        elif request.method == 'PUT':
            #127.0.0.1/platos?editarid=150
            idPlato = request.args.get('editarid',default=None,type=int)
            return platosS.modificarByID(idPlato,request.get_json())
            
    
    @__private_app.route('/precios',methods=['GET','POST','DELETE','PUT'])
    @cross_origin()
    def precios():
        '''
            Metodo GET, retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 499
            Metodo Post, agrega el JSON recibido en la DB a traves de servicio
            Metodo PUT, modifica el registro con ID = PARAMETRO ID
            Metodo DELETE, borra el registro de acuerdo al ID suministrado
        '''
        preciosS = PreciosService.PreciosService()
        if request.method == 'GET':
            #127.0.0.1/precios?idplato=150
            idPlato = request.args.get('idplato',default=None,type=int)
            if idPlato != None:
                return preciosS.getPrecioByIdPlato(idPlato)
            else:
              traerTodos = request.args.get('traertodos',default=None,type=int)
              if traerTodos == 1:
                  return preciosS.listar()
        elif request.method == 'POST':
            if request.is_json:
                preciosS.agregarPrecio(request.get_json())
            else:
                return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
        elif request.method == 'DELETE':
            #127.0.0.1/precios?borrarid=150
            idPrecio = request.args.get('borrarid',default=None,type=int)
            return preciosS.borrarPrecioByID(idPrecio)
        elif request.method == 'PUT':
            #127.0.0.1/precios?editarid=150
            idPrecio = request.args.get('editarid',default=None,type=int)
            return preciosS.editarPrecioByID(idPrecio,request.get_json())
    
    @__private_app.route('/ventas',methods=['GET','POST','DELETE','PUT'])
    def ventas():
        '''
            Metodo GET, retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 499
            Metodo Post, agrega el JSON recibido en la DB a traves de servicio
            Metodo PUT, modifica el registro con ID = PARAMETRO ID
            Metodo DELETE, borra el registro de acuerdo al ID suministrado
        '''
        ventaS = VentaService.VentaService()
        if request.method == 'GET':
            #127.0.0.1/ventas?idcliente=150
            idCliente = request.args.get('idcliente',default=None,type=int)
            return ventaS.getVentas(idCliente)
        elif request.method == 'POST':
            if request.is_json:
                ventaS.agregoVentas(request.get_json())
            else:
                return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
        elif request.method == 'DELETE':
            #127.0.0.1/vetans?borrarid=150
            idVenta = request.args.get('borrarid',default=None,type=int)
            return ventaS.borrarVentaByID(idVenta)
        elif request.method == 'PUT':
            #127.0.0.1/ventas?editarid=150
            idVenta = request.args.get('editarid',default=None,type=int)
            return ventaS.editarVentaByID(idVenta,request.get_json())


    @__private_app.route('/reservas',methods=['GET','POST','DELETE','PUT'])
    def reservas():
        '''
            Metodo GET, retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 499
            Metodo Post, agrega el JSON recibido en la DB a traves de servicio
            Metodo PUT, modifica el registro con ID = PARAMETRO ID
            Metodo DELETE, borra el registro de acuerdo al ID suministrado
        '''
        reservaS = ReservaService.ReservaService()
        if request.method == 'GET':
            #127.0.0.1/reservas?idcliente=150
            idCliente = request.args.get('idcliente',default=None,type=int)
            return reservaS.getReserva(idCliente)
        elif request.method == 'POST':
            if request.is_json:
                reservaS.agregarReserva(request.get_json())
            else:
                return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
        elif request.method == 'DELETE':
            #127.0.0.1/reservas?borrarid=150
            idReserva = request.args.get('borrarid',default=None,type=int)
            return reservaS.borrarReservaByID(idReserva)
        elif request.method == 'PUT':
            #127.0.0.1/reservas?editarid=150
            idReserva = request.args.get('editarid',default=None,type=int)
            return reservaS.editarReservaByID(idReserva,request.get_json())
        
    @__private_app.route('/stock',methods=['GET','POST','DELETE','PUT'])
    def stock():
        '''
            Metodo GET, retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 499
            Metodo Post, agrega el JSON recibido en la DB a traves de servicio
            Metodo PUT, modifica el registro con ID = PARAMETRO ID
            Metodo DELETE, borra el registro de acuerdo al ID suministrado
        '''
        stockS = StockService.StockService()
        if request.method == 'GET':
            #127.0.0.1/stock?idplato=150
            idPlato = request.args.get('idplato',default=None,type=int)
            return stockS.getStock(idPlato)
        elif request.method == 'POST':
            if request.is_json:
                stockS.agregarStock(request.get_json())
            else:
                return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
        elif request.method == 'DELETE':
            #127.0.0.1/stock?borrarid=150
            idStock = request.args.get('borrarid',default=None,type=int)
            return stockS.borrarStockByID(idStock)
        elif request.method == 'PUT':
            #127.0.0.1/stock?editarid=150
            idStock = request.args.get('editarid',default=None,type=int)
            return stockS.editarStockByID(idStock,request.get_json())

    @__private_app.route('/loguear',methods=['POST'])
    def login():  
        '''
            Metodo GET, retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 499
            Metodo Post, agrega el JSON recibido en la DB a traves de servicio
            Metodo PUT, modifica el registro con ID = PARAMETRO ID
            Metodo DELETE, borra el registro de acuerdo al ID suministrado
        '''  
        clienteS = clienteService.ClienteService()
        datos = request.get_json()
        return clienteS.validoLogin(datos["usuario"],datos["contrasena"])
        
        
    def run (self):
        '''
        Corro la App Flask
        '''
        self.__private_app.run()