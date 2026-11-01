# Verificación de acceso anónimo a presentaciones V7

Fecha: 1 de noviembre de 2026 (Europe/Madrid).

## Resultado

Se abrieron individualmente las 42 URL V7 vigentes, en un navegador Chrome remoto sin iniciar sesión en Canva durante la prueba. Las 42 redirigieron a `https://www.canva.com/login/` y mostraron **“Log in or sign up in seconds”**, sin mostrar la presentación.

| Clasificación | Cantidad |
| --- | ---: |
| Acceso anónimo confirmado | 0 |
| Autenticación exigida en el navegador de prueba | 42 |
| Apertura sin resultado concluyente | 0 |
| Permisos efectivos de solo lectura confirmados | 0 |

La exigencia de autenticación describe la conducta observada de estas URL en este navegador y fecha. No demuestra que los diseños hayan sido eliminados ni permite inferir sus permisos internos, la causa de la redirección o el comportamiento en todos los navegadores. Los permisos efectivos de visualización siguen **sin verificar** porque no se llegó al visor. No se hizo una auditoría visual del contenido de las diapositivas.

## Método y evidencia

- Fuente del inventario: `canva-manifest.json`, blob `b57e4ce2d1b0d8a79f41cbcb46624b07f7c1f9fe`.
- Se contrastaron las 44 asociaciones DOI/idioma/URL del manifiesto con sus secciones en README.ES.md y README.md: sin discrepancias. Las dos del artículo pendiente se excluyeron de la navegación V7.
- Navegación directa a cada URL exacta del README; observación del DOM y del destino de navegación. No se introdujeron credenciales ni se inició sesión. Se rechazaron las cookies opcionales.
- Evidencia común observada individualmente para cada fila: destino `https://www.canva.com/login/` y encabezado **“Log in or sign up in seconds”**. No se conservan parámetros de redirección con tokens temporales.
- La herramienta de consulta web no pudo abrir los dos primeros enlaces. Esos errores no se utilizaron para clasificar accesos; la clasificación procede de la navegación posterior y la pantalla observada.
- Como comprobación adicional, Canva `get_design` devolvió para `DAHZbIxamho` el enlace de visualización `https://www.canva.com/d/ApWTpJ3xvZ-DUzW`. También se abrió sin iniciar sesión y redirigió a la misma pantalla. Se comprobó solo esta alternativa; no se presume el comportamiento de otras URL alternativas.

## Registro por DOI e idioma

En todas las filas, **Autenticación requerida** significa redirección observada al login; **Sin verificar** corresponde a los permisos efectivos de solo lectura.

