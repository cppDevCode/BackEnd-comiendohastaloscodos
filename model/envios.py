import json

class Envios:
    __private_id = None
    __private_idVenta = None
    __private_idCliente = None
    __private_direccionEnvio = None
    __private_fechaEnvio = None

    @property
    def envio (self):
        return '{"id":' + self.__private_id + ',"idVenta":' + self.__private_idVenta + ',"idCliente":' + self.__private_idCliente
        + ',"direccionEnvio":"' +  self.__private_direccionEnvio + '","fechaEnvio":' + self.__private_fechaEnvio + '}'

    @envio.setter
    def envio (self, vEnvio):
        jsonEnvio = json.loads(vEnvio)
        self.__private_id = jsonEnvio["id"]
        self.__private_idVenta = jsonEnvio["idVenta"]
        self.__private_idCliente = jsonEnvio["idCliente"]
        self.__private_direccionEnvio = jsonEnvio["direccionEnvio"]
        self.__private_fechaEnvio = jsonEnvio["fechaEnvio"]