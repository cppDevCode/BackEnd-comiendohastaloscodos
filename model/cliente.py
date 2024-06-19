import json
import model.reserva as mReserva

class Cliente:
    __private_id = None
    __private_nombre = None
    __private_apellido = None
    __private_email = None
    __private_telefono = None
    __private_direccion = None
    __private_piso = None
    __private_dpto = None
    __private_ciudad = None
    __private_provincia = None
    __private_pais = None
    __private_carnivoro = None
    __private_celiaco = None
    __private_vegano = None
    __private_vegetariano = None
    __private_reserva = None

    def __init__ (self):
        self.__private_reserva = mReserva() 


    @property
    def cliente (self):
        return '{ "id":' + self.__private_id + ',"nombre":"' + self.__private_nombre +'","apellido":"' + self.__private_apellido + '",'  
        + '"email":"' + self.__private_email + '","telefono":' + self.__private_telefono + ',"direccion":"'
        + self.__private_direccion + '","piso":' + self.__private_piso + ',"departamento":"' + self.__private_dpto + '","ciudad":"' 
        + self.__private_ciudad + '","provincia":"' + self.__private_provincia + '","pais":"' + self.__private_pais + '","carnivoro":' 
        + self.__private_carnivoro + ',"celiaco":' + self.__private_celiaco + ',"vegano":' + self.__private_vegano + '"vegetariano":' + self.__private_vegetariano 
        + '}'
    
    @cliente.setter
    def cliente (self, vCliente):
        jsonCliente = json.loads(vCliente) 
        self.__private_id = jsonCliente["id"]
        self.__private_nombre = jsonCliente["nombre"]
        self.__private_apellido = jsonCliente["apellido"]
        self.__private_email = jsonCliente["email"]
        self.__private_telefono = jsonCliente["telefono"]
        self.__private_direccion = jsonCliente["direccion"]
        self.__private_piso = jsonCliente["piso"]
        self.__private_dpto = jsonCliente["departamento"]
        self.__private_ciudad = jsonCliente["ciudad"]
        self.__private_provincia = jsonCliente["provincia"]
        self.__private_pais = jsonCliente["pais"]
        self.__private_carnivoro = jsonCliente["carnivoro"]
        self.__private_celiaco = jsonCliente["celiaco"]
        self.__private_vegano = jsonCliente["vegano"]
        self.__private_vegetariano = jsonCliente["vegetariano"]

    @property
    def nombre (self):
        return self.__private_nombre

    @nombre.setter
    def nombre (self,vNombre):
        self.__private_nombre = vNombre

    @property
    def apellido (self):
        return self.__private_apellido

    @apellido.setter
    def apellido(self,vApellido):
        self.__private_apellido = vApellido

    @property
    def email (self):
        return self.__private_email
    
    @email.setter
    def email(self, vEmail):
        self.__private_email = vEmail

    @property
    def telefono (self):
        return self.__private_telefono

    @telefono.setter
    def telefono (self, vTelefono):
        self.__private_telefono = vTelefono
    
    @property
    def domicilio (self):
        return [self.__private_direccion,self.__private_piso,self.__private_dpto,self.__private_ciudad,self.__private_provincia,
                self.__private_pais]
    
    @domicilio.setter
    def domicilio (self,vDomicilio):
        self.__private_direccion = vDomicilio[0]
        self.__private_piso = vDomicilio[1]
        self.__private_dpto = vDomicilio[2]
        self.__private_ciudad = vDomicilio[3]
        self.__private_provincia = vDomicilio[4]
        self.__private_pais = vDomicilio[5]

    @property
    def dieta (self):
        return [self.__private_carnivoro, self.__private_celiaco,self.__private_vegano,self.__private_vegetariano]
    
    @dieta.setter
    def dieta (self,vDieta):
        self.__private_carnivoro = vDieta[0]
        self.__private_celiaco = vDieta[1]
        self.__private_vegano = vDieta[2]
        self.__private_vegetariano = vDieta[3]
