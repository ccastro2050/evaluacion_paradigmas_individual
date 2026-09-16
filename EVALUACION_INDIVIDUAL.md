# Evaluación individual — Paradigmas de Programación

**Préstamo de implementos deportivos · versión 1 con Spec Kit**

| | |
|---|---|
| **Modalidad** | **Individual** |
| **Peso** | **15 %** |
| **Reparto** | **40 % lo que construye · 60 % lo que reflexiona** |
| **Fecha** | **miércoles 16 de septiembre de 2026** |
| **Hora** | **de 2:00 p. m. a 4:00 p. m.** — **dos horas** |
| **Entrega** | a las **4:00 p. m.**: lo que esté en su repositorio a esa hora |

> **Lo primero, antes de leer el resto: cree su repositorio privado e invite a
> `ccastro2050`.** No es el primer paso del trabajo; es el requisito para
> empezar. **Sin esa invitación su entrega no existe**, y a las 4:00 p. m. ya
> no hay tiempo de arreglarlo. Los pasos están en la sección 2.

> ### Dos horas: en qué gastarlas
>
> El reparto de la nota **no es el reparto del tiempo**. Con dos horas:
>
> | | Tiempo sugerido | Por qué |
> |---|---|---|
> | Repositorio e invitación | **5 min** | Sin esto no hay entrega |
> | `2_spec.md` | **20 min** | Aquí se decide si el resto tiene sentido |
> | La API y la pantalla | **55 min** | Una tabla. Use los ejemplos del curso |
> | **`REFLEXION.md`** | **40 min** | **Es el 60 % de la nota** |
>
> **A las 3:20 pare de programar**, esté como esté la API, y empiece la
> reflexión. Una entrega con la API a medias y la reflexión completa **saca
> más** que al revés. No es un accidente del enunciado: es lo que se quiso
> medir.

---

## 1. Lo que esta evaluación mide, y en qué se diferencia de la de equipos

La evaluación por equipos midió **si el equipo sabe aplicar el método**. Esta
mide otra cosa:

> **Si usted entiende el código que hay en su pantalla — lo haya escrito usted
> o se lo haya escrito una IA.**

Por eso el reparto está invertido respecto de lo habitual:

| | Peso | Qué es |
|---|---|---|
| **A · Lo que construye** | **40 %** | Una tabla, tres capas, una pantalla. Modesto a propósito |
| **B · Lo que reflexiona** | **60 %** | Su código, **código ajeno generado por IA**, y su propio proceso |

**Y una regla que conviene leer dos veces:**

> **Usar IA está permitido y se espera.** Lo que se evalúa **no es si la usó**,
> sino **si entiende lo que le devolvió**. Un estudiante que genera código
> correcto y no sabe explicarlo saca menos que uno que genera código con un
> defecto, lo encuentra, y explica por qué estaba mal.

---

## 2. Antes de empezar: el repositorio, en cinco pasos

**No hay repositorio creado.** Lo crea usted, y **le toma cinco minutos**.

### Paso 1 · Crear el repositorio en GitHub

1. Entre a **github.com** con su cuenta.
2. Arriba a la derecha, el botón **+** → **New repository**.
3. Llénelo así:

| Campo | Qué poner |
|---|---|
| **Repository name** | `evaluacion_paradigmas` |
| **Description** | Evaluación individual · Paradigmas de Programación |
| **Visibility** | **Private** ← **no público** |
| **Add a README file** | ✅ márquelo — así el repositorio nace con una rama |

4. **Create repository**.

### Paso 2 · Invitar al profesor — **esto es lo que hace que su entrega exista**

1. Dentro de su repositorio, pestaña **Settings** (arriba, a la derecha).
2. En el menú de la izquierda: **Collaborators**.
3. GitHub le va a pedir la contraseña otra vez. Es normal.
4. Botón **Add people**.
5. Escriba exactamente:

```
ccastro2050
```

6. Elíjalo de la lista y confirme con **Add ccastro2050 to this repository**.
7. **Compruébelo:** debe quedar una línea que dice **«Pending invite»**. Si no
   la ve, la invitación no se envió.