| DOI | Idioma | Diseño V7 conservado | URL comprobada | Apertura anónima | Solo lectura |
| --- | --- | --- | --- | --- | --- |
| 10.5281/zenodo.18237585 | ES | `DAHZbIxamho` | [Enlace](https://www.canva.com/d/gmCKYmr6dGYmrN0) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.18237585 | EN | `DAHZbB_jcAo` | [Enlace](https://www.canva.com/d/QMgAZ7QLehb0R6H) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17575262 | ES | `DAHZbJpejVs` | [Enlace](https://www.canva.com/d/ABM-6Nm-GNuu03L) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17575262 | EN | `DAHZbClxJdc` | [Enlace](https://www.canva.com/d/jhGw-Ty63lDEidE) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17575998 | ES | `DAHZbJ4zb6c` | [Enlace](https://www.canva.com/d/RKfH8puppRH8_g_) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17575998 | EN | `DAHZbP8GPHo` | [Enlace](https://www.canva.com/d/0t7T-V-dp0u5xS1) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17508884 | ES | `DAHZbCER6t0` | [Enlace](https://www.canva.com/d/3j8pt6Poc8bxKUb) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17508884 | EN | `DAHZbGsULz4` | [Enlace](https://www.canva.com/d/B2410Svs1YuBHCA) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17508689 | ES | `DAHZbMfCPRA` | [Enlace](https://www.canva.com/d/eNM0t_OaAcVHuzM) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17508689 | EN | `DAHZbXGCYVg` | [Enlace](https://www.canva.com/d/DxqWJZvevcv_tgq) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.18463145 | ES | `DAHZbKu8-Xo` | [Enlace](https://www.canva.com/d/CB92MbtQNIRldTU) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.18463145 | EN | `DAHZbdQZx_g` | [Enlace](https://www.canva.com/d/AD3ri9bsK8ifFJs) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17423551 | ES | `DAHZba2B-OA` | [Enlace](https://www.canva.com/d/xw5Vwd2fAfqDsdU) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17423551 | EN | `DAHZbWpWWw4` | [Enlace](https://www.canva.com/d/phHbrtwdL7qIZ6o) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17297095 | ES | `DAHZbdvB4Ls` | [Enlace](https://www.canva.com/d/lF5dag8LYHGJ4n_) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17297095 | EN | `DAHZbbtGiec` | [Enlace](https://www.canva.com/d/Bx85Tzg-ivNQR1p) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17479259 | ES | `DAHZbR1QmMY` | [Enlace](https://www.canva.com/d/eTJoDVZzmomzgTc) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17479259 | EN | `DAHZbbP5268` | [Enlace](https://www.canva.com/d/aOybwk4r6_snFSN) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17344639 | ES | `DAHZbcm2Guk` | [Enlace](https://www.canva.com/d/Ptz2Jj_OZspP_6W) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17344639 | EN | `DAHZbZMf5jE` | [Enlace](https://www.canva.com/d/DwL8kFQRw8Lj4tg) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17278111 | ES | `DAHZbcr6RK0` | [Enlace](https://www.canva.com/d/ljoP01ncD11TakK) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17278111 | EN | `DAHZbbe1TPY` | [Enlace](https://www.canva.com/d/CeaV4GJJE31fpxA) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17873281 | ES | `DAHZbRFSDgc` | [Enlace](https://www.canva.com/d/c8qKPoq8LlQMyjC) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17873281 | EN | `DAHZbUZ1DjI` | [Enlace](https://www.canva.com/d/uz2V7q45gTUnt1k) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17350239 | ES | `DAHZbR8gd-Q` | [Enlace](https://www.canva.com/d/BSjbWOE8yuUuunt) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17350239 | EN | `DAHZbZp99F8` | [Enlace](https://www.canva.com/d/nuYUqB1u5xEnzVg) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.18208838 | ES | `DAHZbVIEAJc` | [Enlace](https://www.canva.com/d/mSsMStlLvKuiu5T) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.18208838 | EN | `DAHZbXgvBLs` | [Enlace](https://www.canva.com/d/TqPIYxkPBRjXMmh) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17363577 | ES | `DAHZbUOoXjY` | [Enlace](https://www.canva.com/d/qQwhXKxSLr7h_qk) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17363577 | EN | `DAHZbQETq2c` | [Enlace](https://www.canva.com/d/8udojP4PF9AHhqo) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17625619 | ES | `DAHZbVQuMZo` | [Enlace](https://www.canva.com/d/Cv0Paa09bwvrjht) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17625619 | EN | `DAHZbebHZ5I` | [Enlace](https://www.canva.com/d/IcawV4W625kAd_o) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17438436 | ES | `DAHZbZMeImo` | [Enlace](https://www.canva.com/d/tN2OvAlOqn0ahMy) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17438436 | EN | `DAHZbTGuji0` | [Enlace](https://www.canva.com/d/TooNB8WWHj-awee) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17506876 | ES | `DAHZbc8niKk` | [Enlace](https://www.canva.com/d/E6RP9zqv9_vNs03) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17506876 | EN | `DAHZbS_t0UI` | [Enlace](https://www.canva.com/d/yilnLh9JH7kQUhn) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17783388 | ES | `DAHZbe0Ekck` | [Enlace](https://www.canva.com/d/UhU2j7MhBMMDvdc) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17783388 | EN | `DAHZbcXUk10` | [Enlace](https://www.canva.com/d/rJ1a8Tu5f6XB9Es) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17735815 | ES | `DAHZbSRHBlM` | [Enlace](https://www.canva.com/d/iFaGd7yG7TypuOE) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.17735815 | EN | `DAHZbXiqJx0` | [Enlace](https://www.canva.com/d/TANtGeo4YQfYsxX) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.18528025 | ES | `DAHZbXRw3U4` | [Enlace](https://www.canva.com/d/g0-GtgAc3vTUfQb) | Autenticación requerida | Sin verificar |
| 10.5281/zenodo.18528025 | EN | `DAHZbbdNVsY` | [Enlace](https://www.canva.com/d/DwzJ6KY3LE06SYs) | Autenticación requerida | Sin verificar |

## Alcance de los cambios y limitación pendiente

Se actualiza `public_anonymous_access` a `authentication_required` exclusivamente en las 42 ediciones publicadas V7, con evidencia fechada por edición. Este valor identifica la pantalla observada; no certifica ni modifica la configuración interna de Canva. Se añade `view_only_permissions: "unverified"` dentro del registro de evidencia para evitar confundir ambas comprobaciones.

Se mantienen intactos los enlaces de los README y del manifiesto, los IDs de los 42 diseños, las versiones históricas y todos los datos bibliográficos. No se dispone de un destino público válido y comprobado para sustituir enlaces. No se cambian permisos ni se crean o reemplazan diseños.

El DOI `10.7238/idp.v0i46.980000013974` conserva `pending_publication`, sus dos borradores `DAHZWVO166I` (ES) y `DAHZWVW6nlE` (EN), y sus estados de acceso `unverified`. No se evaluó de nuevo su publicación ni se incorporaron como presentaciones definitivas.

Para completar la comprobación de permisos se necesita un enlace de visualización que llegue al visor sin login, o inspeccionar la configuración de compartir desde una sesión autorizada de Canva y después volver a probar el enlace sin sesión. El conector disponible devuelve metadatos y enlaces desde la cuenta conectada; no expone una operación para inspeccionar o modificar los permisos de compartir. Un enlace devuelto por ese conector no constituye por sí solo evidencia de acceso público. Esta auditoría no solicitó ni realizó cambios de permisos.
