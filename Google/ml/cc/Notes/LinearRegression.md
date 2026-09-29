# Regresión Lineal
Regresión lineal es una técnica estadística usada para buscar la relación entre variables. En el contexto de ML, busca la relación entre los atributos y la etiqueta.

## Regresión Lineal
### Ecuación de regresión linear
En términos algebraicos, el modelo es definido por la función linear $$y = mx + b$$.En ML, lo especificamos como: $$y' = b +w_1x_1$$ donde:

    - y' es la etiqueta predicha por el modelo
    - b es el sesgo del modelo. Es el valor de la intersección en el eje Y en una ecuación de una recta. Algunas veces se nombra como w0. Este también es un parámetro del modelo calculado en el entrenamiento.
    -  w1 es el peso del atributo x1.Es un parámetro del modelo calculado en su entrenamiento también.
    - x1 es el atributo de entrada.
Durante el entrenamiento, el modelo calcula el sesgo y los pesos que producen el mejor modelo.

### Modelos con múltiples características
La ecuación anterior solo presentaba un atributo $x_1$, pero eso no quiere decir que no podamos tener con modelos con múltiples parámetros, con la fórmula siguiente: $$w_0 + \sum_{i=1}^{n} w_ix_i$$

## Perdidas(Loss)
Las perdidas son una métrica numérica que describe como de mal son las predicciones de un modelo. Mide la distancia entre las predicciones del modelo y las etiquetas verdaderas. El propósito del entrenamiento es minimizar las perdidas. 

### Distancia de perdidas
En estadística y ML, la medida de perdida es la diferencia entre el valor predicho y el real. Y se centra en la distancia entre los valores, no en la dirección, por ello no nos provocamos si la resta negativa, nos interesa el valor absoluto. Las dos maneras más populares de quitar el signo son:
    - Usar el valor absoluto de las diferencias.
    - Elevar al cuadrado las diferencias.
### Tipos de perdidas
| Tipo de perdida | Definición | Ecuación |
|----------|----------|----------|
| Perdida $L_1$    | Sumatorio del valor absoluto de las diferencias.   | $\sum\|valorReal - valorPredicho\|$  |
| Mean Absolute Error(MAE)    | El promedio de las perdidas $L_1$ de un set con N ejemplos.   | $\frac{1}{N}\sum\|valorReal - valorPredicho\| $ |
| Perdida $L_2$| Sumatorio del cuadratico de la diferencia. | $\sum(valorReal - valorPredicho )^2$ |
| Mean Squared Error(MSE) | El promedio de las perdidas $L_2$ entre N ejemplos. | $\frac{1}{N}\sum(valorReal - valorPredicho )^2 $ |
| Root Mean Squared Error(RMSE) | La raíz cuadrada de MSE. | $\sqrt{\frac{1}{N}\sum(valorReal - valorPredicho )^2} $ | 

La diferencia principal entre $L_1$ y $L_2$ es si usa el valor absoluto o el cuadrático. Cuando la diferencia es un valor considerable, elevar al cuadrado hace que la perdida sea bastante más grande. Cuando la diferencia es pequeña(menor a 1), el cuadrado la reduce aún más.
Las métricas como MAE y RMSE son preferibles, ya que son más comprensibles para nosotros, ya que miden el error con la misma escala que el valor predicho por el modelo. 
MAE y RMSE pueden ser bastante diferentes también. MAE representa la pérdida promedio, mientras que RMSE representa la distribución de los errores, y presenta más sesgo para errores grandes.
Cuando procesas múltiples ejemplos, las medidas promedio son mejores.

### Eligiendo una perdida

Decidir si elegir MAE o MSE depende del dataset y la manera en que quieras manejar ciertas predicciones.La mayoría de valores de los atributos en un dataset tiene un rango distintivo propio, es decir, cada uno tiene sus propios dominios y magnitudes características. Cuando los valores de los atributos están fuera del dominio general, se les considera valores atípicos.

Las anomalías también se refieren como de impreciso ha sido el modelo al predecir sus valores respecto a la etiqueta, este escenario ocurre porque el modelo predice un valor más "correcto" cuando el valor real de la etiqueta es anómalo.
A la hora de elegir la mejor función de perdidas, ten en cuenta como quieres que el modelo trate los casos atípicos. P.e, MSE mueve el modelo hacía los valores atípicos, mientras que MAE no. La perdida en $L_2$ penaliza mucho más las valores atípicos respecto a $L_1$.En resumen:

    - **MSE**: El modelo está más cerca de los valores atípicos pero menos del resto de datos.
    - **MAE**: Al contrario, el modelo se aleja más de los resultados atípicos y se acerca más al resto.
Por tanto:

    - Elige MSE si quieres penalizar profundamente los errores grandes. O si los datos atípicos son datos validos e importantes de variabilidad que el modelo debería tener en cuenta.
    - Elige MAE si quieres que los datos atípicos no influyan tanto en el modelo. O si prefieres una función más simple de interpretar como el error promedio.

En la práctica también depende del problema y que tipo de error es más costoso.

