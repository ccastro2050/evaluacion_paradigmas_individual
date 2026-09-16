"""
La capa que habla HTTP, y la unica.

AQUI VA:
  - las seis rutas sobre /api/implemento
  - los codigos de estado: 200, 201, 204, 404, 422
  - traducir la excepcion del dominio a su codigo

AQUI NO VA:
  - SQL
  - reglas de negocio

EL CONTRASTE QUE ESTA VERSION ENSENA, y que la rubrica mira:
  PUT   reemplaza COMPLETO  -> 422 si falta un campo obligatorio
  PATCH cambia SOLO lo enviado -> 200 con el cuerpo parcial
  Si sus dos verbos se comportan igual, la version no esta hecha.
"""
