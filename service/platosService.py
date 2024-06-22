import service.serviceGenerica as serviceGenerica

class PlatosService:
    __private_servicio = serviceGenerica.MetodosBD()

    def agregoPlato (self,platos):
        self.__private_servicio.agregarItemsABD("comiendohastaloscodos","USUARIO","CONTRASENA","tblPlatos", "`nombre`,`descripcion`,`imagen`,`tipo`",
                                                ["nombre","descripcion","imagen","tipo"],platos)
 
    def getPlatoByID(self,idPlato):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","USUARIO","CONTRASENA","tblPlatos",
                                                  ["id","nombre","descripcion","imagen","tipo"],idPlato,"id")
    
    def borrarPlatoById(self,idPlato):
        return self.__private_servicio.borrarById("comiendohastaloscodos","USUARIO","CONTRASENA","tblPlatos",[idPlato])

