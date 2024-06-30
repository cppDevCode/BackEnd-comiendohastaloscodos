#Importacion de libs
from flask import jsonify
from json import loads
from datetime import date
#Importacion de capa de coneccion a BBDD
import repository.repositoryDB as rDB


class MetodosBD:
    '''
    Clase que maneja los metodos comunes utilizados por toda la capa de servicios
    '''    
    def agregarItemsABD(self, baseDeDatos,tabla,campos,llaves,items):
        valores = []
        baseDatos = rDB.baseDeDatos() #Instancio la clase de la capa de coneccion a BBDD
        if type(items) == dict:
            lista = ()
            for key in llaves:
                lista = lista +(items[key],)
            valores.append(lista)
        else:
            for variable in items:
                lista = ()
                for key in llaves:
                    lista = lista +(variable[key],)
                valores.append(lista)
        return baseDatos.agregoRegistros(tabla,campos,valores,len(llaves),baseDeDatos)    

    def getUltimoID(self,db):
        baseDatos = rDB.baseDeDatos()
        ultimoID = baseDatos.getUltimoID(db)
        return jsonify({"ultimoID": ultimoID}),200

    def getItemsBD(self,baseDeDatos,tabla,celdas,llaves,valorBuscado,columnaABuscar):
        baseDatos = rDB.baseDeDatos() #Instancio la clase de la capa de coneccion a BBDD
        resultado = baseDatos.getRegistroBy(tabla,celdas,valorBuscado,columnaABuscar,baseDeDatos)
        if resultado == []:
            baseDatos.cierroConeccion()
            return (jsonify({"statusCode": 492,"error": "No se encontraron resultados en la DB"})), 492
        else:
            #Genero Str JSON para el envio
            jsonFinal = []
            for i in resultado:
                aux = "{"
                nro = 0
                for key in llaves:
                    try:
                        if isinstance(i[nro],date):
                            aux += '"'+ key +'": "' + str(i[nro])+ '",'
                        else:
                            aux += '"'+ key +'": "' + i[nro]+ '",'
                    except:
                        aux += '"'+ key +'": ' + str(i[nro])+ ','
                    nro += 1
                aux = aux[:-1]
                aux += "}"
                #Deserializo el str en un python Object
                jsonFinal.append(loads(aux))
        if len(jsonFinal) == 1:
            jsonFinal = jsonFinal[0]    
        baseDatos.cierroConeccion()
        return (jsonFinal), 200
    
    def borrarById(self,nomBaseDatos,tabla,id):
        baseDatos = rDB.baseDeDatos()
        resultado = baseDatos.borrarRegistroByID(tabla,id,nomBaseDatos)
        baseDatos.cierroConeccion()
        return resultado
        
        
    def listar(self,nomBaseDatos,tabla,campos,llaves):
        baseDatos = rDB.baseDeDatos()
        resultado = baseDatos.listar(tabla,nomBaseDatos,campos)
        if resultado == "":
            baseDatos.cierroConeccion()
            return resultado
        else:
            jsonFinal = []
            
            for i in resultado:
                aux = "{"
                nro = 0
                for key in llaves:
                    try:
                        if isinstance(i[nro],date):
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
        return repositorio.editarRegistroByID(nombreBaseDatos,tabla,modificaciones,[id])
        