import repository.repositoryDB as db
import controller.controladorFlask as fApp


'''
MODULO PRINCIPAL DE APLICACION
CREO LA BASE DE DATOS Y LAS TABLAS EN CASO DE NO EXISTIR
'''
basedatos = db.baseDeDatos("estilo3d","golpea1987")
basedatos.creoBaseDeDatos("comiendohastaloscodos")
basedatos.creoTablas("comiendohastaloscodos")
basedatos.cierroConeccion()


#INSTANCIACION DE LA APP DE FLASK

aplicacionFlask = fApp.AppFlask()
if __name__ == '__main__':
    aplicacionFlask.run()
