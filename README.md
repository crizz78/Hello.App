Hola
Nivel: 1 - Principiante

Es evidente que las aplicaciones deben proporcionar a los usuarios la funcionalidad necesaria para realizar alguna tarea u objetivo. La eficacia de la funcionalidad de una aplicación es el primer factor que determina cómo los usuarios perciben las aplicaciones que utilizan. Sin embargo, no es lo único que influye en la satisfacción del usuario.

Las características de interfaz de usuario y experiencia de usuario (UI/UX) que los desarrolladores incorporan a las aplicaciones influyen significativamente en la percepción que los usuarios tienen de ellas. Si bien puede ser una simplificación excesiva, la UI/UX se centra principalmente (aunque no exclusivamente) en la "forma" de la aplicación. La personalización es un aspecto de la UX que adapta las características y acciones a cada usuario. Personalizar la funcionalidad de la aplicación de esta manera facilita su uso y la hace más agradable.

El objetivo de la aplicación Hello es aprovechar la geolocalización para obtener el país del usuario y así generar un saludo personalizado en su idioma nativo.

Restricciones
Los desarrolladores deben utilizar el servicio IP-API para obtener la dirección IP de los usuarios.
Los desarrolladores deben utilizar el servicio Fourtonfish para obtener el saludo en el idioma nativo del usuario, pasando la dirección IP del usuario.
Los desarrolladores deben utilizar la decodificación de entidades HTML para decodificar el mensaje de saludo.
Historias de usuario
El usuario puede ver un panel de inicio de sesión simulado que contiene un campo para introducir el nombre de usuario, un campo para introducir la contraseña y los botones "Iniciar sesión" y "Cerrar sesión".
El usuario puede introducir un nombre de usuario ficticio en el campo Nombre de usuario.
El usuario puede introducir una contraseña ficticia en el campo Contraseña. La entrada debe estar enmascarada para que el usuario vea asteriscos ( **) por cada carácter introducido, en lugar de la contraseña en texto plano.
El usuario puede hacer clic en el botón "Iniciar sesión" para realizar un inicio de sesión de prueba.
El usuario podrá ver un mensaje si uno o ambos campos de entrada están vacíos, y el color del borde del/de los campo/s con error deberá cambiarse a rojo.
El usuario puede ver un mensaje de confirmación de inicio de sesión con el siguiente formato: <hello-in-native-language> <user-name> you have successfully logged in!
El usuario puede hacer clic en el botón "Cerrar sesión" para borrar los campos de texto introducidos y cualquier mensaje anterior.
El usuario puede ver un nuevo mensaje cuando cierra sesión correctamente en el siguiente formato: Have a great day <user-name>!
Características adicionales
El usuario puede ver un campo de texto adicional para introducir un código de idioma que se utilizará para anular la dirección IP obtenida mediante geolocalización. Consejo: esta es una función muy útil para probar tu aplicación.
Tras iniciar sesión, el usuario puede ver información de geolocalización adicional que incluye, como mínimo, la dirección IP local, la ciudad, la región, el nombre del país, el código postal, la longitud, la latitud y la zona horaria.
Enlaces y recursos útiles
La forma sigue a la función (Wikipedia)
Personalización (Wikipedia)
Fourtonfish
API IP
Proyectos de ejemplo
Fourtonfish Hola Mundo
