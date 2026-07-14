# Banco de preguntas libres para opositores

Banco abierto de preguntas tipo test para la preparación de oposiciones, disponible para uso no comercial.

## OpenOpo.es

Este banco forma parte del proyecto **OpenOpo.es**, una iniciativa que nace de **Iván Barreda, opositor**, para hacer más accesible la preparación de oposiciones mediante contenido abierto, gratuito y reutilizable para fines no comerciales.

Los valores del proyecto son:

- **Accesibilidad:** facilitar que cualquier opositor pueda estudiar con materiales claros y disponibles.
- **Apertura:** publicar bancos de preguntas en formatos sencillos, descargables y revisables.
- **Gratuidad del contenido:** OpenOpo.es no cobrará nunca por el contenido de las preguntas publicado en este repositorio.

OpenOpo.es sí podrá cobrar por la **organización, ordenación, herramientas, filtros avanzados, experiencia de uso, mantenimiento, soporte o servicios añadidos** construidos alrededor de ese contenido. Es decir: el contenido permanece gratuito; lo que puede ser de pago es la capa de organización o servicio.

## Fuentes

Las preguntas se elaboran a partir de documentos públicos y accesibles, como textos legales, normativa consolidada, boletines oficiales, temarios públicos o referencias administrativas disponibles públicamente.

Cuando una pregunta incorpora referencias normativas, el CSV puede incluir campos de fuente como `source_excerpt`, `source_url`, `source_version` o equivalentes. Los textos legales, disposiciones administrativas y documentos públicos citados conservan su régimen jurídico propio y no quedan apropiados por este proyecto.

## Licencia resumida

Salvo que se indique lo contrario, las preguntas, explicaciones, clasificaciones y organización del banco se publican bajo **Creative Commons Atribución-NoComercial 4.0 Internacional (CC BY-NC 4.0)**.

Puedes:

- Estudiar gratuitamente con las preguntas.
- Descargar, copiar y compartir el banco para fines no comerciales.
- Adaptar el formato para uso personal, educativo gratuito o comunitario no comercial.
- Corregir, mejorar o reutilizar preguntas si mantienes la atribución y la misma condición no comercial.

No puedes, sin autorización previa:

- Vender las preguntas o recopilaciones que las contengan.
- Usarlas en cursos, academias, preparaciones, aplicaciones, plataformas o servicios de pago.
- Monetizarlas mediante publicidad, patrocinios, afiliación, suscripciones o captación comercial.
- Presentarlas como propias o eliminar la atribución.
- Usarlas para entrenar, desarrollar o mejorar productos o servicios comerciales, incluidos sistemas de inteligencia artificial.

El resumen anterior no sustituye al aviso completo de licencia incluido más abajo.

## Visor web

Este repositorio incluye un visor estático de bancos de preguntas. Puede publicarse directamente con GitHub Pages porque no necesita base de datos ni backend: el navegador carga `index.html`, lee `preguntas/manifest.json` y descarga los CSV de `preguntas/` bajo demanda.

### Ejecutar en local

En Windows:

```bat
start_viewer.bat
```

En macOS o Linux:

```sh
./start_viewer.sh
```

También puede ejecutarse directamente con Python:

```sh
python server.py
```

El servidor local se abre en `http://127.0.0.1:8000` y sirve `preguntas/manifest.json` dinámicamente, por lo que permite añadir o quitar CSV durante el trabajo local y recargar la página.

La versión pública permite seleccionar bancos y buscar texto. Los filtros por artículo, dificultad, familia y tipo quedan reservados para la versión premium enlazada desde el visor.

### Añadir preguntas

1. Copia los nuevos archivos `.csv` dentro de `preguntas/`.
2. Si vas a publicarlo en GitHub Pages, actualiza `preguntas/manifest.json` para incluir los nuevos CSV.
3. Sube los cambios al repositorio.

### Jerarquía por carpetas

El visor deduce la jerarquía del banco a partir de las carpetas dentro de `preguntas/` y del nombre del archivo CSV.

Por ejemplo:

