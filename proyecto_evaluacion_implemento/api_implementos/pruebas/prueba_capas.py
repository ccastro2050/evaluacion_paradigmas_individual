"""
La prueba de capas: corre el servicio SIN base de datos.

COMO:
  Se le pasa al servicio un repositorio FALSO —una clase de mentiras que
  cumple la misma interfaz— y se comprueba que el servicio funciona igual.

QUE DEMUESTRA:
  Que el servicio depende del CONTRATO y no de PostgreSQL. Si esta prueba
  necesita la base encendida, las capas no estan separadas.

Se corre con:  python -m api_implementos.pruebas.prueba_capas
"""
