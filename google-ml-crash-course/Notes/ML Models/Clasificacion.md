# Clasificación
## Introducción
La clasificación es la tarea de predecir a qué clase pertenece una instancia de un conjunto de clases(categorías). Aprenderemos:

    - Como convertir un modelo de regresión lógica en un modelo de clasificación binaria(probabilidades -> clases).
    - Métricas de calidad de predicción en clasificadores.
    - Clasificación multiclase.

##  Umbrales y la matriz de confusión
Para transformar las probabilidades del modelo logístico a las clases del modelo de clasificación lo que vamos a hacer es definir un **umbral de clasificación**. Aquellos por encima del umbral, se asignan a la clase positiva, en caso de ser inferior va a la clase negativa.
En caso de 50/50, depende del modelo usado. En la librería Keras se asigna la clase negativa.

### Matriz de confusión
La clasificación de un clasificador binaria cae en una de las siguientes cuatro categorías:

||Positivo real| Negativo real|
|--|---|---|
|Positivo previsto | Verdadero positivo (VP) | Falso positivo |
| Negativo previsto| Falso negativo (FN) | Verdadero negativo |


Donde:

- **Verdadero positivo**: Ha sido clasificado positivamente y correctamente.
- **Falso positivo**: Ha sido clasificado como positivo incorrectamente
- **Falso negativo**:  Ha sido clasificado como negativo correctamente.
- **Verdadero negativo (VN)**: Ha sido clasificador como clase negativa incorrectamente.

Observa que el total de cada fila muestra todos los positivos pronosticados (VP + FP) y todos los negativos pronosticados (FN + TN), independientemente de la validez. Mientras tanto, el total de cada columna muestra todos los verdaderos positivos (VP + FN) y todos los verdaderos negativos (FP + VN), independientemente de la clasificación del modelo.

Cuando el total de positivos reales no está cerca del total de negativos reales, el conjunto de datos está desbalanceado. 
## Exactitud, recuperación, precisión y métricas relacionadas
Los verdaderos y falsos positivos y negativos se usan para calcular varias métricas útiles para evaluar modelos. Las métricas de evaluación más significativas dependen del modelo y la tarea específicos, el costo de las diferentes clasificaciones incorrectas y si el conjunto de datos está balanceado o desbalanceado.

Todas las métricas de esta sección se calculan en un solo umbral fijo y cambian cuando este se modifica. Muy a menudo, el usuario ajusta el umbral para optimizar una de estas métricas.

### Exactitud(Accuracy)
La exactitud es la proporción de todas las clasificaciones que fueron correctas, ya sean positivas o negativas. Se define matemáticamente de la siguiente manera: $$ Accuracy=\frac{TP+TN}{TP+TN+FP+FN}$$

Dado que incorpora los cuatro resultados de la matriz de confusión (VP, FP, VN y FN), dado un conjunto de datos equilibrado, con cantidades similares de ejemplos en ambas clases, la precisión puede servir como una medida general de la calidad del modelo. Por este motivo, suele ser la métrica de evaluación predeterminada que se usa para los modelos genéricos o no especificados que realizan tareas genéricas o no especificadas.

Sin embargo, cuando el conjunto de datos está desequilibrado o cuando un tipo de error (FN o FP) es más costoso que el otro, como sucede en la mayoría de las aplicaciones del mundo real, es mejor optimizar una de las otras métricas.

En el caso de los conjuntos de datos muy desequilibrados, en los que una clase aparece con muy poca frecuencia, por ejemplo, el 1% de las veces, un modelo que predice negativo el 100% de las veces obtendría una puntuación del 99% en exactitud, a pesar de ser inútil.

### Recuperación o tasa de verdaderos positivos
La tasa de verdaderos positivos (TVP), o la proporción de todos los positivos reales que se clasificaron correctamente como positivos, también se conoce como recuperación.

La recuperación se define matemáticamente de la siguiente manera: $$Recall=\frac{TP}{TP+FN}$$
Otro nombre para la recuperación es probabilidad de detección: responde la pregunta "¿Qué fracción detecta este modelo de todas las positivas han sido clasificadas como tal?".

