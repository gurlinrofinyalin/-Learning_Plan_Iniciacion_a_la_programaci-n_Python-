import numpy as np
import pandas as pd # <-- Necesitas importar pandas para cargar CSV

# --- PASO 1: CARGAR LOS DATOS ---
# URL del archivo CSV del dataset de Titanic
url_datos = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url_datos)

# --- PASO 2: PREPARAR LOS DATOS (X e y) ---
# Para este ejemplo, seleccionaremos algunas características y manejaremos valores nulos simples.

# Codificación de variables categóricas:
# df['Sex'] selecciona la columna 'Sex'.
# .map({'male': 0, 'female': 1}) es una función de Series de pandas que
# reemplaza los valores de la columna 'Sex' ('male' y 'female') por los valores numéricos correspondientes (0 y 1).
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Manejo de valores nulos:
# df['Age'].mean() calcula la media (promedio) de los valores en la columna 'Age'.
# .fillna(...) es una función de Series de pandas que rellena los valores nulos (NaN) en la columna.
# En este caso, rellena los NaN con la media calculada de la columna 'Age'.
# inplace=True significa que el cambio se realiza directamente sobre el DataFrame original 'df',
# sin necesidad de reasignar la columna. Si fuera False, devolvería una nueva Serie modificada.

# CAMBIAMOS
#df['Age'].fillna(df['Age'].mean(), inplace=True)
#df['Fare'].fillna(df['Fare'].mean(), inplace=True) # También por si hay NaNs en Fare

# POR ,  para que  los cambios se reflejen en una copia y no en el dataframe original
#La advertencia se refiere a un problema común en Pandas conocido como "SettingWithCopyWarning" o
# situaciones donde Python puede crear una "copia" de una parte del DataFrame para operar sobre ella.
# Al usar inplace=True en una copia, tus cambios no se reflejarían en el DataFrame original.
# Aunque en tu caso parece que sí se aplican, Pandas prefiere que seas explícito para evitar ambigüedades.
df['Age'] = df['Age'].fillna(df['Age'].mean()) # crea una serie temporal
# df['Age'] (lado derecho)  selecciona la columna 'Age' del DataFrame df  donde se reemplazan valores NaN por la media
# df['Age'].mean() clacula la media
# fillna  q reemplaza valores NaNs y los reeemplaza con la media
# df['Age']  = el resultado es una nueva serie con los valores nulos reemplazados con la media
df['Fare'] = df['Fare'].fillna(df['Fare'].mean())


#df['Age'] (lado derecho): Esto selecciona la columna 'Age' del DataFrame df.
# .fillna(df['Age'].mean()): Sobre esa columna 'Age' (que es una Serie de pandas),
# se llama al método fillna().
#  Este método busca todos los valores NaN (nulos) dentro de esa Serie y los reemplaza con el valor que
#   le pasamos como argumento, que en este caso es la media de la propia columna 'Age'.
#Importante: Cuando no usas inplace=True,
# el método fillna() devuelve una nueva Serie con los valores nulos ya rellenados.
#  No modifica la Serie original df['Age'] "en su lugar".
#df['Age'] = ... (lado izquierdo):
# El resultado de esa nueva Serie (con los nulos rellenados) se asigna de nuevo a la columna 'Age'
# del DataFrame df.
# LA MEDIA SE CALCULA CON
#df['Age'].mean(): Esta parte de la expresión calcula el valor de la media de la columna 'Age'.
# El resultado de esta operación es un número único (por ejemplo, 29.69911764705882).
# fillna(...): La función fillna() está diseñada para tomar un argumento:
# el valor con el que quieres reemplazar los NaNs osease la media



"""
En resumen:
No se crea una copia de todo el DataFrame. Solo se está operando sobre una columna específica.
Se crea una nueva Serie temporal con los cambios para esa columna.
Esa nueva Serie se utiliza para sobrescribir la columna original 'Age' en el DataFrame df.
Esta forma es la recomendada porque evita las ambigüedades que a veces surgen con el inplace=True 
en operaciones encadenadas, donde Pandas podría, bajo ciertas circunstancias, 
estar trabajando sobre una "copia" interna de una vista 
y los cambios no se reflejarían en el DataFrame original de forma fiable. 
Al reasignar explícitamente, te aseguras de que el DataFrame df se actualice correctamente.
"""

# Seleccionar las características (X) y la variable objetivo (y)
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
# df[features] selecciona las columnas de características del DataFrame.

