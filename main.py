import repository.repositoryDB as db
import subprocess

basedatos = db.baseDeDatos("###","XXX")
basedatos.creoBaseDeDatos("comiendohastaloscodos")
basedatos.creoTablas("comiendohastaloscodos")
basedatos.cierroConeccion()
subprocess.run(["flask --app ./controller/controladorFlask.py run"],shell=True,)