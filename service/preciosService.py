import service.serviceGenerica as serviceGenerica

class PreciosService:
    __private_servicio = serviceGenerica.MetodosBD()

    def agregarPrecio (self, precios):
        self.__private_servicio.agregarItemsABD("comiendohastaloscodos","USUARIO","CONTRASENA","tblPrecio","`idPlato`,`precio`,`vigencia`",
                                                ["idPlato","precio","vigencia"],precios)
    
    def getPrecioByIdPlato (self,idPlato):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","USUARIO","CONTRASENA","tblPrecio",["id","idPlato","precio","vigencia"],[idPlato],"idPlato")
    
    def borrarPrecioByID (self,idPrecio):
        return self.__private_servicio.borrarById("comiendohastaloscodos","USUARIO","CONTRASENA","tblPrecio",[idPrecio])
    
    def listar(self):
        return self.__private_servicio.listar("comiendohastaloscodos","USUARIO","CONTRASENA","tblPrecio","`idPlato`,`precio`",["idPlato","precio"])
    
    def editarPrecioByID(self,id,datos):
        modificaciones = "idPlato=" + str(datos["idPlato"]) + ",precio=" + str(datos["precio"]) + ",vigencia='" + datos["vigencia"] + "'"
        return self.__private_servicio.modificarByID("comiendohastaloscodos","tblPrecio","USUARIO","CONTRASENA",id,modificaciones)