# .values es un atributo de DataFrame/Series de pandas que devuelve los datos como un array de NumPy.
# Scikit-learn prefiere arrays de NumPy como entrada.
X = df[features].values
# df['Survived'] selecciona la columna objetivo.
# .values convierte esta columna en un array de NumPy.
y = df['Survived'].values

"""
En el contexto de X.shape y y.shape, la palabra "forma" se refiere a las dimensiones o estructura de tus datos.
palabra inglesa "shape".
Cuando imprimes X.shape o y.shape, el resultado es una tupla (una secuencia ordenada de elementos) 
IMPORTANTE
que te dice cuántas "dimensiones" tiene tu array (o matriz) 
y cuántos elementos hay en cada dimensión.


Para ser más específico:
X.shape:
X representa tus características o variables independientes (lo que usas para predecir). 
En el aprendizaje automático, X suele ser una matriz o tabla.
X.shape te devolverá una tupla de la forma (número_de_filas, número_de_columnas).

El primer número (número de filas) indica la cantidad de muestras o registros que tienes en tu 
conjunto de datos. 
En el ejemplo del Titanic, cada fila es un pasajero.

El segundo número (número de columnas) indica la cantidad de características o variables que estás usando 
para cada muestra (por ejemplo, 'Pclass', 'Sex', 'Age', 'Fare', etc.).

y.shape:
y representa tu variable objetivo o dependiente (lo que quieres predecir). 
En el aprendizaje automático, y suele ser un vector (una sola columna de valores).
y.shape te devolverá una tupla de la forma (número_de_elementos,).

El primer (y único) número indica la cantidad de elementos o valores en tu variable objetivo.
 Este número siempre debe coincidir con el número de filas de X, 
 ya que hay un valor objetivo para cada muestra. 
 La coma al final (, ) indica que es una tupla de un solo elemento, no solo un número.

En resumen, shape te da la "geometría" de tus datos: 
cuántas observaciones tienes y cuántas características tiene cada observación. 
Es fundamental para asegurarte de que tus datos tienen el formato correcto para los algoritmos de 
Machine Learning.
"""

print("Forma de X (Características):", X.shape)
print("Forma de y (Objetivo):", y.shape)
print("\nPrimeras 5 filas de X:\n", X[:5])
print("\nPrimeras 5 etiquetas de y:\n", y[:5])
# --- FIN DE LA CARGA Y PREPARACIÓN DE DATOS ---



