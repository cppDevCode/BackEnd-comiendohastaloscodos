import controller.controladorFlask as fApp
import service.inicializadorCliente as servicio


'''
MODULO PRINCIPAL DE APLICACION
CREO LA BASE DE DATOS,LAS TABLAS EN CASO DE NO EXISTIR y cargo datos de prueba de productos y precios
'''
inicializar = servicio.Inicializador("comiendohastaloscodos")
inicializar.cargoDatosPrueba("comiendohastaloscodos",True)



#INSTANCIACION DE LA APP DE FLASK

aplicacionFlask = fApp.AppFlask()
if __name__ == '__main__':
    aplicacionFlask.run()
    
