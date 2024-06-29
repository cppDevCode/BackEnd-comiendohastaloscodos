import repository.repositoryDB as db
from json import load



class Inicializador:
    __private_basedatos = None

    def __init__(self,nombreBaseDatos):
        self.__private_basedatos = db.baseDeDatos()
        self.__private_basedatos.creoBaseDeDatos(nombreBaseDatos)
        self.__private_basedatos.creoTablas(nombreBaseDatos) 

    def cargoDatosPrueba(self,nombreBaseDatos,datosPrueba):
        print ("[Datos Prueba] Inicializacion funcion...")
        if datosPrueba:
            print ("[Datos Prueba] Cargando Datos de prueba de productos desde carpeta 'data'...")
            print ("[Datos Prueba] Verificando existencia de datos...")
            cantidadRegistro = self.__private_basedatos.getCantidadRegistrosTabla(nombreBaseDatos,'tblPlatos')
            if cantidadRegistro == 0:
                with open('data/productos.json','r') as archivo:
                    jsonArchivo = load(archivo)
                valores = []
                for variable in jsonArchivo:
                    plato = ()
                    plato += (variable["nombre"],variable["descripcion"],variable["imgRuta"],variable["tipo"])
                    valores.append(plato)
                
                self.__private_basedatos.agregoRegistros("tblPlatos","`nombre`,`descripcion`,`imgRuta`,`tipo`",valores,4,nombreBaseDatos,True)
                with open('data/precios.json','r') as archivo:
                    jsonArchivo = load(archivo)
                valores = []
                for variable in jsonArchivo:
                    precio = ()
                    precio += (variable["idPlato"],variable["precio"],variable["vigencia"])
                    valores.append(precio)
                self.__private_basedatos.agregoRegistros("tblPrecio","`idPlato`,`precio`,`vigencia`",valores,3,nombreBaseDatos,True)
                print ("[Datos Prueba] Carga de datos Finalizada!")
            else: print ("[Datos Prueba] La tabla tiene datos, no se cargan datos de prueba...")
            self.__private_basedatos.cierroConeccion()
        else:
            self.__private_basedatos.cierroConeccion()