from sklearn import preprocessing
# Básicamente, los algoritmos de aprendizaje automático se benefician de la estandarización del conjunto de datos.
# Si hay algunos valores atípicos o campos de diferentes escalas en tu conjunto de datos, tienes que corregirlos.
# El paquete de preprocesamiento de Scikit Learn proporciona varias funciones de utilidad comunes
# y clases transformadoras para cambiar vectores de características en bruto a una forma adecuada de
# vector para modelar.
"""EXPLICACION
paso fundamental en el preprocesamiento de datos en el aprendizaje automático,
 conocido como estandarización o escalado de características.

"Básicamente, los algoritmos de aprendizaje automático se benefician de la estandarización del conjunto de 
datos." Significa que muchos algoritmos de Machine Learning funcionan mejor o de manera más eficiente 
cuando las características (las columnas de tu X) tienen una escala similar.

Por ejemplo, algoritmos basados en distancias (como K-Nearest Neighbors - KNN, o Support Vector Machines 
- SVM, que es el que estás usando) o los que usan descenso de gradiente (como las redes neuronales), 
pueden verse desproporcionadamente influenciados por características con rangos de valores muy grandes,
 si no están estandarizadas. Una característica que va de 0 a 100,000 podría "dominar" sobre una que va 
 de 0 a 10, incluso si esta última es más importante. 
 La estandarización ayuda a evitar esto.

"Si hay algunos valores atípicos o campos de diferentes escalas en tu conjunto de datos, tienes que 
corregirlos."
"Valores atípicos" (Outliers): Son puntos de datos que se desvían significativamente de la mayoría de 
los otros datos. Pueden distorsionar la media y la desviación estándar, lo que a su vez afecta la 
estandarización y el rendimiento del modelo. Aunque la estandarización no "corrige" los valores atípicos 
en sí, los algoritmos suelen ser más sensibles a ellos si las características no están en una escala 
comparable.

"Campos de diferentes escalas" (Features of different scales): Esto se refiere a que tus diferentes 
características (columnas) pueden tener rangos de valores muy distintos. Por ejemplo, la edad de un 
pasajero del Titanic puede ir de 0 a ~80, mientras que la tarifa ('Fare') podría ir de 0 a ~500. 
Si no se escalan, la "tarifa" podría tener un peso indebido en el modelo simplemente por su magnitud 
numérica.

"Tienes que corregirlos": No es una corrección en el sentido de eliminar errores, sino de transformar 
los datos para que sean adecuados para el modelo.
"El paquete de preprocesamiento de Scikit Learn proporciona varias funciones de utilidad comunes y 
clases transformadoras para cambiar vectores de características en bruto a una forma adecuada de vector 
para modelar."

sklearn.preprocessing: Este es el módulo dentro de la biblioteca Scikit-learn que contiene herramientas 
para preparar tus datos.
"Funciones de utilidad comunes y clases transformadoras": Se refiere a herramientas específicas como 
StandardScaler (que estás usando), MinMaxScaler, Normalizer, etc. 
Estas son "clases transformadoras" porque tienen métodos fit() (aprenden los parámetros de la transformación 
de tus datos, como la media y la desviación estándar para StandardScaler) 
y transform() (aplican esa transformación a tus datos).

"Cambiar vectores de características en bruto a una forma adecuada de vector para modelar": 
Es el objetivo final. 
La estandarización (StandardScaler) transforma tus características para que tengan una media de 0 
y una desviación estándar de 1. 
Esto asegura que todas las características tengan el mismo "peso" inicial 
y estén en una escala comparable, lo que mejora la estabilidad y el rendimiento de muchos algoritmos de aprendizaje automático.

"""
"""
La desviación estándar es una medida de la dispersión o variabilidad de un conjunto de datos. 
Indica cuánto se alejan, en promedio, los valores individuales de la media del conjunto.
import numpy as np
datos = np.array([10, 20, 30, 40, 50])
print("Media:", np.mean(datos))
print("Desviación estándar:", np.std(datos))
#Media: 30.0
#Desviación estándar: 14.142135623730951
"""

X = preprocessing.StandardScaler().fit(X).transform(X)
#preparar tus datos, asegurando que todas tus características estén en una escala similar para que tu
# modelo de Machine Learning (como el SVM que usas) pueda aprender de ellas de manera efectiva
# y sin sesgos por la magnitud de los valores.

from sklearn.model_selection import train_test_split
# Tienes que dividir tu conjunto de datos en conjuntos de entrenamiento y prueba
# para entrenar tu modelo y luego probar la precisión del modelo por separado.
# Scikit Learn puede dividir arreglos o matrices en subconjuntos aleatorios de entrenamiento y prueba por ti en una línea de código.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#los valores objetivo (y_train).
#las características (X_train)
# datos que nunca ha visto en el entrenamiento NUEVOS (X_test)
# y_test  son las respuestas correctas  de X_train, se compraran con yhat
# yhat  son las prediccones sobre el conjunto NUEVO de prueba y_test
#
"""
Las variables X_train, X_test, y_train, y y_test son el resultado de esta división:

X (Características / Variables Independientes): 
Son las columnas de tu conjunto de datos que utilizas como "entrada" para hacer una predicción. 
Por ejemplo, en el dataset de Titanic, serían la clase del pasajero, la edad, el sexo, la tarifa, etc.

y (Objetivo / Variable Dependiente): 
Es la columna de tu conjunto de datos que quieres predecir. 
En el ejemplo del Titanic, sería si el pasajero sobrevivió o no.

Los conjuntos divididos:
X_train (Conjunto de Características de Entrenamiento)
¿Qué es? 
Son las características (X) de la porción de datos que se usa para entrenar el modelo.
¿Para qué se usa? 
IMPORTANTE
El algoritmo de aprendizaje automático "aprende" de estos datos. 
Ajusta sus parámetros internos para encontrar patrones y relaciones entre las características 
de X_train y los resultados en y_train. 
Es como el material de estudio para el modelo.


y_train (Conjunto de Objetivo de Entrenamiento)
¿Qué es? 
Es la variable objetivo (y) correspondiente a las características de X_train.
¿Para qué se usa? 
Es la "respuesta correcta" para cada fila en X_train. 
IMPORTANTE
El modelo utiliza estos valores para saber si está haciendo bien las cosas mientras aprende.


X_test (Conjunto de Características de Prueba)
¿Qué es? 
Son las características (X) de la porción de datos que se usa para evaluar el modelo. 
IMPORTANTE
Estos datos son completamente nuevos para el modelo; nunca los ha visto durante el entrenamiento.
¿Para qué se usa? 
IMPORTANTE
Una vez que el modelo ha sido entrenado, se le da X_test y se le pide que haga predicciones (yhat). 
Esto simula cómo se comportaría el modelo en el "mundo real" con datos que no conoce.


y_test (Conjunto de Objetivo de Prueba)
¿Qué es? 
Es la variable objetivo (y) correspondiente a las características de X_test.
¿Para qué se usa? 
Son las "respuestas correctas" para X_test. 
Una vez que el modelo hace sus predicciones (yhat) sobre X_test, 
comparas esas predicciones con y_test para calcular métricas de rendimiento
 (como la precisión, la matriz de confusión, etc.) y ver qué tan bien generaliza tu modelo.
 

¿Por qué se hace esta división?
El objetivo principal de dividir los datos es evitar el sobreajuste (overfitting). 
Si entrenas y pruebas tu modelo con los mismos datos, 
IMPORTANTE
el modelo podría simplemente "memorizar" las respuestas en lugar de aprender los patrones subyacentes. 
Esto resultaría en un modelo que se desempeña muy bien en los datos de entrenamiento, 
pero muy mal con datos nuevos.

Al separar los datos de entrenamiento y prueba, obtienes una evaluación más honesta 
y realista de la capacidad de tu modelo para generalizar y hacer predicciones precisas sobre datos futuros 
y desconocidos.
"""


