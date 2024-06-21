import model.cliente as cliente
from flask import jsonify
from json import loads
import repository.repositoryDB as rDB

class ClienteService:
    def agregarCliente (self,cliente):
        clientesParsed = cliente
        valores = []
        baseDatos = rDB.baseDeDatos("USUARIO","CONTRASENA")
        for vcliente in clientesParsed:
            valores.append((vcliente["nombre"],vcliente["apellido"],vcliente["email"],vcliente["telefono"],vcliente["direccion"],
                       vcliente["piso"],vcliente["departamento"], vcliente["ciudad"],vcliente["provincia"],vcliente["pais"],
                       vcliente["carnivoro"],vcliente["celiaco"],vcliente["vegano"],vcliente["vegetariano"],vcliente["contrasena"]))
        
        baseDatos.agregoRegistros("tblClientes",
                                  "`nombre`,`apellido`,`email`,`telefono`,`direccion`,`piso`,`departamento`,`ciudad`,`provincia`,`pais`,`carnivoro`,`celiaco`,`vegano`,`vegetariano`,`contrasena`",
                                  valores,15,"comiendohastaloscodos")    
        
        baseDatos.cierroConeccion()

    def getCliente (self, id):
        baseDatos = rDB.baseDeDatos("USUARIO","CONTRASENA")
        resultado = baseDatos.getRegistroByID("tblClientes",id,"id","comiendohastaloscodos")
        if resultado == []:
            return (jsonify({"statusCode": 400,"error": "No se encontraron resultados en la DB"})), 400
        else:
            jsonFinal = "{"
            for i in resultado:
                jsonFinal += '"id": ' + str(i[0])+ ','
                jsonFinal += '"nombre": "' + i[1]+ '",'
                jsonFinal += '"apellido" :"' + i[2]+ '",'
                jsonFinal += '"email":"' + i[3]+ '",'
                jsonFinal += '"telefono":"' + i[4]+ '",'
                jsonFinal += '"direccion":"' + i[5]+ '",'
                jsonFinal += '"piso":' + str(i[6])+ ','
                jsonFinal += '"departamento":"' + i[7]+ '",'
                jsonFinal += '"ciudad":"' + i[8]+ '",'
                jsonFinal += '"provincia":"' + i[9]+ '",'
                jsonFinal += '"pais":"' + i[10]+ '",'
                jsonFinal += '"carnivoro":' + str(i[11])+ ","
                jsonFinal += '"celiaco":' + str(i[12])+ ","
                jsonFinal += '"vegano":' + str(i[13])+ ","
                jsonFinal += '"vegetariano":' + str(i[14])+ ","
                jsonFinal += '"contrasena":"' + i[15] + '"'
            jsonFinal += "}"
            print(jsonFinal)
            return (loads(jsonFinal)), 200
        baseDatos.cierroConeccion()
