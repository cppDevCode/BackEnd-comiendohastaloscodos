import repository.repositoryDB as rDB
from flask import jsonify
from json import loads

class EnviosService:

    def getEnviosByIDCliente (self, idcliente):
        baseDatos = rDB.baseDeDatos("estilo3d","golpea1987")    
        resultado = baseDatos.getRegistroBy("tblEnvios",idcliente,"idCliente","comiendohastaloscodos")
        if resultado == []:
            return (jsonify({"statusCode": 499,"error": "No se encontraron resultados en la DB"})), 499
        else:
            for i in resultado:
                jsonFinal = "{"
                jsonFinal += '"id":' + i[0] + ','
                jsonFinal += '"idVentas":' + i[1] + ','
                jsonFinal += '"direccionEnvio":"' + i[3] +'",'
                jsonFinal += '"fechaEnvio:' + i[4]
                jsonFinal = "},"
            jsonFinal = jsonFinal[:-1]
        baseDatos.cierroConeccion()
        return (loads(jsonFinal)), 200
    
    def postEnvios (self, envios):
        baseDatos = rDB.baseDeDatos("estilo3d","golpea1987")
        valores = []
        for vEnvio in envios:
            valores.append((vEnvio["idVentas"],vEnvio["idCliente"],vEnvio["direccionEnvio"],vEnvio["fechaEnvio"]))
        baseDatos.agregoRegistros("tblEnvios","`idVentas`,`idCliente`,`direccionEnvio`,`fechaEnvio`",valores,4,"comiendohastaloscodos")
        baseDatos.cierroConeccion()
        