from sklearn import svm
# Luego puedes configurar tu algoritmo.
# Por ejemplo, puedes construir un clasificador utilizando un algoritmo de clasificación de vectores
# de soporte.
# Llamamos a nuestra instancia estimadora CLF y inicializamos sus parámetros.
clf = svm.SVC(gamma=0.001, C=100.)

"""
svm: Esta es la biblioteca (o módulo) dentro de Scikit-learn que contiene varias implementaciones 
de Máquinas de Soporte Vectorial. 
No es el algoritmo en sí mismo, sino el contenedor de ellos.

svm.SVC: Este es el algoritmo específico de clasificación de vectores de soporte
 (Support Vector Classifier). 
 SVC es una clase que representa una versión particular del algoritmo SVM para tareas de clasificación.

clf = svm.SVC(...): Aquí es donde creas una instancia de la clase SVC. 
Es decir, clf es tu objeto concreto (tu "modelo") basado en el algoritmo SVC,
 y es a esta instancia a la que le pasas y "inicializas sus parámetros" (gamma, C, etc.).

Así que, la forma correcta de verlo sería:
svm: El módulo/paquete que contiene la funcionalidad SVM.
SVC: La clase/algoritmo de clasificación de vectores de soporte.
clf: La instancia concreta de ese algoritmo, con sus parámetros inicializados y lista para ser entrenada.
"""

"""
En la línea clf = svm.SVC(gamma=0.001, C=100.), estás creando una instancia de un clasificador de 
Máquinas de Soporte Vectorial (Support Vector Classifier - SVC), 
y le estás pasando dos parámetros muy importantes: gamma y C.

Estos parámetros son cruciales porque controlan cómo el modelo SVM construirá su línea 
o superficie de decisión (el límite que separa las diferentes clases de tus datos).

gamma (en tu caso, 0.001)
Significado: El parámetro gamma define el alcance de la influencia de un solo punto de entrenamiento. 
Se puede pensar en él como la "sensibilidad" del modelo a puntos de datos individuales.
Valores altos de gamma: 
Significa que un solo punto de entrenamiento tiene una influencia muy localizada o cercana. 
El modelo se vuelve muy sensible a los puntos de datos individuales, 
lo que puede llevar a un sobreajuste (overfitting). 
Es como si el modelo intentara encajar perfectamente cada punto de entrenamiento, 
creando límites de decisión muy complejos y "sinuosos".

Valores bajos de gamma: 
Significa que un punto de entrenamiento tiene una influencia más amplia o lejana. 
El modelo busca límites de decisión más suaves y generales. 
Un gamma muy bajo puede llevar a un subajuste (underfitting), 
donde el modelo es demasiado simple y no captura bien las relaciones en los datos.

gamma es especialmente relevante cuando se utilizan ciertos tipos de kernels, 
como el kernel RBF (Radial Basis Function), que es el predeterminado para SVC.

C (en tu caso, 100.)
Significado: El parámetro C es el parámetro de regularización. 
Controla la penalización que el modelo recibe por los puntos de entrenamiento que están mal 
clasificados o que se encuentran dentro del margen. 
Es un equilibrio entre tener un margen amplio y clasificar correctamente todos los puntos de entrenamiento.

Valores altos de C: 
Imponen una alta penalización por los errores de clasificación de los puntos de entrenamiento. 
El modelo intentará clasificar correctamente la mayor cantidad posible de puntos de entrenamiento, 
incluso si eso significa crear un límite de decisión más complejo y un margen más estrecho. 
Esto puede llevar a sobreajuste (overfitting), ya que el modelo se vuelve muy rígido para acomodar a casi 
todos los puntos de entrenamiento.
Valores bajos de C: 
Imponen una baja penalización por los errores de clasificación.
 El modelo permite más puntos mal clasificados en el conjunto de entrenamiento para lograr un límite de 
 decisión más simple y un margen más amplio. 
 Esto puede llevar a subajuste (underfitting), ya que el modelo podría ser demasiado general 
 y no capturar suficiente detalle.

En resumen, tanto gamma como C son hiperparámetros que debes ajustar cuidadosamente para encontrar 
el equilibrio adecuado entre el sobreajuste y el subajuste, 
y lograr que tu modelo generalice bien a datos nuevos. 
El proceso de encontrar los mejores valores para estos parámetros se conoce como optimización de 
hiperparámetros.
"""