```text
preguntas/
  CE/
    preliminar_banco_180_editorial_v2.csv
    titulo_i_banco_628_editorial_v2.csv
  EACV/
    titulo_i_banco_168.csv
  Ley 5 1983 Consell/
    bloque_a_banco_880.csv
```

Se mostrará como:

```text
CE / Preliminar
CE / Titulo I
EACV / Titulo I
Ley 5 1983 Consell / Bloque A
```

En el selector del visor, las carpetas con varios bancos aparecen como opciones padre. Si seleccionas `CE (todos)`, se cargan todos los bancos que cuelgan de `preguntas/CE/`.

El nombre del archivo se interpreta hasta `_banco`; lo que aparece después se considera parte técnica del archivo. Si un archivo necesita más niveles internos, puede usar `__` dentro del nombre, por ejemplo `titulo_preliminar__capitulos_i_ii_banco_352.csv`.

Si quieres forzar un nombre distinto sin cambiar el archivo, añade una propiedad `title` a su entrada en `preguntas/manifest.json`. Si quieres forzar la jerarquía, añade `hierarchy` como lista de textos.

Cada CSV debe incluir columnas equivalentes a `statement`, `option_a`, `option_b`, `option_c`, `option_d` y `correct_option`. El visor también reconoce alias en castellano como `enunciado`, `opcion_a`, `respuesta_correcta`, `explicacion`, `articulo`, `dificultad`, `familia` y `tipo`.

### Publicación en GitHub Pages

Para publicarlo sin consumo de servidor, activa GitHub Pages desde la rama principal y la carpeta raíz del repositorio. GitHub servirá archivos estáticos, por lo que el coste computacional del servidor es nulo más allá del alojamiento estático que proporciona GitHub Pages.

## Aviso de licencia y condiciones de uso

© 2026 Ivan Barreda Prades

Salvo que se indique expresamente lo contrario, las preguntas originales, respuestas, explicaciones, comentarios, clasificaciones y la selección y organización del banco de preguntas de este proyecto se ofrecen bajo la licencia **Creative Commons Atribución–NoComercial 4.0 Internacional — CC BY-NC 4.0**.

Esta licencia permite copiar, compartir, adaptar y reutilizar el contenido para fines no comerciales, siempre que se cumplan las siguientes condiciones:

1. Se reconozca adecuadamente la autoría de **Ivan Barreda Prades**.
2. Se incluya una referencia a la licencia CC BY-NC 4.0.
3. Se indique claramente si el contenido ha sido modificado.
4. El uso no tenga como finalidad principal obtener ingresos, una ventaja comercial o una compensación económica.

## Usos permitidos

A título orientativo, se permite:

- Estudiar gratuitamente con las preguntas de manera individual.
- Descargar o imprimir preguntas para uso personal.
- Compartir gratuitamente preguntas concretas con otros opositores.
- Crear un grupo de estudio gratuito utilizando las preguntas.
- Utilizar las preguntas en una asociación o comunidad de estudiantes sin ánimo de lucro, siempre que no se cobre por el acceso al contenido.
- Crear simulacros, resúmenes, fichas de estudio o selecciones de preguntas para uso personal o no comercial.
- Adaptar el formato de las preguntas para facilitar su estudio, por ejemplo, incorporándolas a tarjetas de memoria, documentos, hojas de cálculo o aplicaciones de uso personal.
- Publicar gratuitamente una selección limitada de preguntas en una página o repositorio no monetizado, siempre que se reconozca la autoría y se respeten las demás condiciones de la licencia.
- Corregir o mejorar una pregunta, siempre que se indique que ha sido modificada y que su reutilización siga siendo no comercial.

## Usos no permitidos sin autorización

No está permitido, salvo autorización previa y por escrito de **Ivan Barreda Prades**:

