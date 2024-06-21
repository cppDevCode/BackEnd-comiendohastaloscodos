import repository.repositoryDB as db
import controller.controladorFlask as fApp


basedatos = db.baseDeDatos("USUARIO","CONTRASENA")
basedatos.creoBaseDeDatos("comiendohastaloscodos")
basedatos.creoTablas("comiendohastaloscodos")
basedatos.cierroConeccion()

aplicacionFlask = fApp.AppFlask()
if __name__ == '__main__':
    aplicacionFlask.run()
