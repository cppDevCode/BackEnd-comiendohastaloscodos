import service.serviceGenerica as serviceGenerica
from flask import jsonify

class ClienteService:
    __private_servicio = serviceGenerica.MetodosBD()

    def agregarCliente (self,cliente):
        self.__private_servicio.agregarItemsABD("comiendohastaloscodos","tblClientes",
                                                "`nombre`,`apellido`,`email`,`telefono`,`direccion`,`piso`,`departamento`,`ciudad`,`provincia`,`pais`,`carnivoro`,`celiaco`,`vegano`,`vegetariano`,`contrasena`",
                                                ["nombre","apellido","email","telefono","direccion","piso","departamento","ciudad","provincia",
                                                 "pais","carnivoro","celiaco","vegano","vegetariano","contrasena"],cliente)

    def getCliente (self, id):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","tblClientes","*",["id","nombre","apellido",
                                            "email","telefono","direccion","piso","departamento","ciudad","provincia","pais","carnivoro",
                                            "celiaco","vegano","vegetariano","contrasena"],id,"id")

    def validoLogin(self,email,contrasena):
        resultado=self.__private_servicio.getItemsBD("comiendohastaloscodos","tblClientes","`id`,`email`,`contrasena`,`nombre`",["id","email","contrasena","nombre"],[email],"email")
        if resultado[1] == 499:
            return (jsonify({"statusCode": 490,"error":"Usuario/Contraseña Erroneo"})), 490
        elif resultado[0][0]["contrasena"] == contrasena:
            return (jsonify({"statusCode": 200,"usuario":resultado[0][0]["nombre"],"id":resultado[0][0]["id"]})), 200
        else:
            return (jsonify({"statusCode": 490,"error":"Usuario/Contraseña Erroneo"})), 490


    def deleteCliente(self,id):
        return self.__private_servicio.borrarById("comiendohastaloscodos","tblClientes",[id]) 
    
    def modificarByID(self,id,datos):
        modificaciones = "nombre='" + datos["nombre"] + "',apellido='" \
        + datos["apellido"] + "',email='" + datos["email"] + "',telefono='" + datos["telefono"] + "',direccion='" \
        + datos["direccion"] + "',piso=" + str(datos["piso"]) +",departamento='" + datos["departamento"] + "',ciudad='" \
        + datos["ciudad"] + "',provincia='" + datos["provincia"] + "',pais='" + datos["pais"] + "',carnivoro=" \
        + str(datos["carnivoro"]) + ",celiaco=" + str(datos["celiaco"]) + ",vegano=" + str(datos["vegano"]) + ",vegetariano=" \
        + str(datos["vegetariano"]) + ",contrasena='" + datos["contrasena"] + "'"
        return self.__private_servicio.modificarByID("comiendohastaloscodos","tblClientes",id,modificaciones)
        

