# Comiendo Hasta los Codos BackEnd

Ofrece soporte de persistencia y consulta de datos a base de datos relacional mysql sin ORM


### Requisitos
* Python 3.8+
* flask
* flask-cors
* mysql-connector-python
* jinja2
* Flask-MySQL


### Configuracion de Coneccion a Base de Datos

JSON en el raiz del proyecto setting.json:

{
    "usuario": "usuario",
    "contrasena": "contraseña"
}

Al iniciar el Server al crearse las tablas se crean automaticamente datos en la tabla productos y precios para hacer las pruebas.

### HTTP CODES

* 200 OK
* 201 Creado/Modificado
* 490 No se recibio un Archivo JSON
* 491 Usuario ya existente (1062)
* 492 Error en consulta con BBDD
* 493 No se ha encontrado registro con ID=[NRO_ID]
* 494 Usuario/Contraseña Erroneo
