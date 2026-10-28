# Equidad

## Introducción

Evaluar un modelo de aprendizaje automático (AA) de forma responsable requiere hacer más que solo calcular las métricas de pérdida generales. 
Antes de implementar un modelo en producción, es fundamental controlar los datos de entrenamiento y evaluar las predicciones para detectar sesgos.

## Tipos de sesgo

Los modelos de aprendizaje automático (AA) no son objetivos de manera inherente. Los profesionales del AA entrenan modelos al proporcionarles
un conjunto de datos con ejemplos de entrenamiento. La participación humana en el aprovisionamiento y la selección de estos datos puede hacer que
las predicciones del modelo sean susceptibles al sesgo.

Cuando compilas modelos, es importante tener en cuenta los sesgos humanos comunes que pueden manifestarse en tus datos, para que puedas tomar medidas proactivas y mitigar sus efectos.

> Nota: El siguiente inventario de sesgos proporciona solo una pequeña selección de sesgos que a menudo se encuentran en los 
> conjuntos de datos de aprendizaje automático. Esta lista no pretende ser exhaustiva. El [catálogo de sesgos cognitivos de 
> Wikipedia](https://wikipedia.org/wiki/List_of_cognitive_biases) enumera más de 100 tipos diferentes de sesgos humanos que
> pueden afectar nuestro juicio. Cuando audites tus datos, ten cuidado con todas las posibles fuentes de sesgo que podrían sesgar las predicciones del modelo.

### Sesgo de reporte

El sesgo de reporte se produce cuando la frecuencia de los eventos, las propiedades o los resultados contenidos en un conjunto de datos no refleja con 
exactitud su frecuencia en el mundo real. Una posible causa es que las personas tienden a enfocarse en el registro de circunstancias inusuales o especialmente memorables,
ya que se supone que lo común no se necesita registrar.

Se entrena un modelo de análisis de opiniones para predecir si las opiniones sobre libros son positivas o negativas en función de un corpus 
de envíos de usuarios a un sitio web popular. La mayoría de las opiniones del conjunto de datos de entrenamiento reflejan opiniones extremas 
(revisores que amaron u odiaron un libro), ya que era menos probable que las personas enviaran una opinión sobre un libro si no les había gustado mucho. 
Como resultado, el modelo es menos capaz de predecir correctamente el sentimiento de las opiniones que usan un lenguaje más sutil para describir un libro.

### Sesgo histórico

El sesgo histórico se produce cuando los datos históricos reflejan desigualdades que existían en el mundo en ese momento.

Un conjunto de datos de viviendas de una ciudad de la década de 1960 contiene datos sobre precios de viviendas que reflejan prácticas 
de préstamos discriminatorias vigentes durante esa década.

### Sesgo de automatización
El sesgo de automatización es la tendencia a favorecer los resultados que se generan mediante sistemas automatizados sobre los 
que se generan a través de aquellos que no lo son, sin importar la tasa de error de cada uno.

Los profesionales del AA que trabajaban para un fabricante de ruedas dentadas estaban ansiosos por implementar el nuevo modelo 
“innovador” que entrenaron para identificar defectos dentales, hasta que el supervisor de la fábrica señaló que las tasas de precisión 
y recuperación del modelo eran un 15% más bajas que las de los inspectores humanos.

### Sesgo de selección

El sesgo de selección tiene lugar cuando los ejemplos de un conjunto de datos se eligen de un modo que no refleja su distribución en el mundo real. 
El sesgo de selección puede adoptar muchas formas diferentes, como el sesgo de cobertura, el sesgo de no respuesta y el sesgo de muestreo.

#### Sesgo de cobertura

El sesgo de cobertura se produce si los datos no se seleccionan de forma representativa.

Se entrena un modelo para predecir las ventas futuras de un producto nuevo en función de encuestas telefónicas realizadas con 
una muestra de consumidores que compraron el producto. En cambio, no se encuestaron a los consumidores que decidieron comprar 
un producto de la competencia, por lo que este grupo no estuvo representado en los datos de entrenamiento.

#### Sesgo de no respuesta

El sesgo de no respuesta (también conocido como sesgo de participación) ocurre si los datos no resultan representativos debido 
a interrupciones en la participación en el proceso de recopilación de datos.

Se entrena un modelo para predecir las ventas futuras de un producto nuevo en función de encuestas telefónicas realizadas con
una muestra de consumidores que compraron el producto y con una muestra de consumidores que compraron un producto de la competencia. 
Los consumidores que compraron el producto de la competencia tenían un 80% más de probabilidades de rechazar completar la encuesta,
y sus datos estaban subrepresentados en la muestra.

#### Sesgo muestral

El sesgo muestral ocurre si no se usa una aleatorización adecuada durante la recopilación de datos.

Se entrena un modelo para predecir las ventas futuras de un producto nuevo a partir de encuestas telefónicas realizadas con una 
muestra de consumidores que compraron el producto y con una muestra de consumidores que compraron un producto de la competencia. 
En lugar de seleccionar a los consumidores de manera aleatoria, el encuestador eligió a los primeros 200 consumidores que respondieron
un correo electrónico, quienes posiblemente estaban más entusiasmados acerca del producto que los compradores promedio.

### Sesgo de correspondencia

El sesgo de correspondencia es la tendencia a generalizar la realidad de los individuos para todo el grupo al que pertenecen. El sesgo 
de atribución grupal a menudo se manifiesta de las siguientes formas.

#### Sesgo endogrupal

El sesgo endogrupal es una preferencia por los miembros de tu propio grupo al que también perteneces o por características que también compartes.

Dos profesionales del AA que entrenan un modelo para filtrar currículums de desarrolladores de software están predispuestos a 
creer que los postulantes que asistieron a la misma academia de informática que ellos están más calificados para el puesto.

#### Sesgo de homogeneidad de los demás

El sesgo de homogeneidad de los demás es una tendencia a estereotipar a los miembros individuales de un grupo al que no perteneces
o a ver sus características como más uniformes.

Dos profesionales del AA que entrenan un modelo de selección de currículums para desarrolladores de software están predispuestos a 
creer que todos los postulantes que no asistieron a una academia de informática no tienen la experiencia suficiente para el puesto.

### Sesgo implícito

El sesgo implícito tiene lugar cuando se realizan suposiciones en función de modelos mentales propios y experiencias personales que 
no aplican necesariamente a un nivel más general.

Un profesional del AA que entrena un modelo de reconocimiento de gestos usa un movimiento de cabeza como un atributo para indicar 
que una persona está comunicando la palabra "no". Sin embargo, en algunas regiones del mundo, un movimiento de cabeza significa en realidad "sí".

### Sesgo de confirmación

El sesgo de confirmación se produce cuando los creadores de modelos procesan inconscientemente los datos de maneras que afirman
sus hipótesis y creencias preexistentes.

Un profesional del AA está creando un modelo que predice la agresividad de los perros en función de una variedad de características (altura, peso, raza y entorno).
El practicante tuvo un encuentro desagradable con un caniche toy cuando era niño y, desde entonces, ha asociado a la raza con agresión. Cuando se 
seleccionaron los datos de entrenamiento del modelo, el profesional descartó de forma inconsciente las características que proporcionaban 
evidencia de docilidad en perros más pequeños.

### Sesgo del investigador

El sesgo del experimentador ocurre cuando quien crea el modelo sigue entrenándolo hasta que produce un resultado que se alinea con su hipótesis original.

Un profesional de la AA está creando un modelo que predice la agresividad de los perros en función de distintas características (altura, peso, raza, entorno).
El practicante tuvo un encuentro desagradable con un caniche toy cuando era niño y, desde entonces, ha asociado a la raza con agresión. Cuando el modelo entrenado 
predijo que la mayoría de los caniches toy eran relativamente dóciles, el profesional volvió a entrenar el modelo varias veces hasta que produjo un resultado que
muestra que los caniches más pequeños son más violentos.

## Identificación del sesgo

A medida que preparas tus datos para el entrenamiento y la evaluación del modelo, es importante tener en cuenta los problemas de equidad
y auditar las posibles fuentes de sesgo para que puedas mitigar sus efectos de forma proactiva antes de lanzar el modelo a producción.

¿Dónde podría aparecer el sesgo? A continuación, se incluyen algunos indicadores de advertencia que debes tener en cuenta en tu conjunto de datos.

### Atributos con valores faltantes

Si tu conjunto de datos contiene una gran cantidad de ejemplos en los que uno o más atributos no tienen valores, esto podría indicar 
que algunas características clave de tu conjunto de datos están subrepresentadas.

### Atributos con valores inesperados

Cuando exploras los datos, debes buscar también ejemplos que contengan atributos con valores que se destaquen por ser atípicos o inusuales.
Estos valores de atributos inesperados podrían indicar problemas que ocurrieron durante la recopilación de datos, o bien otras imprecisiones que podrían generar sesgo.

### Sesgo de datos

Cualquier tipo de sesgo en tus datos, en el que ciertos grupos o características puedan estar sub o sobrerrepresentados en relación con 
su prevalencia en el mundo real, puede introducir sesgos en tu modelo.

Cuando se audita el rendimiento del modelo, es importante no solo observar los resultados de forma agregada, sino también desglosarlos
por subgrupo. Por ejemplo, en el caso de nuestro modelo de adoptabilidad de perros rescatados, para garantizar la equidad, no es 
suficiente con observar la precisión general. También debemos auditar el rendimiento por subgrupo para asegurarnos de que el modelo
funcione igual de bien para cada raza, grupo de edad y grupo de tamaño de perro.

## Mitigación del sesgo

Una vez que se identifica una fuente de sesgo en los datos de entrenamiento, podemos tomar medidas proactivas para mitigar sus efectos. Existen dos estrategias
principales que suelen emplear los ingenieros de aprendizaje automático (AA) para corregir el sesgo:
- Aumentar los datos de entrenamiento
- Ajustar la función de pérdida del modelo

### Aumento de los datos de entrenamiento

Si una auditoría de los datos de entrenamiento reveló problemas con datos faltantes, incorrectos o sesgados, a menudo, la forma
más directa de abordar el problema es recopilar datos adicionales.

Sin embargo, si bien aumentar los datos de entrenamiento puede ser ideal, la desventaja de este enfoque es que también puede ser inviable, 
ya sea por falta de datos disponibles o por restricciones de recursos que impiden la recopilación de datos. Por ejemplo, recopilar más 
datos puede ser demasiado costoso o requerir mucho tiempo, o no ser viable debido a restricciones legales o de privacidad.

### Cómo ajustar la función de optimización del modelo

En los casos en que no sea viable recopilar datos de entrenamiento adicionales, otro enfoque para mitigar el sesgo es ajustar 
la forma en que se calcula la pérdida durante el entrenamiento del modelo. Por lo general, usamos una función de optimización como 
la pérdida de registro para penalizar las predicciones incorrectas del modelo. Sin embargo, la pérdida de registro no tiene en cuenta
la membresía del subgrupo. Por lo tanto, en lugar de usar la pérdida de registro, podemos elegir una función de optimización diseñada 
para penalizar los errores de una manera que tenga en cuenta la equidad y que contrarreste los desequilibrios que identificamos en nuestros
datos de entrenamiento.

La biblioteca de **Model Remediation de TensorFlow** proporciona utilidades para aplicar dos técnicas diferentes de mitigación de sesgos durante el entrenamiento del modelo:
- **MinDiff**: Su objetivo es equilibrar los errores de dos segmentos de datos diferentes (estudiantes hombres o mujeres en comparación con estudiantes no binarios) agregando una penalización por las diferencias en las distribuciones de predicciones de los dos grupos.
- **Sincronización contrafáctica de logit**: La sincronización contrafáctica de logit (CLP) tiene como objetivo garantizar que cambiar un atributo sensible de un ejemplo determinado no altere la predicción del modelo para ese ejemplo. Por ejemplo, si un conjunto de datos de entrenamiento contiene dos ejemplos cuyos valores de atributos son idénticos, excepto que uno tiene un valor gender de male y el otro tiene un valor gender de nonbinary, la CLP agregará una penalización si las predicciones de estos dos ejemplos son diferentes.

- Las técnicas que elijas para ajustar la función de optimización dependen de los casos de uso del modelo. En la siguiente sección, analizaremos con mayor detalle cómo abordar la tarea de evaluar un modelo en cuanto a su equidad considerando estos casos de uso.

## Evaluación de sesgos

Cuando se evalúa un modelo, las métricas calculadas con una prueba o validación completa no siempre brindan una imagen precisa de cuán justo es el modelo. 
Un buen rendimiento del modelo general puede esconder problemas de rendimiento en subgrupos, lo que puede resultar en predicciones sesgadas. 
Usar métricas de rendimiento agregadas, como precisión, recuperación, y exactitud no necesariamente para exponer estos problemas.

Supongamos que el modelo de clasificación de admisiones selecciona 20 estudiantes para admitir universidad a partir de un conjunto de 100 candidatos, 
que pertenecen a dos grupos demográficos: el grupo mayoritario (azul, 80 estudiantes) y el grupo minoritario (naranja, 20 estudiantes).
El modelo debe admitir a los estudiantes calificados de una manera justa para candidatos en ambos grupos demográficos.

¿Cómo debemos evaluar las predicciones del modelo en cuanto a la equidad? Hay una gran variedad de métricas que podemos considerar, cada una
de las cuales proporciona una definición de "equidad". En las siguientes secciones, exploraremos estas métricas de equidad: 
- Paridad demográfica
- Igualdad de oportunidades
- Equidad contrafáctica.

## Paridad demográfica

Un método que podemos usar para evaluar las predicciones de equidad de nuestro modelo es comparar la tasa de admisión del grupo mayoritario y del grupo minoritario. 
Si las dos tasas de admisión son iguales, las predicciones del modelo muestran **Paridad demográfica**: más probabilidades de que los estudiantes 
ingresen en la universidad no varía por el grupo demográfico.

|                     | Majority group | Minority group |
|---------------------|----------------|----------------|
| **Accepted**        | 16             | 4              |
| **Rejected**        | 64             | 16             |
| **Acceptance Rate** | 20%            | 20%            |

### Ventajas y desventajas
La ventaja principal es que garantiza que tanto los grupos mayoritarios como los minoritarios estén representados de estudiantes 
en la misma proporción que en el grupo de candidatos.

Su desventaja es qué no tiene en cuenta la distribución de las predicciones para cada grupo demográfico cuando evalúa.

<table>
  <tr>
    <th></th>
    <th colspan="2">Majority group</th>
    <th colspan="2">Minority group</th>
  </tr>
  <tr>
    <th></th>
    <th>Accepted</th>
    <th>Rejected</th>
    <th>Accepted</th>
    <th>Rejected</th>
  </tr>
  <tr>
    <td><b>Qualified</b></td>
    <td>16</td><td>19</td><td>4</td><td>11</td>
  </tr>
  <tr>
    <td><b>Unqualified</b></td>
    <td>0</td><td>45</td><td>0</td><td>5</td>
  </tr>
</table>

$$
\text{Majority acceptance rate} = \frac{\text{qualified majority students accepted}}{\text{total qualified majority students}} = \frac{16}{35} = 46\%
$$

$$
\text{Minority acceptance rate} = \frac{\text{qualified minority students accepted}}{\text{total qualified minority students}} = \frac{4}{15} = 27\%
$$

Aunque ambos grupos tienen una tasa de aceptación general del 20%, lo que satisface paridad demográfica, la tasa de aceptación de
la mayoría de los estudiantes calificados es del 46% mientras que la tasa de aceptación de estudiantes de minorías calificadas es de solo un 27%.

En casos como este, cuando la distribución de una etiqueta preferida (como “calificado”) varía mucho entre ambos grupos, la paridad 
demográfica no sería la métrica óptima para evaluar la equidad. En la próxima veremos una métrica alternativa de equidad, 
**igualdad de oportunidades** que toma en cuenta estas diferencias.

## Igualdad de oportunidades

De manera alternativa, podríamos comparar las tasas de aceptación solo de los candidatos del grupo mayoritario y del grupo minoritario. 
Si las tasas de aceptación de estudiantes calificados en ambos grupos son los mismos, el modelo exhibe **igualdad de oportunidades**: 
los estudiantes con nuestra etiqueta preferida ("calificado para admisión") tienen un más probabilidades de ser admitido, independientemente 
del grupo demográfico al que pertenezcan.

Supongamos que el modelo de admisiones acepta 14 candidatos del grupo mayoritario, y 6 candidatos del grupo minoritario. Las decisiones 
del modelo satisfacen igualdad de oportunidades, ya que la tasa de aceptación de las mayorías calificadas y de candidatos minoritarios calificados es del 40%.

### Ventajas y desventajas

La ventaja es que permite que la probabilidad del modelo de predicciones varié a lo largo de los grupos demográficos, considerando
que el modelo es igual de exitoso al predecir la etiqueta deseada para ambos grupos.

Una desventaja de la igualdad de oportunidades es que está diseñada para usarse en casos en los que hay una etiqueta preferida clara. 
Si es igualmente importante que el modelo prediga tanto la clase positiva (“calificado para admisión”) y negativa ("no calificada para la admisión") 
para todos los grupos demográficos, puede que tenga sentido usar la métrica** probabilidades equitativas**, que imponen tasas de éxito iguales para ambas etiquetas.

## Equidad contrafáctica

Hasta ahora, en nuestras discusiones sobre métricas de equidad, asumimos que nuestro entrenamiento y los ejemplos de prueba contienen 
los datos demográficos integrales de los subgrupos que se están evaluando. Pero a menudo este no es el caso.

Supongamos que nuestro conjunto de datos de admisiones no contiene datos demográficos completos. En cambio, la pertenencia a un
grupo demográfico se registra solo para un pequeño porcentaje de ejemplos, como los estudiantes que optaron por identificar qué
grupo a los que pertenecían.

En este caso, no es factible evaluar las predicciones del modelo para ningún segmento demográfico paridad o igualdad de oportunidades, 
porque no tenemos datos demográficos para el 94% de nuestros ejemplos. Sin embargo, el 6% de los ejemplos que sí contienen de 
características demográficas, de todos modos podemos comparar pares de predicciones individuales (un candidato mayoritario o minoritario) 
y ver si han sido tratadas equitativamente por el modelo.

Por ejemplo, supongamos que revisamos minuciosamente los datos de los atributos disponibles para dos candidatos (uno en el grupo mayoritario y otro en la minoría grupo) 
y han determinado que están idénticamente calificados para la admisión en todos los aspectos. Si el modelo hace la misma predicción para ambos
candidatos (rechaza ambos o acepta a ambos candidatos), se dice que satisface la política contrafáctica equidad para estos ejemplos. 
La equidad contrafáctica estipula que dos ejemplos idénticos en todo sentido, excepto por un atributo sensible determinado 
(en este caso, pertenencia a un grupo demográfico), deberían generar la misma predicción para el modelo.

### Ventajas y desventajas
La ventaja principal es que permite evaluar predicciones cuando otras métricas no son adecuadas. Como ya se explicó para el caso
en que los valores de un atributo importante falten en general.

Además, como la paridad demográfica e igualdad de oportunidades son métricas basadas en agregación, pueden esconder errores de 
sesgo que afecten a las predicciones de instancias individuales, que puede ser evaluado con equidad contrafactual.

La desventaja principal de la equidad contrafáctica es que no proporcionan una visión holística del sesgo en las predicciones del modelo.
Identificar y corregir unas cuantas desigualdades en pares de ejemplos puede no ser suficiente para abordar los problemas de sesgo 
sistémico que afectan a subgrupos completos de ejemplos.

En los casos en que sea posible, los profesionales pueden considerar hacer una combinación un análisis de equidad (mediante una métrica
como la paridad demográfica o la igualdad de oportunidad), así como un análisis de equidad contrafáctica para obtener la mayor variedad 
de perspectivas sobre posibles problemas de sesgo que necesitan corrección.

### Resumen

Paridad demográfica, igualdad de oportunidades, y la equidad contrafáctica proporcionan diferentes definiciones matemáticas de 
equidad para las predicciones de modelos. Y esas son solo tres posibles y formas de cuantificar la equidad. Algunas definiciones 
de equidad son incluso mutuamente incompatibles, lo que significa que puede ser imposible satisfacerlos simultáneamente por un 
las predicciones del modelo dado.

Entonces, ¿cómo elegir la solución "correcta" de equidad para tu modelo? Debes considerar el contexto en el que se usa y los 
objetivos generales que quieres lograr. Por ejemplo, ¿el objetivo es lograr una representación equitativa (en este caso, la 
paridad demográfica puede ser la métrica óptima) o lograr la igualdad de oportunidades (aquí, la igualdad de oportunidades puede ser métricas)?