> **El error que se repite todos los semestres:** escribir mal el usuario. Si
> el «Pending invite» aparece con **otro nombre**, invitó a un desconocido.
> Quítelo e invite de nuevo. **Es `ccastro2050`**, con dos ces y sin puntos.

### Paso 3 · Traerlo a su computador

```bash
git clone https://github.com/SU_USUARIO/evaluacion_paradigmas.git
cd evaluacion_paradigmas
```

### Paso 4 · Copiar el andamiaje

Copie dentro la carpeta **`proyecto_evaluacion_implemento`** que le entregó el
profesor. Trae la estructura hecha, el `db/init.sql` y un comentario en cada
archivo diciendo qué va ahí.

### Paso 5 · El primer commit, ya

```bash
git add .
git commit -m "Andamiaje de la evaluación individual"
git push
```

> **Haga este primer push ahora, no al final.** Si a las 4:00 p. m. su
> repositorio está vacío, no hay nada que calificar — aunque en su computador
> esté todo. **Y haga un commit por fase**, no uno solo al final: el historial
> es parte de lo que se mira.

---

## 3. El problema

> Bienestar Universitario **presta implementos deportivos**: balones, raquetas,
> colchonetas. De cada **implemento** interesa su código, su nombre, en qué
> **estado** está —bueno, regular, dado de baja— y cuántas unidades hay.
> Los **estudiantes** piden prestado; de cada **préstamo** interesa la fecha en
> que salió, la fecha en que se devolvió, y si se devolvió completo.

Cuatro frases. **Es un dominio nuevo a propósito**: no se parece al de talleres
—que fue el de equipos— ni al de facturación —que es el ejemplo de referencia—.
No hay un repositorio del que copiar la respuesta.

---

## 4. Qué construye: **una sola tabla, y no se elige**

**Todos construyen `implemento`.** No hay opción, y eso también es a propósito:
con todos sobre la misma tabla, las reflexiones son comparables y las
respuestas copiadas se notan de inmediato.

`implemento` es **la única tabla sin clave foránea** del modelo, y ahí está la
primera pregunta que va a tener que contestar: **por qué**.

### El modelo, completo

```
implemento(codigo PK, nombre, estado, unidades, activo)
estudiante(documento PK, nombre, correo, semestre, activo)
prestamo(id PK, implemento FK → implemento, estudiante FK → estudiante,
         fecha_salida, fecha_devolucion, devuelto_completo, activo)
```

### El script de PostgreSQL

