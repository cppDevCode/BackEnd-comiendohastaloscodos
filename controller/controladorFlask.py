import json.tool
from flask import Flask
from flask import request
import sys
import os
from flask import jsonify
sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
import model.cliente as cliente
app = Flask(__name__)

@app.route('/cliente', methods=['GET','POST'])
def getCliente():
    if request.method == 'GET':
        #127.0.0.1/cliente?idcliente=150
        idCliente = request.args.get('idcliente',default=None,type=int)
        return str(idCliente)
    elif request.method == 'POST':
        return "hola"
    '''vCliente = cliente.Cliente
    vCliente.cliente = {"id":1,"nombre":"alejandro","apellido":"baldres","email":"ejemplo@dos.com","telefono":2914754789,"direccion":"Haitiano 124","piso":2,"departamento":"G","ciudad":"9 de Julio","provincia":"Buenos Aires","pais":"Argentina","carnivoro":True,"celiaco":False,"vegano":False,"vegetariano":False}
    return jsonify(vCliente.cliente)'''
