import repository.repositoryDB as rDB
from flask import jsonify
from json import loads

class PlatosService:
    def agregoPlato (self,platos):
        valores = []
        baseDatos = rDB.baseDeDatos("estilo3d","golpea1987")
        
        for vPlatos in platos:
            valores.append((vPlatos["nombre"],vPlatos["descripcion"],vPlatos["imagen"],vPlatos["tipo"]))
        
        baseDatos.agregoRegistros("tblPlatos",
                                  "`nombre`,`descripcion`,`imagen`,`tipo`",
                                  valores,4,"comiendohastaloscodos")    
        baseDatos.cierroConeccion()
    
    def getPlatoByID(self,idPlato):
        baseDatos = rDB.baseDeDatos("estilo3d","golpea1987")
        resultado = baseDatos.getRegistroBy("tblPlatos",idPlato,"id","comiendohastaloscodos")
        if resultado == []:
            return (jsonify({"statusCode": 499,"error": "No se encontraron resultados en la DB"})), 499
        else:
            jsonFinal = "{"
            for i in resultado:
                jsonFinal += '"id": ' + str(i[0])+ ','
                jsonFinal += '"nombre": "' + i[1]+ '",'
                jsonFinal += '"descripcion":"' + i[2]+ '",'
                jsonFinal += '"imagen":"' + i[3]+ '",'
                jsonFinal += '"tipo":"' + i[4]+ '"'
        jsonFinal += "}"
        baseDatos.cierroConeccion()
        return (loads(jsonFinal)), 200