```sql
-- ---------------------------------------------------------------------------
-- Prestamo de implementos deportivos · Bienestar Universitario
-- Artefacto DADO: no se modifica. Los datos son HIPOTETICOS.
-- ---------------------------------------------------------------------------

DROP TABLE IF EXISTS prestamo;
DROP TABLE IF EXISTS estudiante;
DROP TABLE IF EXISTS implemento;

-- La unica tabla SIN clave foranea.
CREATE TABLE implemento (
    codigo    varchar(10)  NOT NULL,
    nombre    varchar(60)  NOT NULL,
    estado    varchar(10)  NOT NULL,
    unidades  integer      NOT NULL,
    activo    boolean      NOT NULL DEFAULT TRUE,

    CONSTRAINT pk_implemento       PRIMARY KEY (codigo),
    CONSTRAINT uq_implemento_nom   UNIQUE (nombre),
    CONSTRAINT chk_implemento_est  CHECK (estado IN ('BUENO','REGULAR','BAJA')),
    CONSTRAINT chk_implemento_uni  CHECK (unidades >= 0)
);

CREATE TABLE estudiante (
    documento varchar(15)  NOT NULL,
    nombre    varchar(80)  NOT NULL,
    correo    varchar(120) NOT NULL,
    semestre  integer      NOT NULL,
    activo    boolean      NOT NULL DEFAULT TRUE,

    CONSTRAINT pk_estudiante      PRIMARY KEY (documento),
    CONSTRAINT uq_estudiante_cor  UNIQUE (correo),
    CONSTRAINT chk_estudiante_sem CHECK (semestre BETWEEN 1 AND 12)
);

CREATE TABLE prestamo (
    id                 integer GENERATED ALWAYS AS IDENTITY,
    implemento         varchar(10) NOT NULL,
    estudiante         varchar(15) NOT NULL,
    fecha_salida       date        NOT NULL,
    fecha_devolucion   date,
    devuelto_completo  boolean,
    activo             boolean     NOT NULL DEFAULT TRUE,

    CONSTRAINT pk_prestamo      PRIMARY KEY (id),
    CONSTRAINT fk_prestamo_imp  FOREIGN KEY (implemento) REFERENCES implemento(codigo),
    CONSTRAINT fk_prestamo_est  FOREIGN KEY (estudiante) REFERENCES estudiante(documento),
    CONSTRAINT chk_prestamo_fec CHECK (fecha_devolucion IS NULL
                                       OR fecha_devolucion >= fecha_salida)
);

-- Datos HIPOTETICOS. Ninguna persona real.
INSERT INTO implemento (codigo, nombre, estado, unidades) VALUES
    ('BAL-001', 'Balon de futbol n.5',     'BUENO',   12),
    ('BAL-002', 'Balon de baloncesto n.7', 'BUENO',    8),
    ('RAQ-001', 'Raqueta de tenis',        'REGULAR',  4),
    ('COL-001', 'Colchoneta de yoga',      'BUENO',   20),
    ('RAQ-002', 'Raqueta de badminton',    'BAJA',     2);

INSERT INTO estudiante (documento, nombre, correo, semestre) VALUES
    ('1000000001', 'Estudiante Uno',  'uno@ejemplo.edu.co',  3),
    ('1000000002', 'Estudiante Dos',  'dos@ejemplo.edu.co',  5),
    ('1000000003', 'Estudiante Tres', 'tres@ejemplo.edu.co', 8);

INSERT INTO prestamo (implemento, estudiante, fecha_salida, fecha_devolucion,
                      devuelto_completo) VALUES
    ('BAL-001', '1000000001', DATE '2026-09-01', DATE '2026-09-03', TRUE),
    ('COL-001', '1000000002', DATE '2026-09-05', NULL,              NULL),
    ('RAQ-001', '1000000003', DATE '2026-09-08', DATE '2026-09-08', FALSE);
```

> **`prestamo` y `estudiante` existen en la base y NO se tocan.** Son de una v2
> que aquí no se pide. Están para que usted pueda contestar por qué
> `implemento` no tiene claves foráneas y ellas sí.

---

## 5. Parte A — lo que construye (40 %)

Lo mismo que en la evaluación por equipos, pero **una sola tabla y una sola
persona**:

1. **El spec kit de la v1**, completo y **antes** del código.
2. **La API**: los seis endpoints sobre `implemento`, en tres capas con
   interfaces.
3. **La pantalla**: lista y crea, y **sigue en pie con la API apagada**.
4. **Un solo comando**: `docker compose up -d --build`.

### El contrato mínimo

| Verbo | Ruta | Qué hace | Éxito | Error |
|---|---|---|---|---|
| `GET` | `/api/implemento` | Lista los **activos** | 200 | — |
| `GET` | `/api/implemento/{codigo}` | Uno | 200 | 404 |
| `POST` | `/api/implemento` | Crea | 201 | **422** si falta un campo |
| `PUT` | `/api/implemento/{codigo}` | **Reemplaza completo** | 200 | **422** si falta un campo |
| `PATCH` | `/api/implemento/{codigo}` | **Cambia solo lo enviado** | 200 | 404 |
| `DELETE` | `/api/implemento/{codigo}` | **Baja LÓGICA** | 204 | 404 al repetirlo |

> **El contraste `PUT` 422 / `PATCH` 200 es lo que esta versión enseña.** Si sus
> dos verbos se comportan igual, la versión no está hecha.

---

## 6. Parte B — lo que reflexiona (60 %)

Se responde en **`REFLEXION.md`**, en la raíz de su repositorio. Son **tres
bloques**, y cada uno pesa distinto.

---

### B1 · Su propio código — **20 %**

**Cada respuesta exige señalar su código con archivo y línea**, y después
explicar con sus palabras. Una respuesta correcta **sin la referencia no
puntúa**.

