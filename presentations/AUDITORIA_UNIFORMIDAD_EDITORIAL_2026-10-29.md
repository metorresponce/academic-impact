# Auditoría de uniformidad editorial — Presentaciones académicas Canva

**Fecha:** 29 de octubre de 2026  
**Repositorio:** `metorresponce/academic-impact`  
**Alcance:** 21 artículos con texto completo; 42 diseños Canva definitivos (ES/EN).  
**Excluido:** artículo pendiente de publicación y sus dos borradores.

## Resultado ejecutivo

**No existe actualmente una norma homogénea de titulación de portadas.** Se verificaron las primeras diapositivas de las 42 presentaciones directamente mediante Canva y se contrastaron con los 21 títulos del manifiesto y los README. Se observan cuatro prácticas distintas:

1. Título original en ambos idiomas, con subtítulo o título adaptado traducido (ej.: CRA).
2. Título bibliográfico original en un encabezado secundario, acompañado de título expositivo adaptado (cinco pares de la tanda V4).
3. Título principal traducido o abreviado sin distinguirlo explícitamente del título académico oficial (patrón frecuente en V3/V5/V6).
4. Título reformulado en ambos idiomas, incluso cuando el título bibliográfico original contiene matices jurídicos o clínicos que la abreviación omite.

**Importante:** traducir un título no es necesariamente incorrecto. El problema es que se presenta indistintamente una traducción, un resumen editorial o el título original, sin señalización ni criterio fijo.

## Hallazgos por prioridad

### P1 — Identidad bibliográfica y precisión conceptual

- **Creaciones con Inteligencia Artificial** (DOI `10.5281/zenodo.17575998`): la portada inglesa usa «AI-Generated Works: Ownership and Regulatory Proposals». «Generated» estrecha el alcance respecto de «creaciones *con* IA» y puede borrar la distinción entre obras asistidas y generadas, esencial al artículo.
- **The Thousand-Click Bureaucracy** (DOI `10.5281/zenodo.17873281`): la portada inglesa «Due Process in Digital Government» no conserva la tesis identificadora «The erosion of due process in digital administration». La española también la reformula.
- **Overdiagnosis by Information Overload** (DOI `10.5281/zenodo.18208838`): la portada inglesa sustituye «health anxiety» por «anxiety» y «the clinical visit as a validation encounter» por «clinical visits for validation». Conserva el tema pero pierde especificidad.
- **Detecting Is Not Understanding** (DOI `10.5281/zenodo.18463145`): las portadas reducen el título a un lema más corto y no reproducen la identificación académica completa («Functional, audiovisual, and legal analysis of the algorithmic mediation of human movement»).
- **Kubernetes/GitOps** (DOI `10.5281/zenodo.17350239`): «Kubernetes + GitOps — Change governance in the cloud-native era» es un nombre expositivo, no la traducción exacta del título publicado.
- **Contratos Informáticos** (DOI `10.5281/zenodo.17783388`): en la portada española se sustituye «depósito de código fuente» por «escrow»; la equivalencia puede explicarse en el cuerpo, pero debe preservarse la denominación académica.
- **CRA** (DOI `10.5281/zenodo.17479259`): el texto extraído de las portadas aparece «Open Source Under theCyber Resilience Act». Debe inspeccionarse visualmente el espacio entre «the» y «Cyber» antes de editar; podría ser una concatenación de cajas de texto del importador.
- **Child Health** (DOI `10.5281/zenodo.18528025`): en inglés se conserva el comienzo del título, pero «Changing social contexts» pasa al subtítulo con agregados («habits, movement and participation»). No debe confundirse con la denominación original del trabajo. La autoría de las tres investigadoras está preservada correctamente.

### P1 — Orden de autoría: README frente al artículo original

Las siguientes discrepancias fueron contrastadas con la primera página del PDF original, no solo con la portada de Canva:

| Trabajo | Orden en PDF original y portada Canva | Orden actualmente consignado en README | Acción recomendada |
|---|---|---|---|
| IA en Salud Mental | Sandra Susana Arroyo Giuliani; Mariano Enrique Torres Ponce | Mariano; Sandra | Alinear README al PDF |
| Digital Medicine in Health Emergencies | María Noel Arana; Mariano Enrique Torres Ponce | Mariano; María Noel | Alinear README al PDF |
| Overdiagnosis by Information Overload | María Noel Arana; Mariano Enrique Torres Ponce; Sandra Susana Arroyo Giuliani | Mariano; María Noel; Sandra | Alinear README al PDF |

**No debe «corregirse» el orden de Canva para hacerlo coincidir con el README actual:** en estos tres casos la portada de Canva coincide con la fuente original. Primero corresponde corregir las fichas bibliográficas si el PDF es la versión canónica.

### P2 — Idioma de rótulos y familias gráficas

- En las presentaciones inglesas V3 aparece el encabezado español «REVISIÓN ACADÉMICA · EN».
- Las versiones V4 mantienen en ambos idiomas el encabezado bilingüe «INVESTIGACIÓN / RESEARCH» y el distintivo «RESEARCHLIBRARY»; son convenciones gráficas distintas de las demás tandas.
- Algunas portadas conservan un título original como franja superior y una variante traducida como título principal, mientras otras no muestran el original. En algunas traducciones se omiten los calificativos originales de la obra.
- En V6 se usa «AUTORES / AUTHORS» incluso para trabajos de autor único. Debe variar según corresponda «AUTOR / AUTHOR».
- Las 42 presentaciones activas tienen de 12 a 14 diapositivas; esta diferencia no es por sí sola un error de rigor ni exige forzar un número fijo.

