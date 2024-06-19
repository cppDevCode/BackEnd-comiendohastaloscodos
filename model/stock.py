import json

class Stock:
    __private_id = None
    __private_idPlato = None
    __private_cantidad = None

    @property
    def stock (self):
        return '{"id":' + self.__private_id + ',"idPlato":' + self.__private_idPlato + ',"cantidad":' + self.__private_cantidad + '}'
    
    @stock.setter
    def stock (self, vStock):
        jsonStock = json.loads(vStock)
        self.__private_id = jsonStock["id"]
        self.__private_idPlato = jsonStock["idPlato"]
        self.__private_cantidad = jsonStock["cantidad"]