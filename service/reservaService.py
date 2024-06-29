import service.serviceGenerica as serviceGenerica

class ReservaService:
    __private_servicio = serviceGenerica.MetodosBD()

    def getReserva(self,idCliente):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","tblReserva",
                                                  ["id","idCliente","cantidadPersonas","fecha","horario"], [idCliente],"idCliente")
    
    def agregarReserva(self,reservas):
        return self.__private_servicio.agregarItemsABD("comiendohastaloscodos","tblReserva","`idCliente`,`cantidadPersonas`,`fecha`,`horario`",
                                                ["idCliente","cantidadPersonas","fecha","horario"],reservas)
        
    def borrarReservaByID(self,idReserva):
        return self.__private_servicio.borrarById("comiendohastaloscodos","tblReserva",[idReserva])
    
    def editarReservaByID(self,id,datos):
        modificaciones = "idCliente=" + str(datos["idCliente"]) + ",cantidadPersonas=" + str(datos["cantidadPersonas"]) \
                        + ",fecha='" + datos["fecha"] + "',horario='" + datos["horario"] + "'"
        return self.__private_servicio.modificarByID("comiendohastaloscodos","tblReserva",id,modificaciones)