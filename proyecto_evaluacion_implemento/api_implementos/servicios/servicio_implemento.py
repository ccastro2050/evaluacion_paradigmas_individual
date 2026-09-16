"""
Las reglas del negocio.

ESTA CAPA NO SABE DE HTTP. Si aqui aparece `HTTPException`, `status_code`,
`request` o `response`, la separacion se rompio — y es una de las preguntas
de la reflexion.

AQUI VA:
  - decidir que pasa cuando el implemento no existe: se lanza una excepcion
    PROPIA del dominio, no una de HTTP
  - la diferencia entre reemplazo completo y cambio parcial
  - la baja logica como regla, no como detalle del SQL

AQUI NO VA:
  - SQL: se le pide al repositorio POR SU INTERFAZ
  - codigos de estado: los pone el controlador
"""
