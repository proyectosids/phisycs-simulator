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

Este proyecto presenta el desarrollo de un simulador educativo enfocado en la enseñanza de conceptos fundamentales de Física, específicamente en las temáticas de cuerpos en equilibrio y tiro parabólico, dirigido a estudiantes y docentes en general. 

La iniciativa surge ante las dificultades que enfrentan los alumnos para comprender estos temas debido a la falta de herramientas interactivas y la limitada conectividad a internet en algunos entornos. Este simulador, que no requiere conexión a internet, busca facilitar un aprendizaje práctico y dinámico, permitiendo a los estudiantes explorar y entender conceptos a su propio ritmo.

El sistema tiene como objetivo principal proporcionar una herramienta interactiva que apoye a los estudiantes y docentes en la comprensión del tema 1: primera condición de equilibrio en Física, tema 2: tiro parabólico, mediante simulaciones que representen de manera visual y práctica los principios físicos involucrados.

## Especificación de Requisitos del Software

### Introducción

#### Propósito

El propósito de este documento es especificar los requisitos del para un simulador educativo diseñado para ayudar a los estudiantes de bachillerato a comprender la primera condición de equilibrio en Física 1. Este simulador será una herramienta interactiva que permitirá a los usuarios explorar conceptos de manera práctica y dinámica, así como comprobar resultados de ejercicios sobre este tema.

#### Convenciones del documento

Este documento sigue normas tipográficas especificas para garantizar claridad y consistencia, lo que facilita la lectura en pantallas. Los títulos y subtítulos están destacados por puntos, lo que permite una rápida identificación de las secciones. Además, se establece que las prioridades de los requisitos, cada enunciado tiene su propia prioridad claramente indicada.

#### Público al que va dirigido y sugerencias de lectura

El documento está destinado a varios tipos de lectores:
* Desarrolladores: Necesitan entender los requisitos funcionales y no funcionales del simulador.
* Usuarios finales (estudiantes): Interesados en cómo el simulador puede faciliar su aprendizaje.
* Evaluadores: Encargados de valorar la usabilidad y efectividad del simulador.
La organización del SRS se estructura en varias secciones clave, comenzando con una introducción general, seguida por la descripción del producto, donde se detallan las funciones y características. Se sugiere leer primero la sección de introducción, luego la descripción general, y finalmente las secciones específicas según el interés.

#### Ámbito del Sistema

Este simulador tiene como objetivo principal proporcionar una herramienta interactiva que permita a los estudiantes y docentes en general explorar y comprender los temas de la primera condición de equilibrio y el tiro parabólico en la materia de Física 1.

Funcionalidades del Sistema:
* Simulación Interactiva: Permitirá a los usuarios manipular objetos físicos virtuales para observar dichas simulaciones.
* Visualización de Resultados: Ofrecerá gráficos y retroalimentación inmediata sobre el estado del sistema simulado.
* Accesibilidad Offline: No requerirá conexión a internet, facilitando su uso en cualquier momento y lugar.

Por otro lado, el sistema no incluirá:
Contenido Avanzado: No abordará temas más allá de la primera condición de equilibrio.
Interacción en Tiempo Real con Otros Usuarios: No permitirá la colaboración en tiempo real entre múltiples usuarios.

#### Beneficios, Objetivos y Metas.

Los beneficios esperados del Simulador incluyen:
* Mejora en la Comprensión Conceptual: Al permitir a los estudiantes interactuar con el contenido, se espera que logren enriquecer sus conocimientos al llevar la teoría a la practica de manera virtual.
* Fomento del Aprendizaje Autónomo: Los estudiantes podrán explorar a su propio ritmo, lo que es especialmente útil para aquellos que requieren más tiempo para entender los temas.
Los objetivos específicos del sistema son:
* Identificar las características esenciales de un simulador a partir de la revisión de literatura y sitios académicos reconocidos.
* Determinar las características del simulador de acuerdo con las necesidades.
* Diseñar e implementar un simulador de escritorio.
Las metas incluyen:
* Evaluar la efectividad del simulador mediante encuestas de satisfacción y usabilidad al finalizar su uso en el aula.

#### Definiciones, Acrónimos y Abreviaturas

Simulador Educativo. Un simulador educativo es una herramienta digital diseñada para replicar virtualmente un fenómeno o proceso específico. Su principal objetivo es ofrecer la oportunidad de explorar, comprender y experimentar conceptos de forma interactiva y atractiva, fomentando la comprensión a través de la práctica [1].

CSUQ. (Cuestionario de usabilidad del sistema) es un cuestionario estandarizado de 15 ítems que se utiliza para medir la satisfacción percibida por los usuarios y la usabiliad de un sistema, sitio web, software o producto al final de un estudio o prueba de usabiliad [18].

### Descripción General

#### Perspectiva del Producto

El Simulador es una herramienta independiente que se integra en el ámbito educativo, específicamente en la enseñanza de la física. Este producto se relaciona con otras herramientas educativas digitales, pero no depende de ellas para su funcionamiento. A diferencia de otros simuladores que requieren conexión a internet o son parte de plataformas más amplias, este simulador está diseñado para operar de manera autónoma en computadoras personales.

#### Funciones del Producto

El Simulador incluirá varias funciones clave:
* Simulación Interactiva: Permite a los usuarios manipular objetos virtuales para observar los efectos de diferentes objetos simulados.
* Visualización Gráfica: Proporciona gráficos que ilustran las fuerzas actuantes y el estado del sistema simulado y trayectoria con el rastro en el lanzamiento del proyectil.
* Retroalimentación Inmediata: Ofrece resultados instantáneos sobre las decisiones del usuario, ayudando a identificar errores por parte de los estudiantes y mejorar la comprensión.
* Configuración Personalizada: Los usuarios podrán ajustar parámetros como peso, ángulo para explorar diferentes escenarios y velocidad de lanzamiento.