## Descenso de gradiente
Descenso de gradiente es una técnica matemática que de forma iterativa encuentra los pesos y sesgo que minimizan la perdida. Hace esto ejecutando un número de ciclos determinados por el usuario.
El modelo empieza con pesos y sesgo aleatorios próximos a cero,y entonces repite los siguientes pasos:
    
    1. Calcula perdida con el peso y sesgo actual.
    2. Determina la dirección en que mover los pesos y sesgo para reducir la perdida.
    3. Varía un poco los pesos y sesgos en la dirección que reduce la perdida.
    4. Vuelve al paso 1 hasta que el modelo no puede reducir la perdida.

Al final, el modelo reduce la perdida repetidamente hasta que converge. Cuando converge, los entrenamientos ya no reducen la perdida, ya que ha encontrado valores muy próximos a aquellos que minimizan la perdida.
Si continuamos entrenado pasada la convergencia, los valores de perdida empiezan a fluctuar en pequeñas cantidades. Esto puede complicar la verificación de la convergencia del modelo. Por ello, entrenarás el modelo hasta que la perdida se haya estabilizado.

### Convergencia del modelo y curva de perdida
Cuando entrenes un modelo, a menudos mirarás la curva de perdidas para ver si ha convergido. Esta curva muestra como cambia la perdida a lo largo del entrenamiento.

### Convergencia y funciones convexas
La función de perdida para modelos lineales siempre produce una superficie convexa. Por esta propiedad, cuando un modelo de regresión lineal converge, sabemos que hemos encontrado los valores de los parámetros que minimizan la perdida. Aunque esto es mentira en cierto sentido, como ya hemos dicho, encuentra valores muy próximos a los óptimos.

## Hiperparámetros
Los hiperparámetros son variables que controlan distintos aspectos del entrenamiento. Los tres más comunes son:

    - El índice de aprendizaje(Learning rate)
    - El tamaño del lote(Batch Size)
    - Las épocas(Epochs)

A diferencia de los parámetros que son variables del modelo. Los hiperparámetros son valores que tu decides, los parámetros son valores calculados en el entrenamiento. 

### Indice de aprendizaje
Es un número de coma flotante que configuras para determinar como de rápido quieres que el modela converja. Si es muy bajo, el modelo tomará mucho para converger. En el caso contrario, al ser muy alto, hace que nunca converja y fluya alrededor de los valores que minimicen la perdida. El objetivo es elegir un valor adecuado para aprender, pero no demasiado alto ni bajo.
Determina la magnitud del cambio de los pesos y el sesgo en cada iteración. El modelo multiplica el gradiente por el índice de aprendizaje para configurar los valores de los parámetros para la siguiente iteración.

### Tamaño de lote
El tamaño del lote se refiere al número de ejemplos que el modelo procesa antes de actualizar los pesos y sesgo. Hacerlo de 1 en 1 no es práctico para datasets grandes.
Dos técnicas habituales para obtener el correcto gradiente con frecuencia sin necesitar mirar el dataset antes de actualizar los parámetros son:

    - **Descenso de gradiente estocástico(SGD)**: Usa un tamaño de lote de 1 por iteración. Funcione pero produce mucho ruido. El ruido son aquellas variaciones durante el entrenamiento que aumentan la perdida en vez de disminuirla. El termino estocástico quiere decir que se coge un ejemplo aleatorio del conjunto.
    - **Descenso de gradiente estocástico de minilotes**:Estable el tamaño de lote entre 1 y N(el número total de ejemplos). Entonces el modelo coge estos N' ejemplos de forma aleatoria, hace la media de sus gradientes, y actualiza los pesos y sesgo. Elegir el N' adecuado depende del dataset y los recursos disponibles. Y se comporta más hacía el 1 o hacía el N en cuanto a la recta. Es decir, compromiso de ruido/rapidez de convergencia.

Cuando entrenas puedes pensar que el ruido es algo indeseable. Sin embargo, el ruido puede ser bueno en algunos casos para generalizar mejor p.e en redes neuronales.

### Epocas
Una época indica que se han procesado todos los ejemplos en la iteración. Obviamente la duración de la época en iteraciones es: $$it = \frac{NumeroEjemplos}{TamañoLote}$$ Generalmente el entrenamiento requiere muchas épocas, mejorando el modelo pero requiriendo más tiempo.
| Tipo de lote | Cuándo se producen las actualizaciones de los pesos y el sesgo | 
|----------|----------|
| Lote completo | Después de que el modelo observa todos los ejemplos del conjunto de datos Por ejemplo, si un conjunto de datos contiene 1,000 ejemplos y el modelo se entrena durante 20 épocas, el modelo actualiza los pesos y el sesgo 20 veces, una vez por época. |
| Descenso de gradientes estocástico | Después de que el modelo analiza un solo ejemplo del conjunto de datos Por ejemplo, si un conjunto de datos contiene 1,000 ejemplos y se entrena durante 20 épocas, el modelo actualiza los pesos y la desviación 20,000 veces. |
| Descenso de gradientes estocástico por minilotes | Después de que el modelo analiza los ejemplos de cada lote Por ejemplo, si un conjunto de datos contiene 1,000 ejemplos, el tamaño del lote es 100 y el modelo se entrena durante 20 épocas, el modelo actualiza los pesos y el sesgo 200 veces. |