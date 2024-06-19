import json

class PrecioPlato:
    __private_id = None
    __private_idPlato = None
    __private_precio = None
    __private_vigencia = None

    @property
    def precio (self):
        return '{"id":' + self.__private_id + ',"idPlato":' + self.__private_idPlato + ',"precio":' + self.__private_precio + ',"vigencia":' 
        + self.__private_vigencia + '}'
    
    @precio.setter
    def precio (self, vPrecio):
        jsonPrecio = json.loads(vPrecio)
        self.__private_id = jsonPrecio["id"]
        self.__private_idPlato = jsonPrecio["idPlato"]
        self.__private_precio = jsonPrecio["precio"]
        self.__private_vigencia = jsonPrecio["vigencia"]