| # | Pregunta |
|---|---|
| **1** | Señale la línea donde su repositorio **parametriza** un valor. Escriba cómo se vería esa misma línea concatenando, y **qué podría hacer alguien** con ella |
| **2** | Muestre que su **servicio no sabe de HTTP**: ni `request`, ni `response`, ni códigos de estado. ¿Por qué importa? |
| **3** | *«Mañana la base es MySQL.»* ¿Qué archivos toca y cuáles **no**? ¿Qué principio se lo permite? |
| **4** | Señale dónde su `DELETE` hace la baja **lógica**. ¿Qué devuelve el segundo `DELETE` sobre el mismo código, y por qué? |
| **5** | ¿Por qué `implemento` **no tiene** claves foráneas y `prestamo` tiene **dos**? |

---

### B2 · Interpretar código que escribió una IA — **25 %**

**Este es el bloque que más pesa, y es el nuevo.**

Abajo hay **cuatro fragmentos** que una IA devolvió cuando se le pidió «una API
de implementos en tres capas con FastAPI». **Los cuatro corren.** Ninguno tiene
un error de sintaxis. Y **los cuatro tienen un defecto** que este curso ya vio.

Por cada fragmento conteste **las cuatro preguntas**, en este orden:

```
a) ¿Qué hace este código? (dos o tres líneas, con sus palabras)
b) ¿Qué tiene mal?
c) ¿Qué pasa el día que esto esté en producción? Un caso CONCRETO.
d) Reescríbalo bien. Y diga qué regla del curso lo obliga.
```

> **Si no encuentra el defecto, dígalo.** «Lo leí, no le veo el problema»
> puntúa más que inventar un defecto que no está. Lo que no puntúa es copiar el
> fragmento y decir «está mal».

---

#### Fragmento 1

```python
class RepositorioImplementoPostgreSQL:
    def __init__(self, cadena_conexion: str):
        self._engine = create_async_engine(cadena_conexion)

    async def buscar_por_nombre(self, nombre: str) -> list[dict]:
        sql = "SELECT * FROM implemento WHERE nombre LIKE '%" + nombre + "%'"
        async with self._engine.connect() as cx:
            filas = await cx.execute(text(sql))
            return [dict(f._mapping) for f in filas]
```

---

#### Fragmento 2

```python
class ServicioImplemento:
    def __init__(self, repositorio):
        self._repositorio = repositorio

    async def obtener(self, codigo: str):
        fila = await self._repositorio.obtener_por_codigo(codigo)
        if fila is None:
            raise HTTPException(status_code=404, detail="No encontrado")
        return fila
```

---

#### Fragmento 3

```python
@app.delete("/api/implemento/{codigo}", status_code=204)
async def eliminar(codigo: str, servicio=Depends(obtener_servicio)):
    await servicio.eliminar(codigo)
    return None


# ... en el repositorio:
async def eliminar(self, codigo: str) -> None:
    sql = "DELETE FROM implemento WHERE codigo = :codigo"
    async with self._engine.begin() as cx:
        await cx.execute(text(sql), {"codigo": codigo})
```

---

#### Fragmento 4

```python
@app.get("/api/{tabla}")
async def listar_cualquier_cosa(tabla: str, limite: int | None = None):
    """Un solo endpoint para todas las tablas. Menos codigo repetido."""
    sql = f"SELECT * FROM {tabla} LIMIT :limite"
    async with engine.connect() as cx:
        filas = await cx.execute(text(sql), {"limite": limite or 50000})
        return [dict(f._mapping) for f in filas]
```

> **Del fragmento 4 conteste además una quinta pregunta:**
> **e)** Este fragmento tiene **más de un** defecto. Enumérelos, y diga **cuál
> es el más grave y por qué**.

---

### B3 · Su proceso con la IA — **15 %**

Aquí no hay respuesta correcta: **hay respuesta honesta o no la hay.**

| # | Qué pide |
|---|---|
| **6** | **Copie un prompt suyo, literal**, de los que usó en esta evaluación. No lo mejore para la entrega: el que usó |
| **7** | Copie **un pedazo de lo que la IA le devolvió y usted NO usó**, y diga por qué lo descartó |
| **8** | ¿En qué momento la IA le dijo algo **que resultó estar mal**? Si no le pasó, escriba *«no me pasó»* — y diga entonces **cómo lo comprobó** |
| **9** | De lo que entregó, **¿qué parte escribió usted de principio a fin**, sin IA? Señálela con archivo y línea |
| **10** | Si mañana le quitan la IA, **¿qué parte de esta evaluación no habría podido hacer?** |

