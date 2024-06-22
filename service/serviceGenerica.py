import repository.repositoryDB as rDB
from flask import jsonify
from json import loads

class MetodosBD:
    def agregarItemsABD(self, baseDeDatos,usuario, contrasena,tabla,campos,llaves,items):
        valores = []
        baseDatos = rDB.baseDeDatos(usuario,contrasena)
        
        for variable in items:
            lista = ()
            for key in llaves:
                lista = lista +(variable[key],)
            valores.append(lista)
        baseDatos.agregoRegistros(tabla,campos,valores,len(llaves),baseDeDatos)    
        baseDatos.cierroConeccion()

    def getItemsBD(self,baseDeDatos,usuario, contrasena,tabla,llaves,valorBuscado):
        baseDatos = rDB.baseDeDatos(usuario,contrasena)
        resultado = baseDatos.getRegistroBy(tabla,valorBuscado,"id",baseDeDatos)
        if resultado == []:
            return (jsonify({"statusCode": 499,"error": "No se encontraron resultados en la DB"})), 499
        else:
            jsonFinal = "{"
            for i in resultado:
                nro = 0
                for key in llaves:
                    try:
                        jsonFinal += '"'+ key +'": "' + i[nro]+ '",'
                    except:
                        jsonFinal += '"'+ key +'": ' + str(i[nro])+ ','
                    nro += 1
        jsonFinal = jsonFinal[:-1]
        jsonFinal += "}"
        baseDatos.cierroConeccion()
        
        return (loads(jsonFinal)), 200