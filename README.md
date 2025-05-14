# Simulador Educativo de Física

## Índice

- **RESUMEN.**
- **ESPECIFICACIÓN DE REQUISITOS DEL SOFTWARE.**
  - Introducción.
  - Descripción general.
  - Requisitos específicos.
  - Casos de uso.
  - Restricciones.
- **DISEÑO DE ARQUITECTURA DEL SOFTWARE.**
  - Introducción.
  - Diagrama de arquitectura.
  - Descripción de componentes y sus interfaces.
  - Patrones de diseño y vista gráfica.
  - Resultados de diseño.
- **DISEÑO DETALLADO DEL SOFTWARE.**
  - Diseño arquitectónico.
  - Descripción de la descomposición.
  - Fundamento del diseño.
  - Descripción general de la interfaz de usuario.
  - Matriz de requisitos.
  - Diagrama de clases.
  - Estructura de datos.
  - Interfaces de los componentes.
- **MANUAL DE USUARIO.**
  - Guía de instalación.
  - Guía de uso.
  - Preguntas frecuentes.
  - Solución de problemas comunes.
- **MANUAL DE MANTENIMIENTO.**
  - Procedimientos de mantenimiento.
  - Plan de actualizaciones.
  - Manejo de errores.
  - Copias de seguridad y recuperación.
  - Consideraciones especiales.
- **PLAN DE GESTIÓN DE CONFIGURACIÓN.**
  - Gestión de configuración del software.
- **PLAN DE GESTIÓN DEL PROYECTO.**
  - Introducción.
  - Planificación del cronograma.
  - Gestión de riesgo.
  - Gestión de calidad.
- **DOCUMENTACIÓN DE PRUEBAS.**
  - Propósito.
  - Alcance.
  - Estrategia de pruebas.
  - Estrategia de ejecución.
  - Requisitos ambientales.
- **GUÍA DE IMPLEMENTACIÓN.**
  - Requisitos del sistema.
  - Descarga y configuración.
  - Ejecución del simulador.
  - Interacción con el simulador.
  - Problemas comunes y soluciones.
- **DOCUMENTACIÓN DE LA API.**
- **REFERENCIAS.**

## Resumen

Este proyecto presenta el desarrollo de un simulador educativo enfocado en la enseñanza de conceptos fundamentales de Física, específicamente en las temáticas de **cuerpos en equilibrio** y **tiro parabólico**, dirigido a estudiantes y docentes de nivel bachillerato. La iniciativa surge ante las dificultades que enfrentan los alumnos para comprender estos temas debido a la falta de herramientas interactivas y la limitada conectividad a internet en algunos entornos. Este simulador, que no requiere conexión a internet, busca facilitar un aprendizaje práctico y dinámico, permitiendo a los estudiantes explorar y entender conceptos a su propio ritmo.

El sistema tiene como objetivo principal proporcionar una herramienta interactiva que apoye a los estudiantes y docentes en la comprensión de la **primera condición de equilibrio** y el **tiro parabólico** mediante simulaciones que representen de manera visual y práctica los principios físicos involucrados.


## Especificación de Requisitos del Software

### Introducción

**Propósito**

El propósito de este documento es especificar los requisitos para un simulador educativo diseñado para ayudar a los estudiantes de bachillerato a comprender la **primera condición de equilibrio** en Física 1. Este simulador será una herramienta interactiva que permitirá a los usuarios explorar conceptos de manera práctica y dinámica, así como comprobar resultados de ejercicios sobre este tema.

**Convenciones del Documento**

Este documento sigue normas tipográficas específicas para garantizar claridad y consistencia. Los títulos y subtítulos están destacados por puntos, y cada requisito tiene su propia prioridad claramente indicada.

**Público al que va Dirigido**

- **Desarrolladores**: Necesitan entender los requisitos funcionales y no funcionales del simulador.
- **Usuarios Finales (Estudiantes)**: Interesados en cómo el simulador puede facilitar su aprendizaje.
- **Evaluadores**: Encargados de valorar la usabilidad y efectividad del simulador.

**Sugerencias de Lectura**

Leer primero la sección de introducción, luego la descripción general, y finalmente las secciones específicas según el interés.

### Ámbito del Sistema

El simulador tiene como objetivo proporcionar una herramienta interactiva que permita a los estudiantes y docentes explorar y comprender los temas de la **primera condición de equilibrio** y el **tiro parabólico** en Física 1.

