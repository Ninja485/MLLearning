# Conjuntos de datos, generalización y sobreajuste
## Introducción

- Si tuvieras que priorizar la mejora de una de las siguientes áreas en tu proyecto de aprendizaje automático, ¿cuál tendría el mayor impacto?
    - Mejora la calidad de tu conjunto de datos
    Los datos tienen prioridad sobre todo. La calidad y el tamaño del conjunto de datos son mucho más importantes de lo que el algoritmo más brillante que usas para crear tu modelo.
-  En tu proyecto de aprendizaje automático, ¿cuánto tiempo sueles invertir en la preparación y transformación de los datos?
    - Más de la mitad del tiempo del proyecto.
    - Sí, quienes practican el AA dedican la mayor parte de su tiempo a la construcción de conjuntos de datos y a la ingeniería de atributos.

## Características de los datos
Un conjunto de datos es una colección de ejemplos. Muchos conjuntos de datos almacenan datos en tablas (cuadrículas), por ejemplo, como valores separados por comas (CSV) o directamente desde hojas de cálculo o tablas de bases de datos. Las tablas son un formato de entrada intuitivo para los modelos de aprendizaje automático. Puedes imaginar cada fila de la tabla como un ejemplo y cada columna como un atributo o una etiqueta potenciales. Dicho esto, los conjuntos de datos también pueden derivarse de otros formatos, incluidos los archivos de registro y los búferes de protocolo.

Independientemente del formato, la calidad de tu modelo de AA depende de los datos con los que se entrena. 

### Tipos de datos
Un conjunto de datos puede contener muchos tipos de datos, incluidos, entre otros, los siguientes:
- datos numéricos
- datos categóricos
- lenguaje humano, incluidas palabras y oraciones individuales, hasta documentos de texto completos
- multimedia (como imágenes, videos y archivos de audio)
- resultados de otros sistemas de AA
- vectores de incorporación, que se tratan en una unidad posterior

### Cantidad de datos
Como regla general, tu modelo debe entrenarse con al menos un orden de magnitud (o dos) más de ejemplos que los parámetros entrenables. Sin embargo, los buenos modelos suelen entrenarse con muchos más ejemplos que eso.

Los modelos entrenados con grandes conjuntos de datos con pocas características suelen tener un mejor rendimiento que los modelos entrenados con conjuntos de datos pequeños con muchas características.

Los diferentes conjuntos de datos para diferentes programas de aprendizaje automático pueden requerir cantidades muy diferentes de ejemplos para crear un modelo útil. Para algunos problemas relativamente simples, unas pocas docenas de ejemplos pueden ser suficientes. Para otros problemas, un billón de ejemplos podría no ser suficiente.

Es posible obtener buenos resultados a partir de un conjunto de datos pequeño si adaptas un modelo existente que ya se entrenó con grandes cantidades de datos del mismo esquema.

### Calidad y confiabilidad de los datos
Todos prefieren la alta calidad a la baja calidad, pero la calidad es un concepto tan ambiguo que se puede definir de muchas maneras diferentes. En este curso, se define la calidad de manera pragmática:

```
Un conjunto de datos de alta calidad ayuda a tu modelo a lograr su objetivo. Un conjunto de datos de baja calidad impide que tu modelo alcance su objetivo.
```

Por lo general, un conjunto de datos de alta calidad también es confiable. La confiabilidad se refiere al grado en que puedes confiar en tus datos. Es más probable que un modelo entrenado en un conjunto de datos confiable genere predicciones útiles que un modelo entrenado en datos poco confiables.

Para medir la confiabilidad, debes determinar lo siguiente:
- ¿Qué tan comunes son los errores de etiquetado? Por ejemplo, si tus datos los etiquetan personas, ¿con qué frecuencia cometen errores?
- ¿Tus atributos tienen ruido? Es decir, ¿los valores de tus atributos contienen errores? Sé realista: no puedes borrar todo el ruido de tu conjunto de datos. Es normal que haya un poco de ruido. Por ejemplo, las mediciones del GPS de cualquier ubicación siempre fluctúan un poco de una semana a otra.
- ¿Los datos se filtraron correctamente para tu problema? Por ejemplo, ¿tu conjunto de datos debe incluir búsquedas de bots? Si estás compilando un sistema de detección de spam, es probable que la respuesta sea sí. Sin embargo, si intentas mejorar los resultados de la búsqueda para las personas, la respuesta es no.

A continuación, se incluyen las causas comunes de datos poco confiables en los conjuntos de datos:
- Valores omitidos. Por ejemplo, una persona olvidó ingresar un valor para la antigüedad de una casa.
- Ejemplos duplicados. Por ejemplo, un servidor subió por error las mismas entradas de registro dos veces.
- Valores de atributos incorrectos. Por ejemplo, alguien escribió un dígito de más o un termómetro quedó al sol.
- Etiquetas incorrectas. Por ejemplo, una persona etiquetó por error una imagen de un roble como un arce.
- Secciones de datos incorrectas. Por ejemplo, una función es muy confiable, excepto por ese día en que la red falló constantemente.

