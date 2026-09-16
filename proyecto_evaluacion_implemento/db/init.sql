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
