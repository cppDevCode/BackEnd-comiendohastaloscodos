import service.serviceGenerica as serviceGenerica

class VentaService:
    __private_servicio = serviceGenerica.MetodosBD()

    def agregoVentas(self,ventas):
        self.__private_servicio.agregarItemsABD("comiendohastaloscodos","USUARIO","CONTRASENA","tblVentas","`idCliente`,`factura`,`fecha`,`idPlato`,`cantidad`,`valorUnitario`",
                                                ["idCliente","factura","fecha","idPlato","cantidad","valorUnitario"],ventas)
    
    def getVentas(self,idCliente):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","USUARIO","CONTRASENA","tblVentas",["id","idCliente","factura","fecha","idPlato","cantidad","valorUnitario"],
                                           [idCliente],"idCliente")
    
    def borrarVentaByID(self,idVenta):
        return self.__private_servicio.borrarById("comiendohastaloscodos","USUARIO","CONTRASENA","tblVentas",[idVenta])