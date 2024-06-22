from flask import Flask
from flask import request
from sys import path
from os import path as osPath
from flask import jsonify
path.insert(0,osPath.dirname(osPath.dirname(__file__)))
import service.clienteService as clienteService
import service.enviosService as EnviosService
import service.platosService as PlatosService
from json import JSONEncoder as jsonE



class AppFlask:
    __private_app =  Flask(__name__)

    @__private_app.route('/cliente', methods=['GET','POST'])
    def cliente():
        '''
            Metodo GET, requiere de variable idcliente y retorna el cliente con ese ID, en caso de ser correcto devuelve codigo 200, caso contrario 403
            Metodo Post, agrega el JSON recibido en la DB a traves de clienteService
        '''
        if request.method == 'GET':
            #127.0.0.1/cliente?idcliente=150
            clienteS = clienteService.ClienteService()
            idCliente = request.args.get('idcliente',default=None,type=int)
            return clienteS.getCliente([idCliente])
        elif request.method == 'POST':
            clienteS = clienteService.ClienteService()
            if request.is_json:
                clienteS.agregarCliente(request.get_json())
            else:
                return (jsonify({"statusCode": 490,"error": "No se recibio un Archivo JSON"})), 490
            return (jsonify({"statusCode": 201,"error": ""})), 201
        
    @__private_app.route('/envios',methods=['GET','POST'])
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
    
    #@__private_app.route('/precios',methods=['GET','POST'])
    #def precios():

        
    def run (self):
        self.__private_app.run()