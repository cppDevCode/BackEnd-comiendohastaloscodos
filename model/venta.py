import json

class Venta:
    __private_id = None
    __private_idCliente = None
    __private_factura = None
    __private_fecha = None
    __private_idProducto = None
    __private_cantidad = None
    __private_valorUnitario = None

    @property
    def venta(self):
        return '{"id":' + self.__private_id + ',"idCliente":' + self.__private_idCliente + ',"factura":"' + self.__private_factura
        + '","fecha":' + self.__private_fecha + ',"idProducto":' + self.__private_idProducto + ',"cantidad:"' + self.__private_cantidad
        + ',"valorUnitario":', self.__private_valorUnitario + '}'

    @venta.setter
    def venta(self, vVenta):
        jsonVenta = json.loads(vVenta)
        self.__private_id = jsonVenta["id"]
        self.__private_idCliente = jsonVenta["idCliente"]
        self.__private_factura = jsonVenta["factura"]
        self.__private_fecha = jsonVenta["fecha"]
        self.__private_idProducto = jsonVenta["idProducto"]
        self.__private_cantidad = jsonVenta["cantidad"]
        self.__private_valorUnitario = jsonVenta["valorUnitario"]