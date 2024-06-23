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
        print(id)
        return self.__private_servicio.borrarById("comiendohastaloscodos","USUARIO","CONTRASENA","tblClientes",[id]) 
    
    