Te recomendamos que uses la automatización para marcar los datos poco confiables. Por ejemplo, las pruebas de unidades que definen o dependen de un esquema de datos formal externo pueden marcar valores que se encuentran fuera de un rango definido.

Nota: Es casi seguro que cualquier conjunto de datos lo suficientemente grande o diverso contenga valores atípicos que no se encuentren dentro de tu esquema de datos o bandas de pruebas de unidades. Determinar cómo manejar los valores atípicos es una parte importante del aprendizaje automático. En la unidad de datos numéricos, se detalla cómo manejar los valores atípicos numéricos.

### Ejemplos completos y ejemplos incompletos
En un mundo ideal, cada ejemplo es completo, es decir, cada ejemplo contiene un valor para cada atributo.

Lamentablemente, los ejemplos del mundo real suelen ser incompletos, lo que significa que falta al menos un valor de atributo.

No entrenes un modelo con ejemplos incompletos. En su lugar, corrige o elimina los ejemplos incompletos haciendo una de las siguientes acciones:
- Borra los ejemplos incompletos.
- Impute valores faltantes; es decir, convertir el ejemplo incompleto en uno completo proporcionando conjeturas bien fundamentadas para los valores faltantes.

Si el conjunto de datos contiene suficientes ejemplos completos para entrenar un modelo útil, considera borrar los ejemplos incompletos. Del mismo modo, si a un solo atributo le falta una cantidad significativa de datos y es probable que no pueda ayudar mucho al modelo, considera borrarlo de las entradas del modelo y ver cuánta calidad se pierde cuando se quita. Si el modelo funciona igual o casi igual sin él, es excelente. Por el contrario, si no tienes suficientes ejemplos completos para entrenar un modelo útil, puedes considerar imputar los valores faltantes.

Está bien borrar ejemplos inútiles o redundantes, pero no es bueno borrar ejemplos importantes. Lamentablemente, puede ser difícil diferenciar entre ejemplos inútiles y útiles. Si no puedes decidir si borrar o imputar, considera crear dos conjuntos de datos: uno formado por la eliminación de ejemplos incompletos y el otro por la imputación. Luego, determina qué conjunto de datos entrena el mejor modelo.

Los algoritmos inteligentes pueden imputar algunos valores faltantes bastante buenos. Sin embargo, los valores imputados rara vez son tan buenos como los valores reales. Por lo tanto, un buen conjunto de datos le indica al modelo qué valores se imputan y cuáles son reales. Una forma de hacerlo es agregar una columna booleana adicional al conjunto de datos que indique si se imputa el valor de una característica en particular. Por ejemplo, dado un atributo llamado temperature, podrías agregar un atributo booleano adicional llamado temperature_is_imputed. Luego, durante el entrenamiento, es probable que el modelo aprenda gradualmente a confiar en los ejemplos que contienen valores imputados para la característica temperature menos que en los ejemplos que contienen valores reales (no imputados).

La imputación es el proceso de generar datos bien fundamentados, no datos aleatorios ni engañosos. Ten cuidado: una buena imputación puede mejorar tu modelo, mientras que una mala puede perjudicarlo.

Un algoritmo común es usar la media o la mediana como el valor imputado. En consecuencia, cuando representas un atributo numérico con puntuación Z, el valor imputado suele ser 0 (porque 0 suele ser el promedio de los puntuación Z).

Un conjunto de datos ordenado a veces puede simplificar la imputación. Sin embargo, no es una buena idea entrenar en un conjunto de datos ordenado. Por lo tanto, después de la interpolación, aleatoriza el orden de los ejemplos en el conjunto de entrenamiento.

## Etiquetas
### Comparación entre etiquetas directas y de proxy
Considera dos tipos diferentes de etiquetas:
- Etiquetas directas, que son etiquetas idénticas a la predicción que tu modelo intenta realizar. Es decir, la predicción que tu modelo intenta realizar está presente exactamente como una columna en tu conjunto de datos. Por ejemplo, una columna llamada bicycle owner sería una etiqueta directa para un modelo de clasificación binaria que predice si una persona tiene o no una bicicleta.
- Etiquetas proxy, que son etiquetas similares, pero no idénticas, a la predicción que tu modelo intenta realizar Por ejemplo, una persona que se suscribe a la revista Bicycle Bizarre probablemente tenga una bicicleta, pero no es seguro.