En un conjunto de datos desequilibrado en el que la cantidad de positivos reales es muy baja, la recuperación es una métrica más significativa que la precisión, ya que mide la capacidad del modelo para identificar correctamente todas las instancias positivas. Para aplicaciones como la predicción de enfermedades, es fundamental identificar correctamente los casos positivos. Por lo general, un falso negativo tiene consecuencias más graves que un falso positivo.

### Tasa de falsos positivos
La tasa de falsos positivos (FPR) es la proporción de todos los negativos reales que se clasificaron incorrectamente como positivos, también conocida como la probabilidad de falsa alarma. Se define matemáticamente de la siguiente manera: $$FPR = \frac{FP}{FP+TN}$$

Para un conjunto de datos desequilibrado, el FPR suele ser una métrica más informativa que la precisión. Sin embargo, si la cantidad de negativos reales es muy baja, el FPR puede no ser una opción ideal debido a su volatilidad. Por ejemplo, si solo hay cuatro negativos reales en un conjunto de datos, una clasificación incorrecta genera un FPR del 25%, mientras que una segunda clasificación incorrecta hace que el FPR aumente al 50%. En casos como este, la precisión puede ser una métrica más estable para evaluar los efectos de los falsos positivos.

### Precisión
La precisión es la proporción de todas las clasificaciones positivas del modelo que son realmente positivas. Se define matemáticamente de la siguiente manera: $$Precision=\frac{TP}{TP+FP}$$
En un conjunto de datos desequilibrado en el que la cantidad de positivos reales es muy, muy baja (por ejemplo, de 1 a 2 ejemplos en total), la precisión es menos significativa y menos útil como métrica.

La precisión mejora a medida que disminuyen los falsos positivos, mientras que la recuperación mejora cuando disminuyen los falsos negativos. Sin embargo, como se vio en la sección anterior, aumentar el umbral de clasificación tiende a disminuir la cantidad de falsos positivos y aumentar la cantidad de falsos negativos, mientras que disminuir el umbral tiene los efectos opuestos. Como resultado, la precisión y la recuperación suelen mostrar una relación inversa, en la que mejorar una de ellas empeora la otra.

NaN, o "no es un número", aparece cuando se divide por 0, lo que puede ocurrir con cualquiera de estas métricas. Cuando TP y FP son 0, por ejemplo, la fórmula de precisión tiene 0 en el denominador, lo que genera NaN. Si bien, en algunos casos, NaN puede indicar un rendimiento perfecto y podría reemplazarse por una puntuación de 1.0, también puede provenir de un modelo prácticamente inútil. Por ejemplo, un modelo que nunca predice positivos tendría 0 VP y 0 FP, por lo que el cálculo de su precisión daría como resultado NaN.

### Elección de la métrica y las compensaciones

Las métricas que elijas priorizar cuando evalúes el modelo y elijas un umbral dependerán de los costos, los beneficios y los riesgos del problema específico.

![](MetricasClasificacion.png)

### Métrica extra: Puntuación F1
La puntuación F1 es la media armónica (un tipo de promedio) de la precisión y la recuperación.Matemáticamente, se expresa de la siguiente manera: 
$$F1 =2*\frac{precision * recall}{precision + recall} $$
Esta métrica equilibra la importancia de la precisión y la recuperación, y es preferible a la exactitud para los conjuntos de datos con clases desequilibradas. Cuando la precisión y la recuperación tienen puntuaciones perfectas de 1.0, la puntuación F1 también será perfecta y equivaldrá a 1.0. En términos más generales, cuando la precisión y la recuperación tienen valores similares, la puntuación F1 también será similar a esos valores. Cuando la precisión y la recuperación están muy separadas, la métrica F1 será similar a la que sea peor.

## ROC y AUC

En la sección anterior, se presentó un conjunto de métricas del modelo, todas calculadas en un valor de umbral de clasificación único. Sin embargo, si deseas evaluar la calidad de un modelo en todos los umbrales posibles, necesitas herramientas diferentes.

### Curva de característica operativa del receptor (ROC)

La curva ROC es una representación visual del rendimiento del modelo en todos los umbrales. La versión larga del nombre, característica operativa del receptor, es un remanente de la detección de radar de la Segunda Guerra Mundial.

Para dibujar la curva ROC, se calcula la tasa de verdaderos positivos (TPR) y la tasa de falsos positivos (FPR) en cada umbral posible (en la práctica, en intervalos seleccionados) y, luego, se representa gráficamente la TPR sobre la FPR. Un modelo perfecto, que en algún umbral tiene una TPR de 1.0 y una FPR de 0.0, se puede representar con un punto en (0, 1) si se ignoran todos los demás umbrales o con lo siguiente:

