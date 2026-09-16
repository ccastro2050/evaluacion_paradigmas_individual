"""
La pantalla. Es un proceso APARTE de la API.

AQUI VA:
  - las rutas de las vistas: lista y formulario
  - llamar a la API a traves de cliente_api.py

AQUI NO VA, Y ES LO QUE SE CALIFICA:
  - el driver de PostgreSQL
  - la cadena de conexion
  - una sola linea de SQL

Con la API apagada (`docker compose stop api-implementos`) esta pantalla
tiene que SEGUIR EN PIE y explicar el problema. Una pantalla en blanco o un
error de Python en el navegador no cumple.
"""