"""
# Ahora puedes entrenar tu modelo con el conjunto de entrenamiento.
# Al pasar nuestro conjunto de entrenamiento al método fit,
#  el modelo CLF aprende a clasificar casos desconocidos.
# X_train,  fila del material de estudio para el modelo
# y_train   la respuesta correcta para cada fila de X_train, para comprobar si aprende bien
"""
clf.fit(X_train, y_train) #clf aprende a identificar los patrones y la relación entre
# las características (X_train)  y los valores objetivo (y_train).
"""
X_train (Conjunto de Características de Entrenamiento)
Son las características (X) de la porción de datos que se usa para entrenar el modelo.
El algoritmo de aprendizaje automático "aprende" de estos datos. 
Ajusta sus parámetros internos para encontrar patrones y relaciones entre las características 
de X_train y los resultados en y_train. 
Es como el material de estudio para el modelo.

y_train (Conjunto de Objetivo de Entrenamiento) 
Es la variable objetivo (y) correspondiente a las características de X_train. 
Es la "respuesta correcta" para cada fila en X_train
El modelo utiliza estos valores para saber si está haciendo bien las cosas mientras aprende.
"""


#PREDICCIONES
# Luego, podemos usar nuestro conjunto de prueba para hacer predicciones.
# Y el resultado nos dice cuál es la clase de cada valor desconocido.
yhat = clf.predict(X_test)
print("Predicciones del modelo (yhat):")
print(yhat)

print("Primeras 10 predicciones (yhat[:10]):")
print(yhat[:10]) # Muestra las primeras 10 predicciones

print("Últimas 10 predicciones (yhat[-10:]):")
print(yhat[-10:]) # Muestra las últimas 10 predicciones

print("Número total de predicciones:", yhat.shape[0])
"""
X_test (Conjunto de Características de Prueba) 
Son las características (X) de la porción de datos que se usa para evaluar el modelo. 
Estos datos son completamente nuevos para el modelo; nunca los ha visto durante el entrenamiento.
Una vez que el modelo ha sido entrenado, se le da X_test y se le pide que haga predicciones (yhat). 
Esto simula cómo se comportaría el modelo en el "mundo real" con datos que no conoce.
"""
"""
La línea yhat = clf.predict(X_test) es el paso donde el modelo de aprendizaje automático, 
que ya ha sido entrenado, hace sus predicciones sobre datos nuevos y no vistos.
clf: Es tu modelo de Support Vector Classifier (SVC) que ya ha sido entrenado 
(es decir, ya ha pasado por la fase clf.fit(X_train, y_train)). Durante el entrenamiento, 
clf aprendió a identificar los patrones y la relación entre las características (X_train) 
y los valores objetivo (y_train).

.predict(X_test):
predict() es un método que todos los estimadores (modelos) en Scikit-learn tienen. 
Su propósito es generar una salida (predicción) basándose en una nueva entrada de características.

X_test son las características del conjunto de prueba. Recuerda que estos son los datos que el modelo nunca ha visto durante su fase de entrenamiento.

yhat = ...:

El resultado de clf.predict(X_test) es un array de NumPy que contiene las predicciones del modelo. Por cada fila de X_test, predict() devuelve el valor que el modelo predice para la variable objetivo.

Esta variable yhat (que a menudo se pronuncia "y-hat") se utiliza para denotar las predicciones del modelo. Es una convención común en estadísticas y aprendizaje automático para diferenciar los valores predichos (yhat) de los valores reales o verdaderos (y_test).

En resumen, lo que hace exactamente es:

El modelo clf, ya capacitado, toma las características (X_test) de cada una de las muestras del conjunto de prueba y, basándose en lo que aprendió durante el entrenamiento, estima y devuelve la etiqueta de clase (o el valor) que cree que corresponde a esas características. Todas estas estimaciones se guardan en la variable yhat.

Posteriormente, yhat se compara con y_test (los valores reales) para evaluar el rendimiento del modelo, como haces con la matriz de confusión.
"""