En general, las etiquetas directas son mejores que las etiquetas de proxy. Si tu conjunto de datos proporciona una etiqueta directa posible, probablemente deberías usarla. Sin embargo, a menudo, las etiquetas directas no están disponibles.

Las etiquetas de proxy siempre son un compromiso, una aproximación imperfecta de una etiqueta directa. Sin embargo, algunas etiquetas de proxy son aproximaciones lo suficientemente cercanas como para ser útiles. Los modelos que usan etiquetas de proxy solo son tan útiles como la conexión entre la etiqueta de proxy y la predicción.

Recuerda que cada etiqueta debe representarse como un número de punto flotante, similar al vector de atributos (porque el aprendizaje automático es, fundamentalmente, una colección de operaciones matemáticas). A veces, existe una etiqueta directa, pero no se puede representar fácilmente como un número de punto flotante. En este caso, usa una etiqueta de proxy.

### Datos generados por humanos
Algunos datos son generados por humanos, es decir, una o más personas examinan cierta información y proporcionan un valor, por lo general, para la etiqueta. Por ejemplo, uno o más meteorólogos podrían examinar imágenes del cielo e identificar los tipos de nubes.

Como alternativa, algunos datos se generan automáticamente. Es decir, el software (posiblemente, otro modelo de aprendizaje automático) determina el valor. Por ejemplo, un modelo de aprendizaje automático podría examinar imágenes del cielo y, luego, identificar automáticamente los tipos de nubes.

En esta sección, se exploran las ventajas y desventajas de los datos generados por humanos.

Ventajas:
- Los evaluadores humanos pueden realizar una amplia variedad de tareas que incluso los modelos de aprendizaje automático sofisticados pueden tener dificultades para completar.
- El proceso obliga al propietario del conjunto de datos a desarrollar criterios claros y coherentes.

Desventajas:
- Por lo general, se les paga a los evaluadores humanos, por lo que los datos generados por humanos pueden ser costosos.
- Errar es humano. Por lo tanto, es posible que varios evaluadores humanos deban evaluar los mismos datos.

