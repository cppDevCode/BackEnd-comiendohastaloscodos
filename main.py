import repository.repositoryDB as db

basedatos = db.baseDeDatos("prueba","XXXX")
basedatos.creoBaseDeDatos("comiendohastaloscodos")
basedatos.creoTablas("comiendohastaloscodos")
basedatos.cierroConeccion()