from sklearn.metrics import confusion_matrix
# Además, puedes usar diferentes métricas para evaluar la precisión de tu modelo.
# Por ejemplo, utilizando una matriz de confusión para mostrar los resultados.
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, yhat, labels=[1,0]))
"""
y_test (Conjunto de Objetivo de Prueba) 
Es la variable objetivo (y) correspondiente a las características de X_test. 
Son las "respuestas correctas" para X_test. 
Una vez que el modelo hace sus predicciones (yhat) sobre X_test, 
comparas esas predicciones con y_test para calcular métricas de rendimiento
 (como la precisión, la matriz de confusión, etc.) y ver qué tan bien generaliza tu modelo.
 
yhat  son las predicciones sobre el conjunto NUEVO de prueba y_test
"""

"""
Matriz de Confusión:
[[ 83  37]                  VerdaderoPositivo   FalsoNegativo-

 [ 24 151]]                 FalsoPositivo       VerdaderoNegativo 
 Dado que utilizaste labels=[1,0] al imprimirla, la interpretación de las filas y columnas es la siguiente:

Las filas representan los valores REALES de la clase.
Las columnas representan los valores PREDICHOS por el modelo.

El orden de las labels=[1,0] significa que la primera fila/columna corresponde a la clase 1 (Sobrevivió) y la segunda fila/columna a la clase 0 (No sobrevivió).
Desglosemos cada número:

83 (esquina superior izquierda): Verdaderos Positivos (VP / True Positives - TP)
Significado: El modelo predijo correctamente que 83 pasajeros sobrevivieron (1), 
y en realidad sí sobrevivieron (1).

Son los aciertos para la clase positiva.
37 (esquina superior derecha): Falsos Negativos (FN / False Negatives)
Significado: El modelo predijo que 37 pasajeros no sobrevivieron (0), pero en realidad sí sobrevivieron (1).

Son los errores donde el modelo "falló en detectar" un caso positivo. A menudo se les llama "falsas alarmas negativas" o "errores de Tipo II".
24 (esquina inferior izquierda): Falsos Positivos (FP / False Positives)
Significado: El modelo predijo que 24 pasajeros sobrevivieron (1), pero en realidad no sobrevivieron (0).

Son los errores donde el modelo "detectó" algo que no estaba presente. A menudo se les llama "falsas alarmas positivas" o "errores de Tipo I".
151 (esquina inferior derecha): Verdaderos Negativos (VN / True Negatives - TN)
Significado: El modelo predijo correctamente que 151 pasajeros no sobrevivieron (0), y en realidad no sobrevivieron (0).

Son los aciertos para la clase negativa.
En resumen, la Matriz de Confusión te dice:
Aciertos: Los números en la diagonal principal (83 y 151) son las predicciones correctas.
Errores: Los números fuera de la diagonal (37 y 24) son las predicciones incorrectas.
Te permite ver no solo cuántas veces el modelo acertó o falló en general, sino también cómo falló: ¿confundió a los que sobrevivieron con los que no, o viceversa? Esto es crucial para entender las fortalezas y debilidades de tu modelo y calcular métricas más avanzadas como la Precisión, Recall y F1-Score.

"""









import pickle
# Y finalmente, guardas tu modelo.
s = pickle.dumps(clf) # solo contiene la representación binaria del modelo

print("\nModelo guardado en formato binario (variable 's').")
print(s[:1000]) # Imprimimos solo los primeros 200 bytes, ya que es muy largo

