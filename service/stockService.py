import service.serviceGenerica as serviceGenerica

class StockService:
    __private_servicio = serviceGenerica.MetodosBD()

    def getStock (self,idPlato):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","USUARIO","CONTRASENA","tblStock",["id","idPlato","cantidad"],[idPlato],"idPlato")

    def agregarStock (self,stock):
        self.__private_servicio.agregarItemsABD("comiendohastaloscodos","USUARIO","CONTRASENA","tblStock","`idPlato`,`cantidad`",
                                                ["idPlato","cantidad"],stock)