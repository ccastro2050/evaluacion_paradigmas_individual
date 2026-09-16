"""
El SQL, y solo aqui. Unica clase que sabe hablar con PostgreSQL.

AQUI VA:
  - las consultas, SIEMPRE PARAMETRIZADAS (:codigo), nunca concatenadas
  - el filtro `WHERE activo = TRUE` en los listados
  - la baja LOGICA: UPDATE ... SET activo = FALSE, nunca DELETE FROM

AQUI NO VA:
  - reglas de negocio
  - codigos de estado HTTP
  - la cadena de conexion quemada: llega por el constructor

OJO CON DOS COSAS QUE LA EVALUACION MIRA:
  1. Concatenar un valor en el SQL es inyeccion. Siempre parametro.
  2. Un listado sin `WHERE activo = TRUE` muestra lo que ya se dio de baja.
"""
