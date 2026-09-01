Descripción del Proyecto

La aplicación Hello es una interfaz web interactiva que simula un sistema de inicio de sesión (login) y ofrece una experiencia personalizada mediante geolocalización. Al ingresar a la aplicación, el sistema detecta de forma automática la dirección IP del usuario (utilizando la API IP-API) y consulta el saludo correspondiente a su idioma nativo a través de la API de Fourtonfish.

Al autenticarse correctamente, el sistema muestra un mensaje de bienvenida personalizado en el idioma local del usuario, procesando de forma segura los caracteres mediante decodificación de entidades HTML. Además, incluye opciones avanzadas como un modo de prueba manual mediante códigos de idioma y la visualización detallada de datos geográficos (ciudad, región, país, coordenadas y zona horaria).

¿Por qué escogí este proyecto?

Aprendizaje práctico de integración de APIs: Permite aprender a conectar una aplicación con servicios externos reales (IP-API y Fourtonfish) para consumir y procesar datos en tiempo real mediante peticiones asíncronas.

Manejo de estados y validación de formularios: Es ideal para dominar conceptos fundamentales del desarrollo web, como la validación de campos obligatorios, la manipulación de eventos (Login/Logout) y el dinamismo en la interfaz mediante manipulación del DOM.

Introducción al diseño UX/UI: Ayuda a entender cómo pequeños detalles visuales —como enmascarar contraseñas o cambiar el color de los bordes a rojo ante un error— mejoran la usabilidad y la percepción de calidad por parte del usuario.

Justificación de la NecesidadAspectoImportancia / ImpactoPersonalización e IdentidadAdaptar la interfaz al idioma nativo del usuario desde el primer contacto reduce la fricción de uso y crea una experiencia más humana y cercana.Feedback Visual EficienteLa validación dinámica en formularios evita la frustración del usuario al indicar claramente qué campos requieren corrección mediante alertas e indicadores visuales.Pruebas y EscalabilidadLa inclusión de herramientas de anulación de código de idioma (override) responde a la necesidad técnica de probar el sistema en diferentes entornos geográficos sin requerir conexiones VPN externas.

Desglose de la Metodología
Desarrollo Basado en Historias de Usuario (Metodologías Ágiles / Scrum):
El proyecto está estructurado dividiendo los requerimientos en "Historias de Usuario" (User Stories). Cada historia describe una interacción específica desde la perspectiva del usuario final (ej. "El usuario puede ver...", "El usuario puede hacer clic..."), lo que facilita el desarrollo incremental y la verificación de funcionalidades.

Desarrollo Orientado a Funcionalidades (FDD - Feature Driven Development):
Se enfoca en entregar funcionalidades pequeñas y bien definidas en ciclos cortos: primero la autenticación básica, luego las validaciones visuales, posteriormente la integración de APIs externas (geolocalización y traducción) y finalmente las características adicionales.

Aprendizaje Basado en Proyectos (ABP):
Al estar clasificado explícitamente como "Nivel: 1 - Principiante", sigue una metodología pedagógica práctica donde se aplican conceptos teóricos (promesas/async-await, peticiones HTTP, manipulación del DOM y diseño UI/UX) mediante la construcción de un producto funcional completo.
