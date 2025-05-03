# 1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

- En este contexto, GraphQL es más útil por el tema de flexibilidad, ya que permite solicitar únicamente las variables específicas sin necesidad de traer todo el objeto. Además, se requieren menos peticiones: por ejemplo, al modificar el stock, con REST se necesitan dos llamadas, mientras que con GraphQL se puede hacer con una sola mutación. Finalmente, ofrece la ventaja de ser un esquema tipado, lo que nos permite saber con anticipación los campos que esperamos.

# 2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

- Los tipos (schema) se definen con type_defs, que es la sintaxis de GraphQL y nos sirve para indicar qué datos podemos pedir. Los type sirven para definir Objetos, Query y Mutation. Los resolvers se refieren a cómo se obtienen o modifican los datos; son funciones en Python que ejecutan la lógica cuando se hace una consulta o una mutación.

# 3. ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?

- Por 3 puntos principales, el primero es por la consistencia que da, ya que si un cliente modifica el stock, el front no se enteraria de actualizar el (disponible), el segundo punto es la seguridad, ya que si hay una tienda online podria enviar un Disponible: true aunque este el stock en 0, y por ultimo es la confiabilidad del backend, ya que es la fuente confiable de la regla de negocio, que el backend decida y no el Front

# 4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

- La modificación del stock ocurre exclusivamente a través de la mutación (en mi caso, modificarStock). No existe otra forma de hacerlo. Además, la actualización del stock y del campo disponible ocurre dentro del mismo bloque de código, y no por separado. Por último, se realiza una validación para asegurar que todo esté en orden.
