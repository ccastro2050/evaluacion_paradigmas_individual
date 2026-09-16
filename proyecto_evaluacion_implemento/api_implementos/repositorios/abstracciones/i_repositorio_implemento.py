"""
El CONTRATO del repositorio. Lo que el servicio puede pedir, sin saber
contra que motor se cumple.

Se declara como Protocol (tipado estructural): la implementacion NO hereda.

AQUI VA:
  - la firma de cada operacion: listar activos, obtener por codigo, crear,
    reemplazar, actualizar parcial, dar de baja

AQUI NO VA:
  - ni una linea de SQL
  - ni el nombre PostgreSQL
"""