- Vender las preguntas, sus explicaciones o cualquier recopilación que las contenga.
- Incluir las preguntas en un libro, manual, temario o publicación que se venda.
- Utilizarlas en cursos, clases, tutorías, preparaciones o formaciones de pago.
- Utilizarlas por parte de una academia, preparador, editorial o empresa como parte de sus servicios profesionales o comerciales.
- Incorporarlas a una aplicación, página web o plataforma que cobre una suscripción, matrícula, cuota o pago por acceso.
- Incorporarlas a una aplicación o página web monetizada mediante publicidad, patrocinios, contenidos promocionales, enlaces de afiliación o venta de datos.
- Ofrecer las preguntas gratuitamente como reclamo para vender cursos, servicios, temarios, suscripciones u otros productos.
- Utilizarlas para captar clientes, alumnos, suscriptores o contactos comerciales.
- Revender, sublicenciar o conceder acceso de pago a una copia o adaptación del banco de preguntas.
- Imprimirlas y distribuirlas cobrando una cantidad superior al coste estrictamente necesario de impresión y entrega.
- Eliminar el nombre del autor, el aviso de licencia o cualquier indicación sobre el origen del contenido.
- Presentar las preguntas como propias o insinuar que Ivan Barreda Prades respalda, colabora o mantiene alguna relación con el usuario.
- Utilizarlas para entrenar, desarrollar o mejorar un producto o servicio comercial, incluidos sistemas automatizados o de inteligencia artificial, sin autorización expresa.

El hecho de que el acceso directo a las preguntas sea gratuito no convierte automáticamente el uso en no comercial cuando las preguntas contribuyen a generar ingresos, publicidad, clientes o cualquier otra ventaja empresarial.

## Usos que requieren consulta previa

Deberá solicitarse autorización previa para:

- Páginas, aplicaciones o canales que reciban ingresos por publicidad, patrocinios o afiliación.
- Proyectos financiados mediante donaciones periódicas, micromecenazgo o cuotas de socios.
- Asociaciones, fundaciones u organizaciones que cobren por actividades relacionadas con las oposiciones.
- Centros educativos o entidades públicas que encarguen el servicio a una empresa privada.
- Empresas que quieran utilizar las preguntas para la formación interna de sus empleados.
- Plataformas gratuitas vinculadas a una academia, editorial, preparador o negocio.
- Aplicaciones gratuitas que incluyan compras, servicios premium o funciones de pago.

La autorización será necesaria aunque no se cobre directamente por cada pregunta cuando el uso forme parte de una actividad destinada principalmente a obtener una ventaja comercial o una compensación económica.

## Licencias comerciales

Ivan Barreda Prades podrá conceder licencias comerciales independientes para academias, editoriales, preparadores, aplicaciones, páginas web, empresas u otras organizaciones.

La concesión de una licencia comercial a una persona o entidad no implica que se conceda el mismo permiso al resto de usuarios.

Para solicitar autorización o una licencia comercial:

- **Titular:** Ivan Barreda Prades
- **Correo electrónico:** i.barreda@gmail.com

## Contenidos no incluidos

Esta licencia se aplica exclusivamente a los contenidos originales cuyos derechos pertenezcan a Ivan Barreda Prades.

No se aplica, salvo indicación expresa, a:

- Preguntas o materiales pertenecientes a terceros.
- Preguntas reproducidas de exámenes oficiales.
- Textos legales, reglamentos, disposiciones administrativas o fragmentos normativos reproducidos como referencia.
- Imágenes, logotipos, marcas o elementos gráficos pertenecientes a terceros.
- El código fuente, diseño técnico o funcionamiento de la página web o aplicación.
- El nombre comercial, dominio, logotipo y demás elementos de identidad del proyecto.

Cada contenido de terceros conservará su licencia, condiciones de uso y atribución correspondientes.

## Carácter orientativo de los ejemplos

Los ejemplos anteriores tienen una finalidad aclaratoria y no constituyen una lista completa o exhaustiva.

Un uso no mencionado expresamente no debe considerarse automáticamente permitido. En caso de duda sobre si una actividad tiene carácter comercial, deberá solicitarse autorización previa a Ivan Barreda Prades mediante el correo electrónico **i.barreda@gmail.com**.

Estos ejemplos no sustituyen ni modifican el texto oficial de la licencia Creative Commons Atribución–NoComercial 4.0 Internacional. En caso de contradicción, prevalecerán el texto oficial de la licencia y la legislación aplicable.
