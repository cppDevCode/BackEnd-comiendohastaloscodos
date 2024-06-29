import service.serviceGenerica as serviceGenerica

class EnviosService:
    __private_servicio = serviceGenerica.MetodosBD()

    def getEnviosByIDCliente (self, idcliente):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","tblEnvios",["id","idVentas","idCliente","direccionEnvio","fechaEnvio"],
                                           idcliente,"idCliente")
    
    def postEnvios (self, envios):
        return self.__private_servicio.agregarItemsABD("comiendohastaloscodos","tblEnvios","`idVentas`,`idCliente`,`direccionEnvio`,`fechaEnvio`",
                                                ["idVentas","idCliente","direccionEnvio","fechaEnvio"],envios)
    def borrarEnvioByID(self, idEnvio):
        return self.__private_servicio.borrarById("comiendohastaloscodos","tblEnvios",[idEnvio])
    
    def editarEnvioByID(self,idEnvio,datos):
        modificaciones = "idCliente=" + str(datos["idCliente"]) + ",direccionEnvio='" + datos["direccionEnvio"] + "',fechaEnvio='" \
                        + datos["fechaEnvio"] + "'"
        return self.__private_servicio.modificarByID("comiendohastaloscodos","tblEnvios",idEnvio,modificaciones)