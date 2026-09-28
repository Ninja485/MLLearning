# Introduccion
## ¿Que es Aprendizaje Automatico?
ML ofrece una nueva manera de resolver problemas, respondiendo a cuestiones complejas, y crear nuevo contenido. ML puede predecir el tiempo, aproximaciones del tiempo de viaje,
autocompletar frases, resumir articulos o generar imagenes nuevas.

En resumen, ML es el proceso de entrenar una pieza de SW, llamada modelo, para realizar predicciones útiles o generar nuevo contenido a partir de los datos.

### Tipos de sistemas ML
Los sistemas ML  son de una o más de las siguientes categorías en función de cómo aprenden o generan contenido:

    - Aprendizaje supervisado(supervised learning)
    - Aprendizaje no supervisado(Unsupervised learning)
    - Aprendizaje por refuerzo(Reinforcement Learning)
    - IA Generativa(Generative AI)
### Aprendizaje Supervisado
En aprendizaje supervisado, los modelos pueden hacer predicciones después de ver muchos datos con las respuestas correctas, entonces descubren la conexión entre los datos y la respuesta correcta.

Los dos usos principales del aprendizaje supervisado son la regresión y clasificación.

#### Regresión
Un modelo de regresión predice un valor numérico. P.e la cantidad de lluvia por m3 que sucederá mañana.
#### Clasificación
Los modelos de clasificación predicen a que categoría pertenece valores nuevos de entrada. A diferencia de los modelos de regresión, cuyo valor de salida es numérico, los modelos de clasificación determinan si algo pertenece o no a una categoría en particular.

Podemos distinguir dos tipos de modelos de clasificación según el número de clases de clasificación:
    - Clasificación Binaria: El dominio de clases se define en dos valores, pertence a ella, o no pertenece.
    - Clasificación Multiclase: Tenemos más de dos clases en el dominio, la salida es una de las múltiples clases posibles.

### Aprendizaje No Supervisado 
En aprendizaje no supervisado, los modelos tienen como objetivo identificar patrones discriminantes en los datos. P.e, muchos modelos de este tipo suelen usar la técnica de 
clustering para organizar datos similares en grupos(clusters).

Clustering se diferencia de clasificación, porque no están definidas las categorías por ti. Aunque luego tu puedes designar un nombre a cada uno de los grupos identificados por el modelo por tu comprensión del problema.

### Aprendizaje por refuerzo
Estos modelos realizar predicciones en función de la recompensa/penalización recibida al realizar una acción en el entorno. El objetivo del modelo es encontrar la política que maximice el beneficio. 

### IA Generativa
La IA Generativa es un tipo de modelo que crea contenido a partir de la petición del usuario. P.e crear imágenes por solicitud de texto, o composiciones a través de imágenes. 
Las IA generativas pueden tomar una diversidad de formatos de entrada y crear una variedad de formatos de salida, y combinaciones de estas.
Podemos diferenciar las ia generativas por sus entradas y salidas:
    - Texto a texto
    - Texto a imagen
    - Texto a vídeo
    - Texto a código.
    - Etc.
Las IA generativas funcionan un poco como aprenden los humanos cuando copian o toman referencias de otras personas.

## Aprendizaje Supervisado en profundidad

### Conceptos principales del Aprendizaje Supervisado
Este tipo de aprendizaje esta basado principalmente por:
    - Datos
    - Modelo
    - Entrenamiento
    - Evaluación
    - Inferencia
### Datos
Los datos son el núcleo principal de ML. Estos vienen definidos en palabras o números almacenados en una tabla, o como los valores de los pixeles u ondas de una imagen, o en archivos de video. Almacenamos estos datos en datasets. P.e, podríamos tener datasets:
    - Imagen de gatos
    - Precios de casas
    - Información del clima

Los datasets están formados por ejemplos individuales que contienen características y etiquetas, en general, es una fila de la tabla del dataset. Las características son los valores usados por el modelo para predecir las etiquetas. La etiqueta es la respuesta o valor que queremos que el modelo prediga. Las instancias tanto con características como etiquetas se denominan ejemplos etiquetados.

Mientras que los ejemplos no etiquetados no las tienen, y el modelo predice las etiquetas a partir de las características.

#### Las características del dataset
Las cualidades principales de un dataset son su tamaño y diversidad. El tamaño es el número de ejemplos.Mientras que la diversidad indica el rango de valores cubiertos en esos ejemplos. Los buenos datasets cumplen ambos,son grandes y muy diversos.

Los datasets puede ser combinaciones de estas dos cualidades, y ninguna de las dos de forma solitaria es condición suficiente de resolución de los problemas. 
Otra característica de los datasets puede ser el número de características. Algunos datasets contendrán mucha más información que otros, ayudando a la detección de patrones más fácilmente y haciendo mejores predicciones. Aunque no significa que siempre más características rinda mejor, tienen que ser características con cierta relacional causal con el objetivo.

### Modelo
En aprendizaje supervisado, un modelo es la colección compleja de números que define la relación matemática de determinadas características de entrada a valores de etiquetas de salida determinadas. El modelo descubre estos patrones a través del entrenamiento.

### Entrenamiento
Antes de que un modelo pueda hacer predicciones, debe ser entrenado. Para entrenarlo, le pasamos un dataset con datos etiquetados. El objetivo del modelo es conseguir que sus valores predichos sean iguales a las etiquetas con las mismas entradas.En función de la diferencia entre los valores predichos y los reales(lo que se conoce como pérdida o loss), el modelo actualiza su solución gradualmente. En resumen, el modelo aprende la relación matemática entre los atributos y la etiqueta, así realiza mejores predicciones en datos nuevos.
Por este gradual aprendizaje, es que los datasets grande y diversos son mejores. Además, no es necesario pasar todos los atributos del dataset, podemos coger aquellos que pensemos que están más relacionados con nuestra etiqueta y añadirlo para usarlos.

### Evaluación 
Evaluamos un modelo para ver como de bien a aprendido.Cuando evaluamos un modelo por aprendizaje supervisado, usamos un dataset etiquetado, pero solo le pasamos los atributos usados en entrenamiento al modelo. Entonces podemos comparar las predicciones del modelo con los valores de etiquetas verdaderas.
En función de las predicciones del modelo, podemos considerar hacer más entrenamientos y evaluaciones antes de desplegarlo en producción.

### Inferencia
Cuando ya estamos satisfechos con la evaluación, puedes usar el modelo para hacer predicciones, esto es lo que se conoce como inferencia en datos no etiquetados.
