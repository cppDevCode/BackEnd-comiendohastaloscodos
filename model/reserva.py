import json

class Reserva:
    __private_idCliente = None
    __private_cantidadPersonas = None
    __private_fecha = None
    __private_horario = None

    @property
    def reserva (self):
        return '{ "idCliente":' + self.__private_idCliente + ',"cantidadPersonas":' + self.__private_cantidadPersonas 
        + ',"fecha":' + self.__private_fecha + ',"horario":"' + self.__private_horario + '"}'
    
    @reserva.setter
    def reserva (self, vReserva):
        jsonReserva = json.loads(vReserva)
        __private_idCliente = jsonReserva["idCliente"]
        __private_cantidadPersonas = jsonReserva["cantidadPersonas"]
        __private_fecha = jsonReserva["fecha"]
        __private_horario = jsonReserva["horario"]
    
    @property
    def cantidadPersonas (self):
        return self.__private_cantidadPersonas
    
    @cantidadPersonas.setter
    def cantidadPersonas (self,vCantidadPersonas):
        self.__private_cantidadPersonas = vCantidadPersonas

    @property
    def fecha (self):
        return self.__private_fecha
    
    @fecha.setter
    def fecha (self,fecha):
        self.__private_fecha = fecha
    
    @property
    def horario (self):
        return self.__private_horario
    
    @horario.setter
    def horario (self, horario):
        self.__private_horario = horario