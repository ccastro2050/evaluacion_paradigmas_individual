# Reflexión — Evaluación individual

> **Copie este archivo a la raíz de su repositorio con el nombre
> `REFLEXION.md` y respóndalo ahí.** Es el **60 %** de la evaluación.
>
> **Deje los encabezados como están.** Se califica buscando cada uno.

---

## Identificación

| | |
|---|---|
| **Nombre completo** | |
| **Usuario de GitHub** | |
| **Enlace del repositorio** (privado) | |
| **¿Invitó a `ccastro2050`?** | |
| **Fecha** | |
| **Herramientas de IA que usó** | *(cuáles, y para qué cada una)* |

---

# B1 · Su propio código — 20 %

> **Cada respuesta necesita archivo y línea.** Una respuesta correcta sin la
> referencia **no puntúa**: lo que se mide es que usted sepa **dónde vive cada
> cosa** en lo que construyó.
>
> Formato de la referencia: `api_implementos/repositorios/repositorio_implemento_postgresql.py:47`

---

### 1 · El SQL parametrizado

**Señale la línea donde su repositorio parametriza un valor.**

```
Archivo y línea:
```

```python
(pegue aquí la línea)
```

**Escriba cómo se vería esa misma línea concatenando:**

```python
(la versión mala)
```

**¿Qué podría hacer alguien con la versión concatenada?** *(un caso concreto:
qué escribiría en el campo y qué pasaría)*

---

### 2 · El servicio no sabe de HTTP

**Muestre que su servicio no menciona `request`, `response` ni códigos de
estado.**

```
Archivo:
```

*(pegue el método completo)*

**¿Por qué importa?** *(no «porque lo dice la constitución»: qué se rompería
si el servicio sí supiera de HTTP)*

---

### 3 · Mañana la base es MySQL

**¿Qué archivos toca?**

**¿Cuáles NO toca?**

**¿Qué principio se lo permite, y por qué?**

---

### 4 · La baja lógica

**Señale dónde su `DELETE` marca en vez de borrar.**

```
Archivo y línea:
```

**¿Qué devuelve el segundo `DELETE` sobre el mismo código?**

**¿Por qué?** *(y qué habría pasado si el borrado fuera físico)*

---

### 5 · Las claves foráneas

**¿Por qué `implemento` no tiene claves foráneas y `prestamo` tiene dos?**

---

# B2 · Interpretar código que escribió una IA — 25 %

> **Es el bloque que más pesa.** Los cuatro fragmentos **corren**: ninguno
> tiene error de sintaxis. Los cuatro tienen un defecto.
>
> **Si no encuentra el defecto, dígalo.** «Lo leí, no le veo el problema»
> puntúa más que inventar uno que no está.

---

## Fragmento 1 — la búsqueda por nombre

**a) ¿Qué hace este código?**

**b) ¿Qué tiene mal?**

**c) ¿Qué pasa en producción?** *(un caso concreto: qué escribe alguien, y qué
ocurre)*

**d) Reescríbalo bien:**

```python

```

**¿Qué regla del curso lo obliga?**

---

## Fragmento 2 — el servicio que obtiene

**a) ¿Qué hace este código?**

**b) ¿Qué tiene mal?**

**c) ¿Qué pasa en producción?** *(pista: piense en qué pasa el día que ese
servicio se llame desde algo que no sea una petición web)*

**d) Reescríbalo bien:**

```python

```

**¿Qué regla del curso lo obliga?**

---

## Fragmento 3 — el borrado

**a) ¿Qué hace este código?**

**b) ¿Qué tiene mal?** *(hay más de una cosa)*

**c) ¿Qué pasa en producción?**

**d) Reescríbalo bien:**

```python

```

**¿Qué regla del curso lo obliga?**

---

## Fragmento 4 — el endpoint que sirve para todo

**a) ¿Qué hace este código?**

**b) ¿Qué tiene mal?**

**c) ¿Qué pasa en producción?**

**d) Reescríbalo bien:**

```python

```

**¿Qué regla del curso lo obliga?**

**e) Este fragmento tiene MÁS DE UN defecto. Enumérelos:**

| # | Defecto | Por qué es un defecto |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

**¿Cuál es el más grave, y por qué?**

---

# B3 · Su proceso con la IA — 15 %

> Aquí no hay respuesta correcta: **hay respuesta honesta o no la hay.**

---

### 6 · Un prompt suyo, literal

**No lo mejore para la entrega.** El que usó, tal como lo escribió — con sus
errores de dedo si los tenía.

```text

```

**¿Qué le devolvió?** *(resumido en dos líneas)*

---

### 7 · Algo que la IA le dio y usted NO usó

```python

```

**¿Por qué lo descartó?**

---

### 8 · Cuando la IA se equivocó

**¿En qué momento le dijo algo que resultó estar mal?**

*(Si no le pasó, escriba «no me pasó» — y diga entonces **cómo comprobó** que
lo que le daba estaba bien. Esa es la pregunta de verdad.)*

**¿Cómo se dio cuenta?**

---

### 9 · Lo que escribió usted, de principio a fin

**Señale con archivo y línea la parte que escribió sin IA.**

```
Archivo y líneas:
```

**¿Por qué esa parte la hizo a mano?**

---

### 10 · Si mañana le quitan la IA

**¿Qué parte de esta evaluación no habría podido hacer?**

> **Decir «esta parte no la habría podido hacer» NO baja la nota.** Es la
> respuesta que más se valora **si viene con el detalle de por qué**. Lo que no
> puntúa es «lo habría hecho todo igual».

---

## Antes de entregar

- [ ] Cada respuesta de **B1** tiene **archivo y línea**
- [ ] Los **cuatro fragmentos** de B2 están respondidos, con sus cuatro
      preguntas cada uno
- [ ] El fragmento 4 tiene además la pregunta **(e)**
- [ ] El prompt de la **6** es literal, no reescrito
- [ ] La **8** dice la verdad
- [ ] Este archivo se llama **`REFLEXION.md`** y está en la **raíz** del
      repositorio
- [ ] `ccastro2050` está invitado al repositorio