> **La 8 y la 10 son las que no se pueden fingir.** Un estudiante que dice «la
> IA nunca se equivocó y yo lo habría hecho todo igual sin ella» está
> describiendo una tarde que no ocurrió.
>
> **Y decir «esta parte no la habría podido hacer» no baja la nota.** Es la
> respuesta que más se valora si viene con el detalle de por qué.

---

## 7. Rúbrica

### A · Lo que construyó — 40 %

| Criterio | Peso | Cumple (3.0 – 5.0) | No cumple (0 – 2.9) |
|---|---|---|---|
| **Spec kit antes del código** | 10 % | Los documentos existen, están **antes** en el historial, y el `9_checklist` está firmado | No hay spec, o se escribió después |
| **API en tres capas** | 15 % | Seis endpoints, **PUT 422 / PATCH 200**, el controlador no sabe SQL y el servicio no sabe HTTP | Endpoints caídos, o todo en un archivo |
| **Baja lógica** | 5 % | `DELETE` marca `activo = FALSE`; los listados filtran; el segundo da 404 | Borrado físico, o los inactivos siguen apareciendo |
| **Pantalla y un solo comando** | 10 % | Consume la API, **sigue en pie con la API apagada**, y `docker compose up` levanta todo | No hay pantalla, o hay que correr pasos a mano |

### B · Lo que reflexionó — 60 %

| Criterio | Peso | Cumple (3.0 – 5.0) | No cumple (0 – 2.9) |
|---|---|---|---|
| **B1 · Su código** | 20 % | Las cinco, **con archivo y línea**, y la explicación describe **su** código | Genéricas, sin referencia, o describen un código que no es el suyo |
| **B2 · Código de la IA** | 25 % | Encuentra los defectos, explica **qué pasa en producción con un caso concreto**, y la corrección funciona | Dice «está mal» sin decir qué, o corrige sin explicar, o inventa defectos que no están |
| **B3 · Su proceso** | 15 % | Prompts literales, un descarte real, **un error de la IA contado**, y qué sabe hacer sin ella | Prompts embellecidos, «la IA nunca falló», o respuestas que describen un proceso ideal |

> **Cómo se desempata dentro de «Cumple».** Entre dos entregas correctas, sube
> la que **muestra el proceso**: el defecto que encontró y no era obvio, el
> prompt que no funcionó, la decisión que reconsideró.

---

## 8. Lo que esta evaluación NO pide

- **Modelar la base.** Está hecha, en §3.
- **`estudiante` ni `prestamo`.** Existen en la base y **no se tocan**.
- **Autenticación, roles ni JWT.**
- **Validar que haya unidades disponibles** antes de prestar. Es una regla de
  dos tablas, y es de otra versión.
- **Informes, dashboard ni consultas multitabla.**

---

## 9. Para empezar hoy

1. **Cree el repositorio e invite a `ccastro2050`** — los cinco pasos de §2.
   **Cinco minutos, y sin esto no hay entrega.**
2. Levante solo la base con el script de §4 y **cuente las filas** de
   `implemento`. Deben ser cinco.
3. **Escriba el `2_spec.md` antes de tocar código.** Si un criterio de
   aceptación no dice **un número o un código de estado**, no es un criterio.
4. Marque con `[NECESITA ACLARACIÓN]` lo que el enunciado no diga. **Se busca
   que marque:** quien no marcó nada, o no leyó, o rellenó los huecos a ojo.
5. Construya, y **haga un commit por fase** con lo que probó en cada una.
6. **Deje `REFLEXION.md` para el final, pero no para los últimos diez
   minutos.** Pesa el 60 %.

> **Y una advertencia sobre el reparto.** Una entrega con la API impecable y
> `REFLEXION.md` a medias saca menos que una con la API incompleta y la
> reflexión completa. **No es un error del enunciado: es lo que se quiso
> medir.**