Piensa en estas preguntas para determinar tus necesidades:
- ¿Qué tan capacitados deben ser tus evaluadores? (Por ejemplo, ¿los evaluadores deben saber un idioma específico? ¿Necesitas lingüistas para aplicaciones de diálogo o PNL?
- ¿Cuántos ejemplos etiquetados necesitas? ¿Qué tan pronto los necesitas?
- ¿Cuál es tu presupuesto?

Siempre verifica a tus evaluadores humanos. Por ejemplo, etiqueta 1, 000 ejemplos por tu cuenta y observa cómo tus resultados coinciden con los de otros evaluadores. Si surgen discrepancias, no supongas que tus calificaciones son las correctas, en especial si se trata de un juicio de valor. Si los evaluadores humanos introdujeron errores, considera agregar instrucciones para ayudarlos y vuelve a intentarlo.

Revisar tus datos de forma manual es un buen ejercicio, independientemente de cómo los hayas obtenido. Andrej Karpathy hizo esto en ImageNet y escribió sobre la experiencia.

Los modelos se pueden entrenar con una combinación de etiquetas generadas automáticamente y por personas. Sin embargo, para la mayoría de los modelos, un conjunto adicional de etiquetas generadas por humanos (que pueden quedar obsoletas) no suele valer la pena por la complejidad y el mantenimiento adicionales. Dicho esto, a veces las etiquetas generadas por humanos pueden proporcionar información adicional que no está disponible en las etiquetas automáticas.

## Conjuntos de datos con desequilibrio de clases
En esta sección, se exploran las siguientes tres preguntas:
- ¿Cuál es la diferencia entre los conjuntos de datos equilibrados y los conjuntos de datos desequilibrados en cuanto a las clases?
- ¿Por qué es difícil entrenar un conjunto de datos desequilibrado?
- ¿Cómo puedes superar los problemas del entrenamiento de conjuntos de datos desequilibrados?

### Conjuntos de datos equilibrados en cuanto a las clases y conjuntos de datos con desequilibrio de clases
Considera un conjunto de datos que contiene una etiqueta categórica cuyo valor es la clase positiva o la clase negativa. En un conjunto de datos equilibrado por clase, la cantidad de clases positivas y clases negativas es aproximadamente igual. Por ejemplo, un conjunto de datos que contiene 235 clases positivas y 247 clases negativas es un conjunto de datos equilibrado.

En un conjunto de datos con desequilibrio de clases, una etiqueta es considerablemente más común que la otra. En el mundo real, los conjuntos de datos con desequilibrio de clases son mucho más comunes que los conjuntos de datos con equilibrio de clases. Por ejemplo, en un conjunto de datos de transacciones con tarjetas de crédito, las compras fraudulentas podrían representar menos del 0.1% de los ejemplos. Del mismo modo, en un conjunto de datos de diagnóstico médico, la cantidad de pacientes con un virus poco común podría ser inferior al 0.01% de los ejemplos totales. En un conjunto de datos con desequilibrio de clases:
- La etiqueta más común se denomina clase mayoritaria.
- La etiqueta menos común se denomina clase minoritaria.

### La dificultad de entrenar conjuntos de datos con un desequilibrio de clases grave
El entrenamiento tiene como objetivo crear un modelo que distinga correctamente la clase positiva de la clase negativa. Para ello, los lotes necesitan una cantidad suficiente de clases positivas y negativas. Esto no es un problema cuando se entrena con un conjunto de datos con un desequilibrio de clases leve, ya que incluso los lotes pequeños suelen contener suficientes ejemplos de la clase positiva y la clase negativa. Sin embargo, un conjunto de datos con un desequilibrio grave entre las clases podría no contener suficientes ejemplos de la clase minoritaria para un entrenamiento adecuado.

El entrenamiento tiene como objetivo crear un modelo que distinga correctamente la clase positiva de la clase negativa. Para ello, los lotes necesitan una cantidad suficiente de clases positivas y negativas. Esto no es un problema cuando se entrena con un conjunto de datos con un desequilibrio de clases leve, ya que incluso los lotes pequeños suelen contener suficientes ejemplos de la clase positiva y la clase negativa. Sin embargo, un conjunto de datos con un desequilibrio grave entre las clases podría no contener suficientes ejemplos de la clase minoritaria para un entrenamiento adecuado.

La exactitud suele ser una métrica deficiente para evaluar un modelo entrenado en un conjunto de datos con clases desequilibradas.

### Entrenamiento de un conjunto de datos con desequilibrio de clases
Durante el entrenamiento, un modelo debe aprender dos cosas:
- Cómo se ve cada clase, es decir, qué valores de atributos corresponden a qué clase
- Qué tan común es cada clase, es decir, cuál es la distribución relativa de las clases

El entrenamiento estándar confunde estos dos objetivos. En cambio, la siguiente técnica de dos pasos llamada **submuestreo y aumento de la ponderación de la clase mayoritaria** separa estos dos objetivos, lo que permite que el modelo alcance ambos objetivos.

#### Paso 1: Submuestrea la clase mayoritaria

Reducción de muestreo significa entrenar con un porcentaje desproporcionadamente bajo de ejemplos de la clase mayoritaria. Es decir, fuerces artificialmente un conjunto de datos con desequilibrio de clases para que se vuelva algo más equilibrado omitiendo muchos de los ejemplos de la clase mayoritaria del entrenamiento. El submuestreo aumenta considerablemente la probabilidad de que cada lote contenga suficientes ejemplos de la clase minoritaria para entrenar el modelo de forma adecuada y eficiente.

Por ejemplo, el conjunto de datos desequilibrado en cuanto a las clases que se muestra en la Figura 6 consta de un 99% de ejemplos de la clase mayoritaria y un 1% de ejemplos de la clase minoritaria. La reducción de muestreo de la clase mayoritaria en un factor de 25 crea artificialmente un conjunto de entrenamiento más equilibrado (80% de clase mayoritaria y 20% de clase minoritaria).

#### Paso 2: Aumenta la ponderación de la clase submuestreada

El submuestreo introduce un sesgo de predicción, ya que le muestra al modelo un mundo artificial en el que las clases están más equilibradas que en el mundo real. Para corregir este sesgo, debes aumentar el peso de las clases mayoritarias según el factor por el que realizaste la reducción de muestreo. El incremento de ponderación significa tratar la pérdida en un ejemplo de clase mayoritaria con más severidad que la pérdida en un ejemplo de clase minoritaria.

Por ejemplo, si reducimos la muestra de la clase mayoritaria en un factor de 25, debemos aumentar su peso en un factor de 25. Es decir, cuando el modelo predice erróneamente la clase mayoritaria, trata la pérdida como si fueran 25 errores (multiplica la pérdida normal por 25).

¿Cuánto debes submuestrear y sobreponderar para reequilibrar tu conjunto de datos? Para determinar la respuesta, debes experimentar con diferentes factores de submuestreo y aumento de peso, al igual que lo harías con otros hiperparámetros.

### Beneficios de esta técnica

La reducción del muestreo y el aumento de la ponderación de la clase mayoritaria aportan los siguientes beneficios:
- Mejor modelo: El modelo resultante "conoce" lo siguiente:
    - La conexión entre los atributos y las etiquetas
    - La distribución real de las clases
- Convergencia más rápida: Durante el entrenamiento, el modelo ve la clase minoritaria con más frecuencia, lo que ayuda a que el modelo converja más rápido.

## División del conjunto de datos original