### Funcionalidades del Sistema

- **Simulación Interactiva**: Permite a los usuarios manipular objetos físicos virtuales para observar simulaciones.
- **Visualización de Resultados**: Ofrece gráficos y retroalimentación inmediata sobre el estado del sistema simulado.
- **Accesibilidad Offline**: No requiere conexión a internet, facilitando su uso en cualquier momento y lugar.

**No Incluye**:

- Contenido avanzado más allá de la primera condición de equilibrio.
- Interacción en tiempo real con otros usuarios.

### Beneficios, Objetivos y Metas

**Beneficios**:

- Mejora en la comprensión conceptual al llevar la teoría a la práctica de manera virtual.
- Fomento del aprendizaje autónomo, permitiendo a los estudiantes explorar a su propio ritmo.

**Objetivos Específicos**:

- Identificar las características esenciales de un simulador a partir de la revisión de literatura y sitios académicos.
- Determinar las características del simulador según las necesidades.
- Diseñar e implementar un simulador de escritorio.

**Metas**:

- Evaluar la efectividad del simulador mediante encuestas de satisfacción y usabilidad.

### Definiciones, Acrónimos y Abreviaturas

- **Simulador Educativo**: Herramienta digital diseñada para replicar virtualmente un fenómeno o proceso específico, fomentando la comprensión a través de la práctica.
- **CSUQ**: Cuestionario de usabilidad del sistema, utilizado para medir la satisfacción y usabilidad.
- **Python**: Lenguaje de programación versátil utilizado en el desarrollo del simulador.
- **Pygame**: Biblioteca de Python para gráficos y simulaciones.
- **Matplotlib**: Biblioteca de Python para visualización de datos en gráficos 2D.
- **Tkinter Canvas**: Herramienta para crear gráficos vectoriales 2D.
- **Diagrama de Cuerpo Libre**: Representación gráfica de las fuerzas actuantes sobre un cuerpo en equilibrio.
- **Primera Condición de Equilibrio**: La suma vectorial de todas las fuerzas sobre un cuerpo es cero.
- **Tiro Parabólico**: Movimiento de un objeto lanzado con una velocidad inicial en un ángulo, bajo la influencia de la gravedad.

### Descripción General

**Perspectiva del Producto**

El simulador es una herramienta independiente que se integra en el ámbito educativo, específicamente en la enseñanza de la física. No depende de otras herramientas digitales y está diseñado para operar de manera autónoma en computadoras personales.

### Funciones del Producto

- **Simulación Interactiva**: Manipulación de objetos virtuales para observar efectos.
- **Visualización Gráfica**: Gráficos que ilustran fuerzas, tensiones y trayectorias.
- **Retroalimentación Inmediata**: Resultados instantáneos para identificar errores.
- **Configuración Personalizada**: Ajuste de parámetros como peso, ángulo y velocidad.

### Características de los Usuarios

**Usuarios Principales**: Estudiantes y docentes de bachillerato.

**Requisitos**:

- Conocimientos básicos de física (fuerzas, vectores, movimiento).
- Habilidades tecnológicas mínimas para interactuar con software educativo.

**Frecuencia de Uso**: Diaria durante sesiones de clase.

### Entorno Operativo

- **Plataforma de Hardware**: Computadoras personales estándar.
- **Sistema Operativo**: Compatible con Windows.
- **Componentes Adicionales**: Bibliotecas Pygame y Matplotlib incluidas.

### Suposiciones y Dependencias

- Acceso a computadoras personales en casa o en la escuela.
- Conocimientos básicos de física por parte de los estudiantes.
- Acompañamiento docente durante las primeras sesiones.
- Apoyo del entorno escolar para el uso de recursos digitales.

### Documentación del Usuario

- **Manual del Usuario**: Instrucciones detalladas sobre el uso del simulador.

### Interfaces de Usuario

- **Diseño Intuitivo**: Interfaz fácil de usar con botones claramente etiquetados.
- **Menú**: Opciones para la interfaz inicial y el simulador.

### Interfaces de Software

- **Bases de Datos**: No requiere bases de datos externas.
- **Herramientas Integradas**: Pygame, Matplotlib y Canvas.

### Requisitos Específicos

**Requisitos Funcionales**:

- Simulación interactiva para manipular objetos virtuales.
- Visualización de gráficos (vectores de fuerza, trayectorias).
- Retroalimentación inmediata para identificar errores.
- Configuración personalizada de parámetros.
- Interfaz gráfica intuitiva.

