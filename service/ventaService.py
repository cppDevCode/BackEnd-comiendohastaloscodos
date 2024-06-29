import service.serviceGenerica as serviceGenerica

class VentaService:
    __private_servicio = serviceGenerica.MetodosBD()

    def agregoVentas(self,ventas):
        if type(ventas) != list:
            ventas = [ventas]
        return self.__private_servicio.agregarItemsABD("comiendohastaloscodos","tblVentas","`idCliente`,`factura`,`fecha`,`idPlato`,`cantidad`,`valorUnitario`",
                                                ["idCliente","factura","fecha","idPlato","cantidad","valorUnitario"],ventas)
    
    def getVentas(self,idCliente):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","tblVentas",["id","idCliente","factura","fecha","idPlato","cantidad","valorUnitario"],
                                           [idCliente],"idCliente")
    
    def borrarVentaByID(self,idVenta):
        return self.__private_servicio.borrarById("comiendohastaloscodos","tblVentas",[idVenta])
    
    def editarVentaByID(self,id,datos):
        modificaciones = "idCliente=" + str(datos["idCliente"]) + ",factura='" + datos["factura"] + "',fecha='" + datos["fecha"] \
                        + "',idPlato=" + str(datos["idPlato"]) + ",cantidad=" + str(datos["cantidad"]) + ",valorUnitario=" + str(datos["valorUnitario"])
        return self.__private_servicio.modificarByID("comiendohastaloscodos","tblVentas",id,modificaciones)