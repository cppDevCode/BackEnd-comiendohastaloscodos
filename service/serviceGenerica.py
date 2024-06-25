import repository.repositoryDB as rDB
from flask import jsonify
from json import loads
import datetime

class MetodosBD:
        
    def agregarItemsABD(self, baseDeDatos,tabla,campos,llaves,items):
        valores = []
        baseDatos = rDB.baseDeDatos()
        
        for variable in items:
            lista = ()
            for key in llaves:
                lista = lista +(variable[key],)
            valores.append(lista)
        baseDatos.agregoRegistros(tabla,campos,valores,len(llaves),baseDeDatos)    
        baseDatos.cierroConeccion()

    def getItemsBD(self,baseDeDatos,tabla,celdas,llaves,valorBuscado,columnaABuscar):
        baseDatos = rDB.baseDeDatos()
        resultado = baseDatos.getRegistroBy(tabla,celdas,valorBuscado,columnaABuscar,baseDeDatos)
        if resultado == []:
            baseDatos.cierroConeccion()
            return (jsonify({"statusCode": 499,"error": "No se encontraron resultados en la DB"})), 499
        else:
            jsonFinal = []
            for i in resultado:
                aux = "{"
                nro = 0
                for key in llaves:
                    try:
                        if isinstance(i[nro],datetime.date):
                            aux += '"'+ key +'": "' + str(i[nro])+ '",'
                        else:
                            aux += '"'+ key +'": "' + i[nro]+ '",'
                    except:
                        aux += '"'+ key +'": ' + str(i[nro])+ ','
                    nro += 1
                aux = aux[:-1]
                aux += "}"
                jsonFinal.append(loads(aux))
            
        baseDatos.cierroConeccion()
        return (jsonFinal), 200
    
    def borrarById(self,nomBaseDatos,tabla,id):
        baseDatos = rDB.baseDeDatos()
        resultado = baseDatos.borrarRegistroByID(tabla,id,nomBaseDatos)
        if resultado == "":
            baseDatos.cierroConeccion()
            return (jsonify({"statusCode": 200,"error": ""})), 200
        else:
            baseDatos.cierroConeccion()
            return (jsonify({"statusCode": 499,"error": str(resultado)})), 499
        
    def listar(self,nomBaseDatos,tabla,campos,llaves):
        baseDatos = rDB.baseDeDatos()
        resultado = baseDatos.listar(tabla,nomBaseDatos,campos)
        if resultado == "":
            baseDatos.cierroConeccion()
            return (jsonify({"statusCode": 499,"error": "Sin resultados"})), 499
        else:
            jsonFinal = []
            
            for i in resultado:
                aux = "{"
                nro = 0
                for key in llaves:
                    try:
                        if isinstance(i[nro],datetime.date):
                            aux += '"'+ key +'": "' + str(i[nro])+ '",'
                        else:
                            aux += '"'+ key +'": "' + i[nro]+ '",'
                    except:
                        aux += '"'+ key +'": ' + str(i[nro])+ ','
                    nro += 1
                aux = aux[:-1]
                aux += "}"
                jsonFinal.append(loads(aux))
            baseDatos.cierroConeccion()
            return (jsonFinal), 200
    
    def modificarByID(self,nombreBaseDatos,tabla, id, modificaciones):
        repositorio = rDB.baseDeDatos()
        resultado = repositorio.editarRegistroByID(nombreBaseDatos,tabla,modificaciones,[id])
        
        if resultado == None:
            repositorio.cierroConeccion()
            return (jsonify({"statusCode": 200,"error": ""})), 200
        else:
            repositorio.cierroConeccion()
            return (jsonify({"statusCode": 490,"error":resultado})), 490