**Requisitos No Funcionales**:

- **Usabilidad**: Intuitivo y fácil de usar sin formación previa.
- **Rendimiento**: Respuesta en menos de un segundo.
- **Compatibilidad**: Funciona en computadoras estándar.
- **Accesibilidad Offline**: Completamente funcional sin internet.
- **Mantenibilidad**: Código documentado y estructurado.
- **Escalabilidad**: Permite incorporar nuevos temas sin reestructuración.

## Casos de Uso

### Casos de Uso - Cuerpos en Equilibrio

**Caso 1: Iniciar el Simulador**

- **Actor Principal**: Usuario
- **Descripción**: El usuario inicia el simulador.
- **Precondiciones**: Sistema encendido, simulador instalado.
- **Flujo Normal**:
  - Ejecuta el simulador.
  - Carga recursos gráficos (imágenes, poleas, cuerdas).
  - Muestra la interfaz gráfica inicial.
- **Postcondiciones**: Escena inicial lista para interacción.
- **Flujo Alternativo**: Muestra mensaje de error si falta un recurso.

**Caso 2: Arrastrar el Cuerpo**

- **Actor Principal**: Usuario
- **Descripción**: El usuario arrastra el cuerpo con el ratón.
- **Precondiciones**: Simulador en ejecución, escena visible.
- **Flujo Normal**:
  - Clic en el cuerpo (imagen del peso).
  - Rastrea el movimiento del ratón.
  - Actualiza la posición del cuerpo en tiempo real.
- **Postcondiciones**: Cuerpo reposicionado.
- **Flujo Alternativo**: No activa arrastre si el clic es fuera del cuerpo.

**Caso 3: Ajustar Ángulos de Poleas**

- **Actor Principal**: Usuario
- **Descripción**: Ajusta ángulos de poleas con el teclado.
- **Precondiciones**: Simulador en ejecución, escena visible.
- **Flujo Normal**:
  - Usa teclas de flechas para ajustar ángulos.
  - Recalcula tensiones y actualiza la interfaz.
- **Postcondiciones**: Ángulos y tensiones visualizados.
- **Flujo Alternativo**: No permite ajustes si se alcanza el límite.

**Caso 4: Conversor de Masa a Newtons**

- **Actor Principal**: Usuario
- **Descripción**: Usa el conversor de masa a newtons.
- **Precondiciones**: Simulador en ejecución.
- **Flujo Normal**:
  - Selecciona el botón de conversor.
  - Ingresa masa en kg y convierte a newtons.
  - Muestra el resultado.
- **Postcondiciones**: Resultado visible.
- **Flujo Alternativo**: Muestra error si el valor no es numérico.

**Caso 5: Generar Gráfico de Fuerzas**

- **Actor Principal**: Usuario
- **Descripción**: Genera un gráfico del sistema de fuerzas.
- **Precondiciones**: Simulador en ejecución.
- **Flujo Normal**:
  - Presiona el botón de graficar.
  - Calcula posiciones y tensiones.
  - Muestra el gráfico.
- **Postcondiciones**: Gráfico visible.
- **Flujo Alternativo**: Notifica error si falla la generación.

### Casos de Uso - Tiro Parabólico

**Caso 1: Iniciar el Simulador**

- **Actor Principal**: Usuario
- **Descripción**: Accede al menú principal para simular tiro parabólico.
- **Precondiciones**: Simulador instalado, conocimientos básicos de física.
- **Flujo Normal**:
  - Ejecuta el simulador.
  - Muestra menú principal con opciones.
  - Selecciona una opción.
- **Postcondiciones**: Menú principal visible.
- **Flujo Alternativo**: Muestra error si falta Pygame.

**Caso 2: Ajustar Ángulo de Lanzamiento**

- **Actor Principal**: Usuario
- **Descripción**: Ajusta el ángulo para observar la trayectoria.
- **Precondiciones**: Escenario de simulación activo.
- **Flujo Normal**:
  - Selecciona velocidad del proyectil.
  - Ajusta ángulo (0°-90°).
  - Actualiza trayectoria en tiempo real.
- **Postcondiciones**: Trayectoria y parámetros actualizados.
- **Flujo Alternativo**: Notifica error si el ángulo es inválido.

**Caso 3: Ingresar Velocidad Inicial**

