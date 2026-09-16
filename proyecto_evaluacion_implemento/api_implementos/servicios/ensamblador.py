"""
El ensamblador: el UNICO sitio donde se dice que implementacion concreta
cumple cada contrato.

AQUI VA:
  - leer la cadena de conexion del ENTORNO (nunca quemada)
  - construir el repositorio concreto y entregarselo al servicio

POR QUE EXISTE:
  Para que el dia que la base sea MySQL, se cambie AQUI y en el repositorio
  nuevo, y no en el servicio ni en el controlador. Es la inversion de
  dependencias, y es la pregunta 3 de la reflexion.
"""
