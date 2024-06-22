import repository.repositoryDB as rDB
from flask import jsonify
from json import loads

class PreciosService:
    def agregarPrecio (self, precios):
        valores = []
        baseDatos = rDB.baseDeDatos("USUARIO","CONTRASENA")
        
        for vPlatos in platos:
            valores.append((vPlatos["nombre"],vPlatos["descripcion"],vPlatos["imagen"],vPlatos["tipo"]))
        
        baseDatos.agregoRegistros("tblPlatos",
                                  "`nombre`,`descripcion`,`imagen`,`tipo`",
                                  valores,4,"comiendohastaloscodos")    
        baseDatos.cierroConeccion()