- **Actor Principal**: Usuario
- **Descripción**: Ingresa velocidad inicial para observar la trayectoria.
- **Precondiciones**: Escenario de simulación activo.
- **Flujo Normal**:
  - Selecciona velocidad del proyectil.
  - Ingresa velocidad en m/s.
  - Recalcula y muestra trayectoria.
- **Postcondiciones**: Trayectoria y parámetros actualizados.
- **Flujo Alternativo**: Notifica error si el valor no es válido.

**Caso 4: Visualizar Gráfico de Trayectoria**

- **Actor Principal**: Usuario
- **Descripción**: Visualiza gráfico de la trayectoria parabólica.
- **Precondiciones**: Simulación activa con parámetros definidos.
- **Flujo Normal**:
  - Selecciona "Ver Trayectoria".
  - Muestra gráfico y parámetros (altura máxima, alcance).
- **Postcondiciones**: Gráfico visible.
- **Flujo Alternativo**: Notifica error si faltan datos.

**Caso 5: Calcular Parámetros Clave**

- **Actor Principal**: Usuario
- **Descripción**: Calcula alcance, altura máxima y tiempo de vuelo.
- **Precondiciones**: Simulación activa con parámetros configurados.
- **Flujo Normal**:
  - Calcula parámetros usando ecuaciones de tiro parabólico.
  - Muestra resultados en tabla.
  - Permite guardar resultados.
- **Postcondiciones**: Parámetros visibles.
- **Flujo Alternativo**: Notifica error si los parámetros son inválidos.

## Restricciones

- **Limitaciones de Hardware**: Compatible con computadoras estándar.
- **Acceso Offline**: Funciona sin conexión a internet.
- **Lenguaje de Programación**: Desarrollado en Python con Pygame y Matplotlib.
- **Interfaz de Usuario**: Accesible para usuarios con habilidades técnicas básicas.
- **Requisitos de Habilidad**: Conocimientos básicos de física.
- **Seguridad**: Medidas básicas para proteger la privacidad.
- **Criticalidad**: No debe fallar durante el uso en el aula.

## Diseño de Arquitectura del Software

### Introducción Arquitectura

**Propósito**

Proporcionar una descripción de la arquitectura del simulador, capturando decisiones clave para guiar el desarrollo.

**Ámbito de Aplicación**

Herramienta independiente para explorar conceptos físicos sin conexión a internet, proporcionando una experiencia interactiva.

### Diagrama de Arquitectura

El sistema se divide en tres capas:

**Cuerpos en Equilibrio**:

- **Capa de Lógica**:
  - **Simulador**: Calcula tensiones y posiciones.
  - **Funciones**: `calcular_tensiones()`, `calcular_posicion()`.
- **Capa de Acceso a Datos**:
  - **Gráficos**: Genera gráficos con Matplotlib.
  - **Componentes**: `crear_grafico()`.

**Tiro Parabólico**:

- **Capa de Presentación**:
  - **Interfaz Gráfica**: Ajusta parámetros y muestra trayectoria.
- **Capa de Lógica**:
  - Calcula componentes de velocidad, posición, alcance, altura máxima y tiempo de vuelo.
- **Capa de Acceso a Datos**:
  - Genera trayectoria y visualiza resultados.

### Descripción de Componentes y sus Interfaces

- **Interfaz Gráfica**:
  - Métodos para iniciar simulación y mostrar resultados.
- **Módulo de Cálculo**:
  - Recibe parámetros y devuelve resultados calculados.
- **Módulo Gráfico**:
  - Crea gráficos y devuelve posiciones de imágenes.

### Patrones de Diseño y Vista Gráfica

**Patrón MVC**:

- **Modelo**: Funciones de cálculo (`Solution`, `calculateTensions`, `calculateBodyPosition`).
- **Vista**: Funciones de dibujo (`drawScene`, `crearGrafico`).
- **Controlador**: Maneja eventos del usuario (clics, movimientos).

### Resultados de Diseño

- Simulación interactiva en tiempo real.
- Visualización gráfica inmediata.
- Interfaz intuitiva para usuarios sin experiencia técnica.

## Diseño Detallado del Software

El diseño detallado especifica los requisitos del simulador, siguiendo las mismas convenciones y público que la especificación de requisitos.

## Manual de Usuario

### Guía de Instalación

**Requisitos Previos**:

- No se requieren instalaciones adicionales (archivo portable).