## Matriz de 21 artículos

| DOI (sufijo) | Diagnóstico principal en portadas | Prioridad |
|---|---|---|
| 18237585 | ES traducido; EN simplifica el subtítulo del título oficial | P2 |
| 17575262 | ES abreviado; EN traducción/adaptación sin título original completo | P2 |
| 17575998 | ES abreviado; EN introduce «AI-Generated» como reformulación del alcance | **P1** |
| 17508884 | Original español visible arriba en ambos; título expositivo traducido | P2: etiquetar |
| 17508689 | Original español visible arriba en ambos; título expositivo EN traducido | P2: etiquetar |
| 18463145 | Título y subtítulo abreviados en ambos idiomas | **P1** |
| 17423551 | EN muy próximo al original; ES traducción sin identificación como adaptación | P2 |
| 17297095 | Título abreviado en ES y EN; autoría en Canva conforme a PDF, no a README | **P1** |
| 17479259 | Original inglés retenido en ES; posible espacio perdido en `theCyber`; EN con rótulo en español | **P1/P2** |
| 17344639 | Dos portadas acortan el título original largo | P2 |
| 17278111 | Título original español visible arriba en ambos; EN adaptado | P2: etiquetar |
| 17873281 | Título reformulado: pérdida de «erosion of due process» | **P1** |
| 17350239 | Título oficial sustituido por «Kubernetes + GitOps» y subtítulos divulgativos | **P1** |
| 18208838 | Matices «health anxiety» y «validation encounter» abreviados; README difiere en orden autoral | **P1** |
| 17363577 | Título original inglés visible arriba en ambos; ES traducido | P2: etiquetar |
| 17625619 | ES traducido; EN omite «rise of transnational governance» | P2 |
| 17438436 | ES original completo; EN traducción editorial no diferenciada | P2 |
| 17506876 | Original inglés visible arriba; ES adaptado; README difiere en orden autoral | **P1** |
| 17783388 | ES «escrow» por «depósito de código fuente»; EN traducción | **P1** |
| 17735815 | ES abrevia «en seguridad de la información»; EN traducción | P2 |
| 18528025 | ES traducido; EN reformula el final del título; tres autoras correctamente preservadas | P2 |

## Estándar único propuesto (para aplicar en futuras versiones)

**Identidad del trabajo, independiente del idioma de la diapositiva:**

1. **Título bibliográfico original, íntegro y literal:** debe aparecer en la portada (si es muy largo, en una línea secundaria con tipografía legible). Nunca tratar una reformulación como si fuera el título oficial.
2. **Título expositivo localizado:** una variante más breve en el idioma de la presentación puede funcionar como título visual grande, pero rotulada explícitamente «Título de la presentación» / «Presentation title», o «Adaptación del título» / «Adapted title».
3. **Subtítulo:** traducido al idioma de la presentación si es explicativo; no cambiar términos doctrinales esenciales. Para traducciones de terminología jurídica preferir precisión a brevedad.
4. **Autores y orden:** copiar exactamente el orden publicado en el PDF; diferenciación entre coautoría, coordinación y revisión académica. Singular/plural correcto.
5. **Idioma de interfaz:** todos los rótulos y pies en ES para README.ES.md y en EN para README.md; términos técnicos y títulos de fuentes conservan su forma pertinente.
6. **Identificadores:** DOI siempre visible y enlazable; año y título original coincidentes con la ficha y el artículo. No añadir fechas de publicación inventadas.
7. **Cierre y trazabilidad:** última diapositiva con título bibliográfico íntegro, autores, DOI, fuente y descripción de los límites de la adaptación.
8. **Control técnico:** no alterar el número de diapositivas de forma automática; priorizar legibilidad y fidelidad. Revisar cada importación tras el cambio.
9. **Enlaces:** mantener identificadores y URLs actuales hasta verificar nuevas versiones Canva; GitHub se cambia solo después de la inspección del contenido y la importación.
10. **Acceso:** la verificación DOI/Canva no garantiza lectura pública sin iniciar sesión. Debe existir un QA de permisos independiente.

## Alcance de esta auditoría y próximos cambios

**Verificado:** texto de la diapositiva de portada de las 42 versiones definitivas; identidad y correspondencia DOI/README; primeras páginas originales de IA en Salud Mental, Digital Medicine, Overdiagnosis, Detecting y U.S. Healthcare; estructura del manifiesto.

**No realizado en esta auditoría:** edición de las diapositivas, inspección visual individual de todas las portadas ni revisión lingüística integral de los textos de las 42 presentaciones. No se deben anunciar esas tareas como completadas.

**Orden de corrección recomendado:** (1) autoría bibliográfica en README según PDF; (2) títulos que modifican el significado; (3) reproducción de título original en todas las portadas; (4) rótulos e idioma uniforme; (5) revisión visual y actualizaciones de enlaces con control de versiones.