"""
(pickle.dumps(clf)) solo contiene la representación binaria del modelo, que no es directamente legible 
para los humanos.

El propósito de pickle.dumps() es serializar el objeto Python (clf) en una secuencia de bytes 
para que pueda ser almacenado (por ejemplo, en un archivo) 
y luego deserializado (pickle.loads() o pickle.load()) para recrear el objeto original en memoria.
"""


#Ver los parámetros con los que se inicializó el modelo:
#Puedes usar get_params() en la instancia clf para ver los parámetros que le pasaste o los predeterminados.
# Después de que clf ha sido definido (clf = svm.SVC(gamma=0.001, C=100.))
print("\nParámetros del modelo (get_params()):")
print(clf.get_params())


#Inspeccionar ATRIBUTOS DEL MODELO ENTRENADO:
#Una vez que el modelo ha sido entrenado (clf.fit(...)),
# adquiere atributos que contienen "la información que aprendió."
# Para un SVC, algunos "ATRIBUTOS IMPORTANTES son:"
#clf.support_vectors_: Los vectores de soporte que definen el margen de separación.
#clf.n_support_: El número de vectores de soporte por clase.
#clf.intercept_: El término de intercepción (bías) de la función de decisión.
#clf.dual_coef_: Coeficientes de los vectores de soporte en la función de decisión.
# Después de que clf.fit(X_train, y_train) ha sido ejecutado
print("\nVectores de soporte (primeros 5):\n", clf.support_vectors_[:5])
print("\nNúmero de vectores de soporte por clase:\n", clf.n_support_)
print("\nIntercepción:\n", clf.intercept_)



#"Cargar" el modelo de nuevo desde su forma binaria:
#La forma más común de "ver" y reutilizar un modelo guardado es cargarlo de nuevo en memoria.
# Al hacerlo, obtienes el objeto clf original,
# listo para hacer nuevas predicciones sin tener que reentrenarlo.
# Suponiendo que 's' ya contiene el modelo guardado con pickle.dumps(clf)
modelo_cargado = pickle.loads(s)
print("\nTipo del modelo cargado:", type(modelo_cargado))
print("Parámetros del modelo cargado:", modelo_cargado.get_params())
# Ahora puedes usar modelo_cargado para hacer nuevas predicciones
# nuevas_predicciones = modelo_cargado.predict(nuevos_datos_X)



"""
Visualizar la superficie de decisión (para entender su comportamiento):
Esta es una forma más gráfica de "ver" cómo el modelo clasifica los datos.
 Sin embargo, esto solo es práctico para datasets con 2 o 3 características,
  ya que se complica visualizar más dimensiones. Implica graficar los puntos de tus 
  datos y la línea/superficie que el SVM ha aprendido para separarlos.
"""



