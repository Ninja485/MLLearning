# Capítulo 1: EL panorama del Machine Learning

[← Índice](00-indice.md)

>**Resumen:** Introducción a conceptos básicos del ML.
> **Conceptos claves:** Definición ML, tipos de ML, usos del ML, problemas del ML.

## Contenido
- [Qué es ML](#qué-es-el-aprendizaje-automático): Definición de Aprendizaje Automático
- [Por qué usar ML](#por-qué-usar-ml): Ventajas del ML frente al paradigma clásico
- [Aplicaciones del ML](#ejemplos-de-usos): Aplicaciones y usos específicos del ML.
- [Tipos de ML](#tipos-de-ml): Distintas tipologías de ML y criterios de clasificación.
- [Problemas del ML](#principales-desafíos-y-problemas-del-ml): Principales desventajas del ML, los problemas de este paradigma.
- [Pruebas](#testeo-y-validación): 

## ¿Qué es el Aprendizaje Automático?

ML es la ciencia de programar ordenadores que aprendan de los datos. O una más rigurosa:
> Se dice que un programa aprende con la experiencia *E* en una tarea *T* medida en rendimiento a través de *P*, si el rendimiento
> en *T*, medido con *P*, mejora con la experiencia *E*.

Los ejemplos con los que aprende el programa son el *conjunto de entrenamiento(training set)*. Cada ejemplo de entrenamiento se 
le denomina *instancia o ejemplo de entrenamiento(training instance/sample)*. Y la parte del sistema que aprende y hace las predicciones
se llama *modelo(model)*.

## ¿Por qué usar ML?

Considera cómo implementarías un detector de spam basado en programación tradicional:
1. Primero examinas como son los correos de spam. Detectas patrones y defines las reglas que clasifican un correo como spam.
2. Implementas un algoritmo de detección de spam con estas reglas.
3. Pruebas tu programa repitiendo los anteriores pasos hasta alcanzar un rendimiento bueno para producción.

Debido a qué este problema es difícil, tu programa lo más posible que se convierta en una larga lista de reglas complejas
difíciles de mantener.

Por el contrario, un filtro de spam basado en ML aprenderá por su cuenta esas reglas de detección de spam. Concluyendo
en un programa más corto, fácil de mantener y en general con mejores resultados.

Otra ventaja de ML es frente a los entornos cambiantes. En el caso de la programación tradicional tendrías que modificar el 
código para añadir las nuevas reglas de spam, con ML el sistema se ajusta automáticamente. P.e, imagina que los correos empiezan
a usar "For U" em vez de "4U", en el enfoque tradicional tendrías que añadir "For U" a las reglas. Mientras que ML detectaría que 
"4U" ha dejado de usarse y al recibir reportes de que "4U" es spam aprendería esta nueva regla.

Otro ámbito en el que ML brilla es para problemas que son demasiado complejos para el enfoque tradicional o no tienen algoritmo conocido.
Un ejemplo de esto es el reconocimiento de voz. La mejor solución actual es escribir un algoritmo que aprenda por sí mismo pasándole 
ejemplos de audios de voz.

Finalmente, ML puede ayudar a los humanos a aprender, podemos mirar que ha aprendido el modelo de ML para resolver el problema(aunque esto
algunas veces puede ser difícil). Algunas veces esto revelará correlaciones inesperadas o nuevas modas, concluyendo en un mejor 
entendimiento del problema. Excavar en grandes cantidades de datos para descubrir patrones ocultos se conoce como *data mining*,
y ML es excelente en ello.

Para resumir, ML es buena para:
- Problemas cuya solución existente requiere mucho fine-tuning o largas listas de reglas.
- Problemas complejos que el enfoque tradicional no ofrece ninguna buena solución.
- Entornos cambiantes, un algoritmo de ML puede ser reentrenado para resolver el problema en el nuevo entorno.
- Obtener conocimiento oculto/profundo de problemas complejos y gran cantidad de datos.

## Ejemplos de usos

Algunas tareas concretas para ML junto a soluciones aplicables son las siguientes:
- Analizar imágenes de productos en una línea de producción para clasificarlos.
  -  Problema de clasificación en imágenes, se resuelven con *redes neuronales convolucionales(CNN)* o *transformadores(transformers)*.
- Detectar tumores en escáneres cerebrales
  - Esto es segmentación semántica de imágenes, donde cada pixel es clasificado(para determinar forma y localización del tumor). Se suele
  resolver con *CNN* o *transformers*.
- Clasificación automática de nuevos artículos
  -  Esto es *natural language processing(NLP)*, y más específicamente clasificación de texto, que puede ser atajado usando *recurrent neural networks(RNN)* y CNN. 
  Los *transformadores* funcionan mejor aún.
- Etiquetación automática de comentarios negativos u ofensivos.
  - También es clasificación de texto mediante NLP.
- Resumir automáticamente documentos largos
  - Es una rama de NLP denominada *text summarization*, usando las mismas herramientas.
- Etc.

Estos son solo algunas aplicaciones, hay muchas más usos de ML, además de diversidad de técnicas para resolver el mismo problema con ML.

## Tipos de ML

Los criterios de clasificación de la tipología de los sistemas ML son los siguientes:
- Cómo son supervisados durante el entrenamiento
- Si pueden o no aprender incrementalmente sobre la marcha
- Si funcionan comparando los nuevos datos con datos ya conocidos o identificando patrones en los datos de entrenamiento y 
construyendo un modelo predictivo.

Estos criterios no son excluyentes entre sí, pueden combinarse. Puedes tener una red neuronal profunda que aprenda sobre la marcha con 
ejemplos etiquetados.

### Supervision en el entrenamiento 

Los sistemas ML pueden ser clasificados en función de la cantidad y tipos de supervision que reciben durante el entrenamiento.
Hay muchas categorías, exploraremos solo las siguientes:
- Aprendizaje supervisado(supervised learning).
- Aprendizaje no supervisado(unsupervised learning).
- Self-supervised learning.
- Semi-supervised learning
- Aprendizaje por refuerzo(Reinforcement learning).

#### Supervised Learning

En el entrenamiento supervisado, el conjunto de entrenamiento que alimenta el modelo tiene las soluciones incluidas, denominadas
*labels o etiquetas*.

Una tarea típica del entrenamiento supervisado es la clasificación. El clasificador de spam es un buen ejemplo, ya que puedes tener 
muchos ejemplos con su respectiva *clase*.

Otra tarea típica es la predicción de un valor numérico objetivo, como p.e el precio de un coche, dado un conjunto de *características/features*.
A este tipo se las conoce como *regresión*.

Además, algunos modelos de regresión pueden ser usados para clasificación y viceversa. P.e, la regresión logística es usada para clasificar,
ya que proporciona como salida la probabilidad de pertenecer a una clase.

#### Unsupervised Learning

Los datos de entrenamiento no están etiquetados. Intenta aprender sin un profesor.

P.e imagina que tienes los datos de los visitantes de tu blog. Tal vez querrías ejecutar un algoritmo de *clustering* para
identificar los grupos de visitantes similares. En ningún momento le dices al algoritmo los grupos de los visitantes El algoritmo
encuentra estas conexiones sin tu ayuda. Si usas un algoritmo *hierarchical clustering*, tal vez divida los grupos en múltiples subgrupos
más pequeños. Esto podría ayudarte en ciertas tareas.

Los algoritmos de *visualización(visualization)* son otro ejemplo de entrenamiento no supervisado: les alimentas datos complejos
y sin etiquetar, y tu salida es una representación 2D o 3D de tus datos fácil de representar gráficamente. Estos algoritmos tratan de 
conservar tanta estructura como puedan(intentando que los distintos clústeres de salida no se solapen demasiado) para que sea comprensible
la organización de los datos e identificar patrones ocultos.

Una tarea relacionada con esta última es *reducción de dimensionalidad*, cuyo objetivo es simplificar los datos sin perder demasiada información.
Una manera es combinando atributos existentes relacionados para crear uno nuevo, a esto se le llama *extracción de características*.

> Es recomendable aplicar un algoritmo de reducción de dimensiones de nuestros datos antes de alimentar al algoritmo del modelo. 
> Se ejecutará más rápido, los datos ocuparán menos espacio en disco y memoria, y en algunos casos rendirá mejor.

Otra tarea de este tipo de entrenamiento es la *detección de anomalías(anomaly detection)*. P.e, detectar transacciones de 
crédito anómalas para prevenir el fraude, o eliminar los datos anómalos del conjunto de entrenamiento antes de alimentar el modelo.
Otra tarea de este tipo similar es la *detección de novedades(novelty detection)* que intenta detectar nuevas instancias que 
no se parecen a ninguna en el conjunto de entrenamiento.

Finalmente, podemos hablar de *association rule learning*, cuyo objetivo es indagar en grandes cantidades de atributos y descubrir
relaciones interesantes entre atributos. P.e, te permite descubrir que la gente que compra filetes también compra salsa barbacoa,
por lo que decidirías que estos dos productos estén próximos.

#### Semi-supervised Learning

Debido a la dificultad y coste de etiquetar los datos, en general tienes una mezcla de ambos tipos de datos, tanto muchos etiquetados
como unos pocos no etiquetados. Algunos algoritmos pueden trabajar con este tipo de conjuntos de entrenamiento.

La mayoría de este tipo de algoritmos son una combinación del aprendizaje no supervisado y el supervisado. P.e, un algoritmo puede
definir los distintos clústeres con un algoritmo de clustering. Y entonces etiquetar cada grupo con la etiqueta más presente. Una vez
etiquetados, se puede aplicar un algoritmo de entrenamiento supervisado.

#### Self-supervised Learning

#### Reinforcement Learning

### Batch vs Online Learning

### Instance-Based vs Model-Based Learning
## Principales desafíos y problemas del ML

## Testeo y validación

## Ejercicios
