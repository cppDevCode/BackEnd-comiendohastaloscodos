import service.serviceGenerica as serviceGenerica

class PreciosService:
    __private_servicio = serviceGenerica.MetodosBD()

    def agregarPrecio (self, precios):
        self.__private_servicio.agregarItemsABD("comiendohastaloscodos","estilo3d","golpea1987","tblPrecio","`idPlato`,`precio`,`vigencia`",
                                                ["idPlato","precio","vigencia"],precios)
    
    def getPrecioByIdPlato (self,idPlato):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","USUARIO","CONTRASENA","tblPrecio",["id","idPlato","precio","vigencia"],[idPlato],"idPlato")
    
    def borrarPrecioByID (self,idPrecio):
        return self.__private_servicio.borrarById("comiendohastaloscodos","USUARIO","CONTRASENA","tblPrecio",[idPrecio])
    
    def listar(self):
        return self.__private_servicio.listar("comiendohastaloscodos","estilo3d","golpea1987","tblPrecio","`idPlato`,`precio`",["idPlato","precio"])