import json

class Platos:
    __private_id = None
    __private_nombre = None
    __private_descripcion = None
    __private_imagen = None
    __private_tipo = None

    @property
    def plato (self):
        return '{"id":' + self.__private_id + ',"nombre":"' + self.__private_nombre + '","descripcion":"' 
        + self.__private_descripcion + '","imagen":"' + self.__private_imagen + '","tipo":"' + self.__private_tipo + '"}' 
    
    @plato.setter
    def plato (self, vPlato):
        jsonPlato = json.loads(vPlato)
        self.__private_id = jsonPlato["id"]
        self.__private_nombre = jsonPlato["nombre"]
        self.__private_descripcion = jsonPlato["descripcion"]
        self.__private_imagen = jsonPlato["imagen"]
        self.__private_tipo = jsonPlato["tipo"]

    