### Área bajo la curva (AUC)

El área bajo la curva ROC (AUC) representa la probabilidad de que el modelo, si se le da un ejemplo positivo y negativo elegido al azar, clasifique el positivo más alto que el negativo.

Para un clasificador binario, un modelo que funciona exactamente igual que las conjeturas aleatorias o las volteretas de moneda tiene un ROC que es una línea diagonal de (0,0) a (1,1). El AUC es de 0.5, lo que representa una probabilidad del 50% de clasificar correctamente un ejemplo positivo y negativo aleatorio.

### Extra: Curva de Precisión-Recuperación(PRC)

La AUC y la ROC funcionan bien para comparar modelos cuando el conjunto de datos está aproximadamente equilibrado entre las clases. Cuando el conjunto de datos está desequilibrado, las curvas de precisión-recuperación (PRC) y el área debajo de esas curvas pueden ofrecer una mejor visualización comparativa del rendimiento del modelo. Para crear curvas de precisión-recuperación, se traza la precisión en el eje Y y la recuperación en el eje X en todos los umbrales.

### AUC y ROC para elegir el modelo y el umbral

La AUC es una medida útil para comparar el rendimiento de dos modelos diferentes, siempre que el conjunto de datos esté aproximadamente equilibrado. Por lo general, el modelo con mayor área debajo de la curva es el mejor.


## Sesgo de predicción

El cálculo del sesgo de predicción es una verificación rápida que puede marcar problemas con el modelo o los datos de entrenamiento en una etapa temprana.

El sesgo de predicción es la diferencia entre la media de las predicciones de un modelo y la media de las etiquetas de verdad fundamental en los datos. Un modelo entrenado con un conjunto de datos en el que el 5% de los correos electrónicos son spam debería predecir, en promedio, que el 5% de los correos electrónicos que clasifica son spam. En otras palabras, la media de las etiquetas en el conjunto de datos de verdad fundamental es 0.05, y la media de las predicciones del modelo también debería ser 0.05. Si este es el caso, el modelo tiene un sesgo de predicción cero. Por supuesto, el modelo podría tener otros problemas.

Si, en cambio, el modelo predice el 50% de las veces que un correo electrónico es spam, algo anda mal con el conjunto de datos de entrenamiento, el nuevo conjunto de datos al que se aplica el modelo o el modelo en sí. Cualquier diferencia significativa entre las dos medias sugiere que el modelo tiene algún sesgo de predicción.

El sesgo de predicción puede deberse a lo siguiente:

- Sesgos o ruido en los datos, incluido el muestreo sesgado para el conjunto de entrenamiento.
- Regularización demasiado fuerte, lo que significa que el modelo se simplificó demasiado y perdió parte de la complejidad necesaria.
- Errores en la canalización de entrenamiento del modelo.
- El conjunto de atributos proporcionado al modelo no es suficiente para la tarea.

## Clasificación Multiclase

La clasificación de varias clases se puede considerar como una extensión de la clasificación binaria a más de dos clases. Si cada ejemplo solo se puede asignar a una clase, el problema de clasificación se puede controlar como un problema de clasificación binaria, en el que una clase contiene una de las múltiples clases y la otra contiene todas las demás clases juntas. Luego, el proceso se puede repetir para cada una de las clases originales.

Por ejemplo, en un problema de clasificación de multiclase de tres clases, en el que clasificas ejemplos con las etiquetas A, B y C, puedes convertir el problema en dos problemas de clasificación binaria separados. Primero, puedes crear un clasificador binario que categorice ejemplos con la etiqueta A+B y la etiqueta C. Luego, podrías crear un segundo clasificador binario que vuelva a clasificar los ejemplos etiquetados como A+B con las etiquetas A y B.

Un ejemplo de un problema de clases múltiples es un clasificador de escritura a mano que toma una imagen de un dígito escrito a mano y decide qué dígito, del 0 al 9, está representado.

Si la pertenencia a la clase no es exclusiva, es decir, un ejemplo se puede asignar a varias clases, esto se conoce como un problema de clasificación de etiquetas múltiples.