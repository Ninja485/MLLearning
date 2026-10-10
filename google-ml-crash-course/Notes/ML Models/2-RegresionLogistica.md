# Regresión Logística
TIpo de modelo de regresión que predice una probabilidad. P.e responder a si lloverá hoy, o si un correo es spam o no.
Necesitamos una función que en el dominio del problema, límite el rango de salida a $(0,1)$, que tienda a 0 cuando tengamos -infinito y a 1 en el positivo. Esta función es la curva sigmoideo que define la función logística.
Esta técnica es usada para crear modelos que discriminan entre dos posibles resultados y clasificación binaria.

## Calculando probabilidades con la función sigmoideo
Muchos problemas requiere una estimación basada en probabilidad como salida. La regresión logística es un mecanismo muy eficiente para el cálculo de probabilidades. Puedes usar la probabilidad devuelta de dos maneras:

    - Aplicado "como si":P.e, si un modelo de predicción de spam devuelve 0.932 ante una entrada. Esto quiere decir que hay un 93.2% de probabilidad de que es spam.
    - Convertirlo en una categoría binaria como Verdadero/Falso, o Spam/No spam.

En esta sección nos enfocaremos en la primera manera, la segunda se profundizará más en el apartado de clasificación.

### Función sigmoideo
La razón por los modelos de regresión logística siempre tienen como salida valores entre 0 y 1 es debido a que estás es una cualidad de las funciones logísticas. La función sigmoideo es también conocida como la función logística estándar, cuya fórmula es: $$f(x) = \frac{1}{1+e^{-x}}$$ donde:
    
    - f(x) es salida de la función sigmoideo.
    - e es la constante de Euler.
    - x es la entrada a la función sigmoideo.
A medida que aumenta la entrada, x, el resultado de la función sigmoidea se acerca a 1, pero nunca lo alcanza. Del mismo modo, a medida que la entrada disminuye, el resultado de la función sigmoideo se acerca a 0, pero nunca lo alcanza.
### Transformando la salida lineal usando la función sigmoideo
La siguiente ecuación representa el componente lineal de un modelo de regresión logística: $$z = b+ w_1x_1 + w_2x_2+...+w_nx_n $$
Donde:
    
    - z es el resultado de la ecuación lineal, también llamado log-odds.
    - b es el sesgo.
    - Los valores de w son los pesos aprendidos del modelo.
    - Los valores x son los valores de atributo para un ejemplo en particular.
Para obtener la predicción de regresión logística, el valor de z se pasa a la función sigmoidea, lo que genera un valor (una probabilidad) entre 0 y 1: $$y' = \frac{1}{1+e^{-z}}$$

## Pérdida y regularización
Los modelos de regresión logística se entrenan con el mismo proceso que los modelos de regresión lineal, con dos distinciones clave:

    - Usan la pérdida logística como función de pérdida en lugar de la pérdida al cuadrado. 
    - Aplicar la regularización es fundamental para evitar el sobreajuste.

### Pérdida logística
 La pérdida al cuadrado funciona bien para un modelo lineal en el que la tasa de cambio de los valores de salida es constante. Sin embargo, la tasa de cambio de un modelo de regresión logística no es constante, ya que la curva sigmoid tiene forma de S en lugar de ser lineal.
 Si usaste la pérdida al cuadrado para calcular los errores de la función sigmoide, a medida que el resultado se acercaba cada vez más a 0 y 1, necesitarías más memoria para conservar la precisión necesaria para hacer un seguimiento de estos valores.
 En cambio, la función de pérdida para la regresión logística es la pérdida logística. La ecuación de pérdida logarítmica devuelve el logaritmo de la magnitud del cambio, en lugar de solo la distancia entre los datos y la predicción. La pérdida logística se calcula de la siguiente manera:
 $$PerdidaLogistica = -\frac{1}{N}\sum_{i = 1}^{N}[y_i log(y'_i) + (1-y_i)log(1-y'_i)]$$
 
Donde:
 
 - N  es la cantidad de ejemplos etiquetados en el conjunto de datos.
 - i es el índice de un ejemplo en el conjunto de datos (p. ej., 
 es el tercer ejemplo en el conjunto de datos).
 - $y_i$ es la etiqueta del ejemplo número 
. Dado que se trata de una regresión logística, 
 debe ser 0 o 1.
 - $y'_i$ es la predicción de tu modelo para el ejemplo $i$
(un valor entre 0 y 1), dado el conjunto de atributos en$x_i$

Esta forma de la función de pérdida logística calcula la pérdida logística media en todos los puntos del conjunto de datos. En la práctica, es conveniente usar la pérdida logística media (en lugar de la pérdida logística total), ya que nos permite desacoplar el ajuste del tamaño del lote y la tasa de aprendizaje.
### Regularización en la regresión logística
Es un mecanismo para penalizar la complejidad del modelo durante el entrenamiento, es extremadamente importante en el modelado de regresión logística. Sin la regularización, la naturaleza asintótica de la regresión logística seguiría llevando la pérdida hacia 0 en los casos en que el modelo tiene una gran cantidad de atributos. Por lo tanto, la mayoría de los modelos de regresión logística usan una de las siguientes dos estrategias para disminuir la complejidad del modelo:

    - Regularización L2
    - Interrupción anticipada: Limita la cantidad de pasos de entrenamiento para detener el entrenamiento mientras la pérdida sigue disminuyendo.