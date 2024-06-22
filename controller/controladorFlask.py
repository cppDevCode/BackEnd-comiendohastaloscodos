from flask import Flask
from flask import request
from sys import path
from os import path as osPath
from flask import jsonify
path.insert(0,osPath.dirname(osPath.dirname(__file__)))
import service.clienteService as clienteService
import service.enviosService as EnviosService
import service.platosService as PlatosService
import service.preciosService as PreciosService
import service.ventaService as VentaService
import service.reservaService as ReservaService
import service.stockService as StockService
from json import JSONEncoder as jsonE



class AppFlask:
    __private_app =  Flask(__name__)

    @__private_app.route('/cliente', methods=['GET','POST','DELETE'])
    def cliente():
        '''
            Metodo GET, requiere de variable idcliente y retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 403
            Metodo Post, agrega el JSON recibido en la DB a traves de clienteService
        '''
        clienteS = clienteService.ClienteService()
        if request.method == 'GET':
            #127.0.0.1/cliente?idcliente=150
            idCliente = request.args.get('idcliente',default=None,type=int)
            return clienteS.getCliente([idCliente])
        elif request.method == 'POST':
            if request.is_json:
                clienteS.agregarCliente(request.get_json())
            else:
                return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
        elif request.method == 'DELETE':
            #127.0.0.1/cliente?borrarid=150
            idCliente = request.args.get('borrarid',default=None,type=int)
            return clienteS.deleteCliente(idCliente)

    @__private_app.route('/envios',methods=['GET','POST','DELETE'])
    def envios():
        enviosS = EnviosService.EnviosService()
        if request.method == 'GET':
            #127.0.0.1/envios?idcliente=150
            idCliente = request.args.get('idcliente',default=None,type=int)
            return enviosS.getEnviosByIDCliente([idCliente])
        elif request.method == 'POST':
            if request.is_json:
                enviosS.postEnvios(request.get_json())
            else:return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
        elif request.method == 'DELETE':
            #127.0.0.1/envios?borrarid=150
            idEnvio = request.args.get('borrarid',default=None,type=int)
            return enviosS.borrarEnvioByID(idEnvio)
        
    @__private_app.route('/platos',methods=['GET','POST'])
    def platos():
        platosS = PlatosService.PlatosService()
        if request.method == 'GET':
            #127.0.0.1/envios?idplato=150
            idPlato = request.args.get('idplato',default=None,type=int)
            return platosS.getPlatoByID([idPlato])
        elif request.method == 'POST':
            if request.is_json:
                platosS.agregoPlato(request.get_json())
            else:return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
    
    @__private_app.route('/precios',methods=['GET','POST'])
    def precios():
        preciosS = PreciosService.PreciosService()
        if request.method == 'GET':
            #127.0.0.1/precios?idplato=150
            idPlato = request.args.get('idplato',default=None,type=int)
            return preciosS.getPrecioByIdPlato(idPlato)
        elif request.method == 'POST':
            if request.is_json:
                preciosS.agregarPrecio(request.get_json())
            else:
                return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
    
    @__private_app.route('/ventas',methods=['GET','POST','DELETE'])
    def ventas():
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


    @__private_app.route('/reservas',methods=['GET','POST'])
    def reservas():
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
        
    @__private_app.route('/stock',methods=['GET','POST'])
    def stock():
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
        
    def run (self):
        self.__private_app.run()