#### Características de los Usuarios

Los usuarios del Simulador de Equilibrio y Tiro Parabólico son principalmente estudiantes y docentes. Se espera que tengan conocimientos previos sobre temas fundamentales como fuerzas, vectores y movimiento en caso de los estudiantes, así como un primer acercamiento al estudio del tiro parabólico. Además, deben contar con habilidades tecnológicas suficientes para interactuar con software educativo, aunque no se requiere experiencia previa en el uso de simuladores.

#### Clases de Usuario y Características

Se identificaron dos clases de usuarios que interactuarán con el Simulador de Equilibrio y Tiro Parabólico:
* Estudiantes.
* Docentes.
Entre las características relevantes de los usuarios se destacan la frecuencia de uso, que se estima diaria durante las sesiones de clase; el nivel educativo, correspondiente al bachillerato; y la experiencia técnica, que suele ser básica, aunque suficiente para manejar recursos digitales educativos de forma autónoma.

#### Entorno operativo

El software operará en un entorno específico que incluye:
* Plataforma de hardware: Computadoras personales estándar sin requerimientos especiales.
* Sistema operativo: Compatible con Windows.
* Componentes adicionales: El simulador debe coexistir con bibliotecas como Pygame y Matplotlib, utilizadas para gráficos y
* visualizaciones, esto ya esta previamente incluido dentro del simulador.
Este entorno garantiza que el software sea accesible para todos los estudiantes sin necesidad de hardware avanzado.

#### Suposiciones y Dependencias

El desarrollo del Simulador de Equilibrio y Tiro Parabólico se basa en varias suposiciones clave:
* Se asume que todos los estudiantes y docentes tendrán acceso a computadoras personales o dispositivos compatibles con el software del simulador, ya sea en casa o en el entorno escolar.
* Se considera que los estudiantes cuentan con conocimientos básicos de física, incluyendo nociones fundamentales sobre fuerzas,
* vectores, movimiento rectilíneo y una introducción al tiro parabólico, antes de utilizar el simulador.
* La implementación efectiva del simulador dependerá de la disponibilidad continua del personal docente, quien desempeñará un papel fundamental en la orientación y acompañamiento de los estudiantes, especialmente durante las primeras sesiones de uso.
* Además, se asume que el entorno escolar apoyará el uso de recursos digitales como parte del proceso educativo.
Cualquier cambio significativo en estas condiciones como la falta de acceso tecnológico, limitaciones en la formación previa de los estudiantes o la ausencia de acompañamiento docente podría requerir una revisión y ajuste de los requisitos establecidos para el correcto funcionamiento y aprovechamiento del simulador.

#### Documentación del usuario

La documentación del usuario incluirá componentes esenciales:
* Manual del usuario: Instrucciones detalladas sobre cómo utilizar el simulador.

#### Descripción y prioridad

Cada característica del simulador se describe brevemente junto a su prioridad:
* Simulación Interactiva: Permite manipular objetos virtuales. Prioridad alta.
* Visualización Gráfica: Muestra gráficos sobre fuerzas actuantes. Prioridad media.
* Retroalimentación Inmediata: Proporciona resultados instantáneos. Prioridad alta.

#### Interfaces de usuario

Las interfaces entre el producto y los usuarios incluyen:
* Diseño intuitivo: La interfaz es fácil de usar, con botones claramente etiquetados.
* Menú: Menú de opciones para tanto para la interfaz inicial y la del simulador.

#### Interfaces de software

Las conexiones entre este producto y otros componentes incluyen:
* Bases de datos: El simulador no requiere bases de datos externas ni locales, pero debe ser capaz de mostrar resultados.
* Herramientas integradas: Se utilizan bibliotecas comp Pygame, Matplotlib y Canvas.

### Requisitos Específicos

#### Requisitos funcionales

Simulación Interactiva:
* El sistema permitirá a los usuarios manipular objetos virtuales.
Visualización de Resultados:
* El simulador mostrará gráficos, incluyendo vectores de fuerza y tensiones, trayectoria del lanzamiento.
Retroalimentación Inmediata:
* Proporcionará resultados instantáneos, ayudando a identificar errores al simulador proporcionar resultados inmediados.
Configuración Personalizada:
* Los usuarios podrán ajustar parámetros, permitiendo la exploración de diferentes escenarios.
Interfaz Intuitiva:
* La interfaz gráfica será fácil de usar, facilitando la navegación.

#### Requisitos no funcionales

Usabilidad:
* El simulador debe ser intuitivo y fácil de usar, permitiendo a los estudiantes interactuar con él sin necesidad de formación previa.
Rendimiento:
* El sistema debe responder a las interacciones del usuario en menos de un segundo para asegurar una experiencia fluida.
Compatibilidad:
* Debe funcionar en computadoras personales estándar sin requerir hardware especializado.
Accesibilidad Offline:
* El simulador debe ser completamente funcional sin necesidad de conexión a internet.
Mantenibilidad:
* El código del simulador debe estar bien documentado y estructurado para facilitar futuras actualizaciones y mantenimiento.
Escalabilidad:
* El diseño del simulador debe permitir la incorporación futura de nuevos temas o funcionalidades sin requerir una reestructuración completa del sistema.

### Casos de uso - cuerpos en equilibrio

* Caso 1

![Caso 1](assets/imgMarkdown/0001.png)

### Casos de uso - Tiro parabólico



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