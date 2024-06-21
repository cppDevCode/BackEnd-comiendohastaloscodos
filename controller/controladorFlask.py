from flask import Flask
from flask import request
from sys import path
from os import path as osPath
from flask import jsonify
path.insert(0,osPath.dirname(osPath.dirname(__file__)))
import service.clienteService as clienteService
from json import JSONEncoder as jsonE


class AppFlask:
    __private_app =  Flask(__name__)

    @__private_app.route('/cliente', methods=['GET','POST'])
    def getCliente():
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
            
        
    def run (self):
        self.__private_app.run()