# RENDIMIENTO
"""
Para calcular el rendimiento de tu modelo de clasificación,
 utilizamos las predicciones que ha hecho (yhat) 
 y las comparamos con los valores reales (y_test). 
 Scikit-learn tiene un módulo excelente (sklearn.metrics) para esto.



Antes de las métricas individuales, recordemos la Matriz de Confusión,
 que ya la has impreso. Es la base de muchas de estas métricas:

Verdaderos Positivos (VP / TP): El modelo predijo correctamente la clase positiva.
Verdaderos Negativos (VN / TN): El modelo predijo correctamente la clase negativa.
Falsos Positivos (FP): El modelo predijo la clase positiva, pero en realidad era negativa (error de Tipo I).
Falsos Negativos (FN): El modelo predijo la clase negativa, pero en realidad era positiva (error de Tipo II).

Métricas de Rendimiento Comunes:

Accuracy (Precisión de Exactitud)
Qué mide: La proporción de predicciones correctas sobre el total de predicciones. Es la métrica más intuitiva.

Fórmula: (VP+VN)/(VP+VN+FP+FN)
Cuándo usarla: Es buena para datasets balanceados (cuando las clases tienen un número similar de muestras). Si las clases están muy desbalanceadas, puede ser engañosa.

Cómo calcularla en Python:
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, yhat)
print(f"Accuracy: {accuracy:.4f}")

Precision (Precisión en Positivos)
Qué mide: De todas las instancias que el modelo predijo como positivas, ¿cuántas fueron realmente positivas? Minimiza los Falsos Positivos.
Fórmula: VP/(VP+FP)
Cuándo usarla: Importante cuando el costo de un Falso Positivo es alto (ej., diagnosticar una enfermedad que no existe, lo que lleva a tratamientos innecesarios).

Cómo calcularla en Python:
from sklearn.metrics import precision_score
precision = precision_score(y_test, yhat)
print(f"Precision: {precision:.4f}")

Recall (Sensibilidad / Exhaustividad / Tasa de Verdaderos Positivos)
Qué mide: De todas las instancias que realmente eran positivas, ¿cuántas identificó correctamente el modelo? Minimiza los Falsos Negativos.
Fórmula: VP/(VP+FN)
Cuándo usarla: Importante cuando el costo de un Falso Negativo es alto (ej., no detectar una enfermedad grave que sí existe).

Cómo calcularla en Python:
from sklearn.metrics import recall_score
recall = recall_score(y_test, yhat)
print(f"Recall: {recall:.4f}")

F1-Score (Puntuación F1)
Qué mide: Es la media armónica de la Precisión y el Recall. Proporciona un equilibrio entre ambas métricas y es especialmente útil cuando las clases están desbalanceadas o cuando te interesa un balance entre Falsos Positivos y Falsos Negativos.
Fórmula: $2 \* (Precision \* Recall) / (Precision + Recall)$

Cómo calcularla en Python:
from sklearn.metrics import f1_score
f1 = f1_score(y_test, yhat)
print(f"F1-Score: {f1:.4f}")

Reporte de Clasificación (Classification Report)
Qué mide: Es un resumen conveniente que muestra la Precision, Recall y F1-Score para cada clase, junto con el "support" (número de instancias reales de cada clase en y_test).

Cómo calcularlo en Python:
from sklearn.metrics import classification_report
print("\nReporte de Clasificación:")
print(classification_report(y_test, yhat))
"""





"""
 el modelo utilizado es de clasificación, específicamente un Support Vector Classifier (SVC). 
 Por lo tanto, las métricas de error para modelos de regresión, como MAE, MSE o RMSE, no son 
 aplicables. Estas métricas están diseñadas para evaluar la precisión en la predicción de 
 valores continuos.

Para evaluar el rendimiento de tu modelo de clasificación, las métricas adecuadas son las que
 se basan en la matriz de confusión. La matriz de confusión te permite entender cómo y dónde 
 tu modelo está acertando y fallando. Ya has incluido la matriz de confusión en tu código,
  y a partir de ella puedes calcular las siguientes métricas clave:

Precisión de Exactitud (Accuracy): Mide la proporción de predicciones correctas sobre el total de
 predicciones.

###Precisión (Precision): Indica, de todas las instancias que el modelo predijo como positivas, cuántas fueron realmente positivas. Es útil cuando el costo de un falso positivo es alto.
###Exhaustividad (Recall): Mide, de todas las instancias que realmente eran positivas, cuántas fueron identificadas correctamente por el modelo. Es crucial cuando el costo de un falso negativo es alto.
###Puntuación F1 (F1-Score): Es la media armónica de la precisión y la exhaustividad, proporcionando un equilibrio entre ambas métricas.
###A continuación, se muestra cómo puedes añadir el cálculo de estas métricas de clasificación en tu código, utilizando la matriz de confusión y el reporte de clasificación para un análisis más completo. Este bloque de código debe ser añadido después de la línea yhat = clf.predict(X_test).
"""

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report

print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, yhat, labels=[1,0])) # Manteniendo los labels del ejemplo


# Calcular y mostrar las métricas de clasificación
accuracy = accuracy_score(y_test, yhat)
precision = precision_score(y_test, yhat, zero_division=0) # zero_division=0 evita errores si no hay positivos predichos
recall = recall_score(y_test, yhat, zero_division=0)
f1 = f1_score(y_test, yhat, zero_division=0)

print(f"\nAccuracy (Exactitud): {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall (Sensibilidad): {recall:.4f}")
print(f"F1-Score: {f1:.4f}")


# El reporte de clasificación es muy útil para obtener todas las métricas por clase
print("\nReporte de Clasificación Completo:")
print(classification_report(y_test, yhat, zero_division=0))

"""
Nota sobre los errores de regresión: Las métricas como MAE, MSE, RMSE, RAE, y RSE se basan en la 
diferencia entre el valor real (y_j) y el valor predicho (ŷ_j). Dado que en clasificación se 
predice una etiqueta (como 0 o 1) y no un valor numérico continuo, estas fórmulas no tienen 
sentido para este tipo de modelo.
"""

