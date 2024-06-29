import service.serviceGenerica as serviceGenerica

class StockService:
    __private_servicio = serviceGenerica.MetodosBD()

    def getStock (self,idPlato):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","tblStock",["id","idPlato","cantidad"],[idPlato],"idPlato")

    def agregarStock (self,stock):
        return self.__private_servicio.agregarItemsABD("comiendohastaloscodos","tblStock","`idPlato`,`cantidad`",
                                                ["idPlato","cantidad"],stock)
    
    def borrarStockByID(self,idStock):
        return self.__private_servicio.borrarById("comiendohastaloscodos","tblStock",[idStock])
    
    def editarStockByID(self,id,datos):
        modificaciones = "idPlato=" + str(datos["idPlato"]) + ", cantidad=" + str(datos["cantidad"])
        return self.__private_servicio.modificarByID("comiendohastaloscodos","tblStock",id,modificaciones)