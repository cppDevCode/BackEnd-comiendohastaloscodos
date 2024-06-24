import service.serviceGenerica as serviceGenerica

class ClienteService:
    __private_servicio = serviceGenerica.MetodosBD()

    def agregarCliente (self,cliente):
        self.__private_servicio.agregarItemsABD("comiendohastaloscodos","USUARIO","CONTRASENA","tblClientes",
                                                "`nombre`,`apellido`,`email`,`telefono`,`direccion`,`piso`,`departamento`,`ciudad`,`provincia`,`pais`,`carnivoro`,`celiaco`,`vegano`,`vegetariano`,`contrasena`",
                                                ["nombre","apellido","email","telefono","direccion","piso","departamento","ciudad","provincia",
                                                 "pais","carnivoro","celiaco","vegano","vegetariano","contrasena"],cliente)

    def getCliente (self, id):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","USUARIO","CONTRASENA","tblClientes",["id","nombre","apellido",
                                            "email","telefono","direccion","piso","departamento","ciudad","provincia","pais","carnivoro",
                                            "celiaco","vegano","vegetariano","contrasena"],id,"id")

    def deleteCliente(self,id):
        return self.__private_servicio.borrarById("comiendohastaloscodos","USUARIO","CONTRASENA","tblClientes",[id]) 
    
    def modificarByID(self,id,datos):
        modificaciones = "nombre='" + datos["nombre"] + "',apellido='" \
        + datos["apellido"] + "',email='" + datos["email"] + "',telefono='" + datos["telefono"] + "',direccion='" \
        + datos["direccion"] + "',piso=" + str(datos["piso"]) +",departamento='" + datos["departamento"] + "',ciudad='" \
        + datos["ciudad"] + "',provincia='" + datos["provincia"] + "',pais='" + datos["pais"] + "',carnivoro=" \
        + str(datos["carnivoro"]) + ",celiaco=" + str(datos["celiaco"]) + ",vegano=" + str(datos["vegano"]) + ",vegetariano=" \
        + str(datos["vegetariano"]) + ",contrasena='" + datos["contrasena"] + "'"
        return self.__private_servicio.modificarByID("comiendohastaloscodos","tblClientes","USUARIO","CONTRASENA",id,modificaciones)
        