**Descarga del Simulador**:

- Descargar desde: [https://carlosher6506.github.io/SitePerson/](https://carlosher6506.github.io/SitePerson/).

**Ejecutar el Simulador**:

- Guardar el archivo en una ubicación accesible.
- Hacer doble clic para iniciar.

### Guía de Uso

- Ejecutar el simulador con doble clic en el icono.
- Ajustar parámetros y observar resultados en tiempo real.

### Preguntas Frecuentes

- **¿Qué hago si no puedo iniciar el simulador?**
  - Verificar que el archivo y sus componentes estén completos.
- **¿Puedo usar el simulador sin internet?**
  - Sí, funciona completamente offline.
- **¿Cómo ajustar parámetros?**
  - Modificar parámetros directamente en la interfaz.
- **¿Qué hago si hay un error?**
  - Anotar el error y consultar la documentación.

### Solución de Problemas Comunes

- **El simulador no se abre**:
  - Verificar archivo y permisos.
  - Asegurar compatibilidad con el sistema operativo.
- **La simulación se congela**:
  - Reiniciar el simulador.
- **Gráficos no se generan**:
  - Verificar actualizaciones del sistema operativo.
- **Problemas de visualización**:
  - Asegurar que las imágenes estén en la carpeta correcta.

## Manual de Mantenimiento

### Procedimientos de Mantenimiento

- **Revisión Periódica**: Mensual, verificar recursos gráficos.
- **Actualización de Bibliotecas**:
  ```bash
  pip install --upgrade pygame matplotlib canvas math
  ```
- **Monitoreo de Errores**: Registrar fallos y analizar patrones.
- **Pruebas de Funcionalidad**: Ejecutar pruebas tras actualizaciones.

### Plan de Actualizaciones

- **Frecuencia**: Actualizaciones mayores cada 6 meses, menores según necesidad.
- **Registro de Cambios**: Documentar fechas, cambios y responsables.
- **Pruebas Post-Actualización**: Verificar funcionamiento tras cambios.

### Manejo de Errores

- Monitorear rendimiento y registrar errores.
- Usar mensajes claros para identificar problemas.

### Copias de Seguridad y Recuperación

- **Frecuencia**: Copias mensuales de archivos.
- **Método**: Usar GitHub para copias automáticas.
- **Proceso Git**:
  ```bash
  git add .
  git commit -m "Descripción del cambio"
  git pull
  git push
  ```

### Consideraciones Especiales

- **Recursos Gráficos**: Verificar rutas de imágenes.
- **Configuraciones Iniciales**: Mantener consistencia.
- **Funciones Matemáticas**: Revisar precisión.
- **Ciclo Principal**: Asegurar ejecución sin bloqueos.
- **Gestión Visual**: Comprobar visualizaciones correctas.

## Plan de Gestión de Configuración

**Control de Versiones**:

- Usar GitHub con esquema semántico:
  - **Principal**: 1.0.0 (nuevas funcionalidades).
  - **Secundaria**: 0.1.0 (mejoras menores).
  - **Parche**: 0.0.1 (correcciones rápidas).
- Documentar cambios en un registro.

**Control de Cambios**:

- Usar Solicitud de Cambio (CCR) con:
  - Descripción, justificación, impacto, recursos.
- Registrar cambios implementados.

**Gestión de Entornos**:

- Desarrollo, pruebas y producción con configuraciones específicas.

**Procedimientos Adicionales**:

- Formación del personal en control de versiones.
- Almacenar documentación en repositorio centralizado.

## Plan de Gestión del Proyecto

### Introducción Proyecto

Establece la estrategia para planificar, ejecutar y controlar el desarrollo del simulador.

**Objetivos**:

- Desarrollar funcionalidades interactivas.
- Asegurar usabilidad.
- Implementar en el aula y evaluar efectividad.

**Roles y Responsabilidades**:

- **Desarrolladores**: Programación y pruebas.
- **Diseñador UI/UX**: Interfaz y experiencia.
- **Evaluador**: Pruebas de usabilidad.

### Planificación del Cronograma

- **Análisis de Requerimientos** (1 día): Identificar necesidades.
- **Diseño** (1 semana): Prototipos en Figma.
- **Desarrollo** (3 semanas): Programación con Python.
- **Pruebas** (1 semana): Unitarias e integradas.
- **Implementación** (2 semanas): Despliegue y capacitación.
- **Evaluación Final** (1 día): Cuestionarios CSUQ.

### Gestión de Riesgo

- **Falta de Aceptación**: Pruebas tempranas con usuarios.
- **Retrasos**: Hitos claros y revisiones.
- **Problemas Técnicos**: Capacitación previa en herramientas.

### Gestión de Calidad

- Pruebas exhaustivas para identificar errores.

## Documentación de Pruebas

- Pendiente de desarrollo.

## Guía de Implementación

### Requisitos del Sistema

- **Sistema Operativo**: Windows 10 o superior.
- **Hardware**:
  - Procesador: Intel i3 mínimo.
  - RAM: 4 GB.
  - Espacio: 500 MB.

### Descarga y Configuración

- **Paso 1**: Descargar desde [https://carlosher6506.github.io/SitePerson/pages/simulador.html](https://carlosher6506.github.io/SitePerson/pages/simulador.html).
- **Paso 2**: Extraer archivos ZIP.
- **Paso 3 (Opcional)**: Instalar Python y bibliotecas:
  ```bash
  pip install pygame matplotlib canvas
  ```

### Ejecución del Simulador

- Hacer doble clic en `PHY-LABS.exe`.
- O ejecutar en terminal:
  ```bash
  python PHY-LABS.py
  ```

### Interacción con el Simulador

- Ajustar parámetros en la interfaz.
- Observar visualizaciones gráficas en tiempo real.
- Ver resultados instantáneos.

### Problemas Comunes y Soluciones

- **Error al Iniciar**: Verificar Python y bibliotecas.
- **Problemas Gráficos**: Actualizar controladores gráficos.
- **No Responde**: Cerrar aplicaciones pesadas y reiniciar.

## Documentación de la API

- Pendiente de desarrollo.

## Referencias

1. Beer, F.P, Johnston, E.R. (2017). *Vector Mechanics for Engineers: Statics*. McGraw-Hill Education.
2. Zacharia, Z. C., & Olympiou, G. (2011). Physical versus virtual manipulative experimentation in physics learning. *Learning and Instruction*, 21(3), 317-331. [https://doi.org/10.1016/j.learninstruc.2010.03.001](https://doi.org/10.1016/j.learninstruc.2010.03.001)
3. Rooney, D. (2022). The impact of simulation-based education on health professionals: A meta-analysis. *Medical Education and Practice*. [https://pmc.ncbi.nlm.nih.gov/articles/PMC11224887/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11224887/)
4. Thompson, L, Cooper, A. (2022). Enhancing remote learning through educational simulations in STEM. *International Journal of E-Learning and Distance Education*.
5. Abosede, A, Ramnarain, U. (2022). Teaching and learning physics using interactive simulation: A guided inquiry practice. [https://scielo.org.za/scielo.php?script=sci_arttext&pid=S0256-0100202000100003](https://scielo.org.za/scielo.php?script=sci_arttext&pid=S0256-0100202000100003)
6. Chanchí Golondrino, G. E, Gómez Álvarez, M. C, & Sierra Martínez, L. M. (2022). Directrices para el diseño y la construcción de videojuegos educativos. [https://revistas.upn.edu.co/index.php/RCE/article/view/12759](https://revistas.upn.edu.co/index.php/RCE/article/view/12759)
7. Gallegos Zurita, D. E, & Pavón, C. (2017). Diseño de un simulador educativo en MATLAB como soporte a la enseñanza de espejos cóncavos. [https://www.iiis.org/CDs2017/CD2017Summer/papers/CA373QX.pdf](https://www.iiis.org/CDs2017/CD2017Summer/papers/CA373QX.pdf)
8. PhET. (2024). Simulaciones interactivas PhET: Características de diseño. [https://phet.colorado.edu/es/inclusive-design](https://phet.colorado.edu/es/inclusive-design)
9. Educaplus. (2022). Simuladores y juegos de Física. [https://www.educaplus.org/games/fisica](https://www.educaplus.org/games/fisica)
10. Universidad Nacional Autónoma de México. (2013). Objetos de aprendizaje UNAM. [http://www.objetos.unam.mx/](http://www.objetos.unam.mx/)
11. Hedlefs Aguilar, M. I, de la Garza González, A, Sánchez Miranda, M. P, & Garza Villegas, A. A. (2017). Adaptación al español del Cuestionario de Usabilidad de Sistemas Informáticos (CSUQ).