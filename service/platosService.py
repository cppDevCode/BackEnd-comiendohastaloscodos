import service.serviceGenerica as serviceGenerica
import repository.repositoryDB as repositoryDB
from flask import jsonify
from json import loads

class PlatosService:
    __private_servicio = serviceGenerica.MetodosBD()

    def agregoPlato (self,platos):
        self.__private_servicio.agregarItemsABD("comiendohastaloscodos","tblPlatos", "`nombre`,`descripcion`,`imgRuta`,`tipo`",
                                                ["nombre","descripcion","imgRuta","tipo"],platos)
 
    def getPlatoByID(self,idPlato):
        return self.__private_servicio.getItemsBD("comiendohastaloscodos","tblPlatos",
                                                  ["id","nombre","descripcion","imgRuta","tipo"],idPlato,"id")
    
    def borrarPlatoById(self,idPlato):
        return self.__private_servicio.borrarById("comiendohastaloscodos","tblPlatos",[idPlato])
    
    def listar(self):
        return self.__private_servicio.listar("comiendohastaloscodos","tblPlatos","`id`,`nombre`, `descripcion`, `imgRuta`,`tipo`",
                                              ["id","nombre","descripcion","imgRuta","tipo"])

    def modificarByID(self, id, datos):
        modificaciones = "nombre='" + datos["nombre"] + "',descripcion='" + datos["descripcion"] + "',imgRuta='" + datos["imgRuta"] + "',tipo='" + datos["tipo"]+"'"
        return self.__private_servicio.modificarByID("comiendohastaloscodos","tblPlatos",id,modificaciones)
        