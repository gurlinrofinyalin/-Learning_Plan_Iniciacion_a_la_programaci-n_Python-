import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold # Para la validación cruzada K-Fold
from sklearn.metrics import mean_squared_error, r2_score
import pickle
import matplotlib.pyplot as plt # Para visualización

# --- PASO 1: CARGAR LOS DATOS ESPECÍFICOS DE LAS IMÁGENES ---
# Creamos el DataFrame 'df' directamente con los datos mostrados en 'image_0b6a5c.png'.
# La fila 9 tiene un valor NaN en CO2EMISSIONS, que trataremos como un valor a predecir.
data = {
    'ENGINESIZE': [2.0, 2.4, 1.5, 3.5, 3.5, 3.5, 3.5, 3.7, 3.7, 2.4],
    'CYLINDERS': [4, 4, 4, 6, 6, 6, 6, 6, 6, 4],
    'FUELCONSUMPTION_COMB': [8.5, 9.6, 5.9, 11.1, 10.6, 10.0, 10.1, 11.1, 11.6, 9.2],
    'CO2EMISSIONS': [196, 221, 136, 255, 244, 230, 232, 255, 267, np.nan] # np.nan para el valor a predecir (fila 9)
}
df = pd.DataFrame(data)

print("Primeras filas del DataFrame cargado (datos de la imagen):")
print(df)
print("\nInformación del DataFrame:")
df.info()

# Definimos las características (variables independientes) y el objetivo (variable dependiente).
# Según las imágenes, las características son 'ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB'.
# El objetivo es 'CO2EMISSIONS'.
features_regresion = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']
target_regresion = 'CO2EMISSIONS'

# --- PASO 2: PREPARAR LOS DATOS (X e y) ---

# Separamos la fila con el valor NaN en 'CO2EMISSIONS' (fila 9) si existe, para predecirla después.
# Esto asegura que nuestro conjunto de entrenamiento y prueba solo contenga datos completos.
df_to_predict_later = df[df[target_regresion].isnull()].copy() # .copy() para evitar SettingWithCopyWarning
df_train_eval = df.dropna(subset=[target_regresion]).copy() # Elimina filas con NaN en el objetivo para entrenamiento/evaluación



# Seleccionar las características (X) y la variable objetivo (y) para el entrenamiento y evaluación.
X = df_train_eval[features_regresion].values #
"""
Cuando usas .values en un DataFrame o en una Serie de Pandas, lo que hace es extraer los datos subyacentes y devolverlos como un array de NumPy.
df_train_eval[features_regresion] te da un DataFrame de Pandas que contiene solo las columnas especificadas en features_regresion 
(por ejemplo, 'ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB').
Al añadir .values al final (df_train_eval[features_regresion].values), estás indicando a Pandas que quieres los datos de ese DataFrame 
en formato de array de NumPy bidimensional.
"""
y = df_train_eval[target_regresion].values
"""
De manera similar, df_train_eval[target_regresion] te da una Serie de Pandas que contiene la columna 'CO2EMISSIONS'.
Al añadir .values (df_train_eval[target_regresion].values), obtienes los datos de esa Serie en formato de array de NumPy unidimensional.
"""
"""
En resumen, .values convierte un objeto de Pandas (DataFrame o Serie) en un array de NumPy.
Muchas librerías de Machine Learning en Python, como scikit-learn (que usas para LinearRegression), 
están optimizadas para trabajar con arrays de NumPy. 
Aunque scikit-learn puede a veces aceptar DataFrames de Pandas directamente, 
es una práctica común y a menudo más segura (y a veces necesaria) convertir los datos a arrays de NumPy explícitamente usando 
.values antes de pasarlos a los algoritmos de entrenamiento o predicción.
"""



print(f"\nDataFrame para entrenamiento y evaluación (excluyendo la fila con NaN):")
print(df_train_eval)
print("\nForma de X (Características para entrenamiento/evaluación):", X.shape)
print("Forma de y (Objetivo para entrenamiento/evaluación):", y.shape)




# --- PASO 3: PREPROCESAMIENTO DE DATOS (Escalado/Estandarización) ---
# Es una buena práctica estandarizar las características para que tengan una media de 0 y una desviación estándar de 1.
# Esto ayuda a que el modelo de regresión lineal funcione mejor, especialmente si las características
# tienen rangos de valores muy diferentes.
scaler = preprocessing.StandardScaler()# crea la herramienta para la standarizacionm objeto scaler
"""
####inicializa un objeto (una instancia) de la clase StandardScaler que proviene del módulo preprocessing de scikit-learn.
-preprocessing: Es un módulo dentro de scikit-learn que contiene diversas funciones y clases para transformar datos 
brutos en un formato que sea más adecuado para los algoritmos de Machine Learning. 
Incluye tareas como escalar, normalizar, codificar variables categóricas, etc.
-StandardScaler: Es una clase específica diseñada para realizar la estandarización de características. 
La estandarización es un proceso de escalado de características donde se transforma la distribución de cada característica
 para que tenga una media de 0 (cero) y una desviación estándar de 1 (uno).

Analogía: Imagina que tienes diferentes medidas: 
la altura de una persona en centímetros (ej. 175 cm), 
el peso en kilogramos (ej. 70 kg) 
y su edad en años (ej. 30 años). 
Estas medidas están en escalas muy diferentes. StandardScaler es como un "transformador" que preparas para que, 
cuando le des esos números, los convierta a una escala común y comparable, donde el "punto de referencia" 
sea el promedio (0) y la dispersión típica sea una unidad (1). 
En este punto, solo estás preparando el transformador, no lo has aplicado aún.
"""
X_scaled = scaler.fit_transform(X)
"""
####realiza dos operaciones consecutivas sobre tus datos de características (X) utilizando el objeto scaler que creaste. HERRAMIENTA
El método fit_transform() es una combinación conveniente de dos pasos separados: fit() y transform().
scaler.fit(X) (Paso de "ajuste"):
Propósito: Este paso es donde el StandardScaler "aprende" o "calcula" los parámetros necesarios para la estandarización.
 Para cada columna (característica) en tu conjunto de datos X, fit() calcula:
La media (μ) de los valores de esa columna.
La desviación estándar (σ) de los valores de esa columna.
Estos valores (media y desviación estándar) son cruciales porque serán los mismos que se usarán para transformar 
cualquier dato futuro (por ejemplo, tus datos de prueba o nuevos datos para predecir). 
Es vital que la transformación de los datos de prueba o nuevos datos se base en las estadísticas de los datos de 
entrenamiento para evitar la fuga de datos (data leakage).

scaler.transform(X) (Paso de "transformación"):
Propósito: Este paso aplica la estandarización real a los datos X utilizando la media y la desviación estándar 
que se calcularon en el paso fit().
Fórmula: Para cada valor individual x en una columna, se transforma de la siguiente manera:
x  transformado = x−μ / σ
Resultado: Esto convierte los valores de cada característica para que tengan una media de 0 y una desviación estándar de 1.
X_scaled: La variable X_scaled almacena el resultado de esta transformación, que es un nuevo array de NumPy con tus 
características ya estandarizadas.

Analogía: Continuando con la analogía del transformador:
fit(X): Es como si el transformador "estudiara" las alturas, pesos y edades de un grupo de personas (tus datos X) 
para entender cuál es la altura promedio, el peso promedio, etc., y cuán dispersos están. 
Él calcula esos promedios y dispersiones.
transform(X): Es cuando el transformador realmente aplica esa "receta" que aprendió 
(restar el promedio y dividir por la desviación estándar) a cada altura, peso y edad de esas mismas personas. 
El resultado son números que ahora son directamente comparables entre sí, independientemente de sus unidades originales.
"""

print("\nPrimeras 5 filas de X después de la estandarización:\n", X_scaled[:5])

# --- PASO 4: CONFIGURAR VALIDACIÓN CRUZADA K-FOLD ---
# En lugar de una única división train/test, usaremos K-Fold Cross-Validation.
# Esto divide el dataset en 'k' partes (folds). El modelo se entrena 'k' veces,
# usando k-1 folds para entrenamiento y el fold restante para prueba en cada iteración.
# Esto proporciona una evaluación más robusta del rendimiento del modelo.

n_splits = 4 # Como sugiere la imagen de K-Fold, usaremos 4 folds (80%/20% se aproxima aquí)
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)# kf: Es el objeto KFold
# 'shuffle=True' para aleatorizar la división
# random_state=42 SI no se especifica, cada vez que se ejecuta el codigo, se divide de forma diferente
# asi la secuencia de numeros aleatorios sera la mismam la división en los folds de entrenamiento y prueba, será exactamente la misma.
"""
#####El parámetro random_state=42 en KFold (y en muchas otras funciones de scikit-learn que involucran aleatoriedad, 
como train_test_split, RandomForestClassifier, etc.) sirve para asegurar la reproducibilidad de los resultados.
Aleatoriedad Controlada:
Cuando shuffle=True (mezclar), KFold (o train_test_split) reorganiza aleatoriamente tus datos antes de dividirlos 
en los diferentes folds (o en conjuntos de entrenamiento y prueba).
Si no especificas random_state, cada vez que ejecutes el código, la mezcla será diferente,  IMPORTANTE 
lo que significa que obtendrás diferentes divisiones de tus datos en entrenamiento y prueba.

Reproducibilidad:
Al establecer random_state a un valor entero fijo (como 42, que es un número arbitrario pero comúnmente usado en 
ejemplos de programación,
Esto significa que, cada vez que ejecutes el código con el mismo random_state, la secuencia de números aleatorios 
generada será idéntica. Por lo tanto, la mezcla de los datos y, consecuentemente, 
la división en los folds de entrenamiento y prueba, será exactamente la misma.

Ventajas de usar random_state:
Resultados Consistentes: Si tú o alguien más ejecuta tu código más tarde, obtendrán los mismos resultados de división 
y, por lo tanto, las mismas métricas de rendimiento del modelo (asumiendo que todo lo demás sea igual). 
Esto es vital para depurar, compartir código y verificar experimentos.

Comparación Justa de Modelos: Si estás comparando diferentes algoritmos de Machine Learning o diferentes configuraciones 
de hiperparámetros, es esencial que se entrenen y evalúen con las mismas divisiones de datos para que la comparación
 sea justa y las diferencias observadas se deban al modelo, y no a una división de datos diferente.

Depuración: Ayuda a identificar problemas. Si tu modelo se comporta de manera extraña, puedes asegurarte de que no es 
debido a una división de datos aleatoria diferente cada vez.

random_state=42 no tiene un significado mágico en sí mismo más allá de ser un número fijo. 
Su propósito es eliminar la variabilidad aleatoria en la división de los datos, 
garantizando que los experimentos sean reproducibles y comparables.
"""


print(f"\nConfiguración de Validación Cruzada K-Fold con {n_splits} splits (folds).")

# Listas para almacenar las métricas de cada fold
mse_scores = []
r2_scores = []
fold_num = 0
"""
mse_scores = []
Propósito: Esta es una lista vacía que se utilizará para almacenar el Error Cuadrático Medio (MSE) 
calculado en cada una de las iteraciones (folds) de la validación cruzada.
En K-Fold, el modelo se entrena y evalúa k veces (una vez por cada fold de prueba). 
Queremos registrar el MSE de cada una de esas evaluaciones para luego poder calcular un MSE promedio y su desviación estándar, 
lo que nos da una medida más robusta y menos dependiente de una única división de datos.

r2_scores = []
Propósito: Similar a mse_scores, esta es una lista vacía que se usará para almacenar la puntuación R-cuadrado (R2-score) 
calculada en cada una de las iteraciones (folds) de la validación cruzada.
Por la misma razón que el MSE. El R2-score es otra métrica clave para la regresión. 
Al promediar los R2-scores de todos los folds, obtenemos una estimación más fiable de qué tan bien el modelo generaliza 
y explica la varianza de los datos en promedio.

fold_num = 0
Propósito: Esta es una variable de contador que se utiliza para llevar la cuenta del número de fold actual en el que 
se encuentra el bucle de validación cruzada.
¿Por qué?: Se inicializa en 0 y se incrementa en cada iteración del bucle (fold_num += 1). 
Su función principal es informativa, permitiendo imprimir mensajes en la consola como "--- Fold 1/4 ---", 
"--- Fold 2/4 ---", etc., lo que ayuda a seguir el progreso y entender qué fold se está procesando en un momento dado. 
No afecta directamente los cálculos del modelo, pero mejora la legibilidad de la salida.
"""



#### EXPLICACION PREVIA
"""
 kf.split(X_scaled) y los índices train_index, test_index
La línea for train_index, test_index in kf.split(X_scaled): es el corazón de la validación cruzada K-Fold.
kf: Es el objeto KFold que inicializaste previamente (kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)). 
Este objeto sabe cómo dividir tus datos en n_splits (en tu caso, 4) partes, mezclándolos si shuffle=True.

kf.split(X_scaled): Este método no devuelve directamente los datos divididos. 
En cambio, es un "generador" que, en cada iteración del bucle for, produce un par de arrays de índices:
train_index: 
Un array de NumPy que contiene "los índices de las filas de tu dataset X_scaled (y y)" 
que deben usarse para entrenar el modelo en la iteración actual (o "fold").

test_index: 
Un array de NumPy que contiene "los índices de las filas de tu dataset X_scaled (y y)" 
que deben usarse para probar (evaluar) el modelo en la iteración actual.

Imagina que tienes 9 filas de datos (índices del 0 al 8). 
Con n_splits=4, kf.split() podría generar algo así en sus iteraciones:
1ª Iteración:
train_index podría ser [2, 3, 4, 5, 6, 7, 8] (7 índices)
test_index podría ser [0, 1] (2 índices
2ª Iteración:
train_index podría ser [0, 1, 4, 5, 6, 7, 8] (7 índices)
test_index podría ser [2, 3] (2 índices)

...y así sucesivamente, asegurándose de que cada fila se use exactamente una vez en el conjunto de prueba 
y k-1 veces en el conjunto de entrenamiento.

Explicación de X_train_fold, X_test_fold, y_train_fold, y_test_fold
Dentro del bucle for, estas variables son los subconjuntos de datos reales (no solo los índices) que se extraen para cada fold.

X_train_fold: Es el subconjunto de características (X) que se utilizará para "entrenar el modelo" en esta iteración específica del K-Fold.
X_test_fold: Es el subconjunto de características (X) que se utilizará para "evaluar el modelo" en esta iteración.
y_train_fold: Es el subconjunto de la variable objetivo (y) que corresponde a X_train_fold y se utiliza para "entrenar el modelo".
y_test_fold: Es el subconjunto de la variable objetivo (y) que corresponde a X_test_fold y se utiliza para "evaluar el rendimiento del modelo".


ALARACION  X_train_fold(son caracteristicas X  entradas) y  y_train_fold(son las respuestas  Y variables objetivo )
X_train_fold  y  y_train_fold son una linea de los datos completa  

Tienes razón en que X_train_fold y y_train_fold representan líneas (o en un contexto de tabla, filas enteras) 
de tu conjunto de datos original, pero ""se manejan por separado para el entrenamiento del modelo.""

IMPORTANTISIMO   
entrenar una nueva instancia del modelo
El algoritmo de regresión lineal ajusta sus coeficientes e intercepto para que sus predicciones (y_hat) 
siendo
X_train_fold   (el array 2d de numpy como entradas ) 
y_train_fold  (el array unidimensional salida o  respouesta correcta) 
El modelo aprende las relaciones entre las características y el objetivo basándose en estos datos,
ajusta sus coeficientes e intercepto, para lograr las predicciones

X_train_fold (Características / Variables Independientes):  (/ array 2D de NumPy  / fila punto de datos / columna caracteristica /)
Contiene todas las columnas de características (por ejemplo, 'ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB') 
para un conjunto específico de filas seleccionadas para el entrenamiento en un fold particular.
Para el modelo, esto se ve como una matriz (array 2D de NumPy) donde cada fila es un punto de datos 
y cada columna es una característica.
Cuando se entrena el modelo (model.fit(X_train_fold, y_train_fold)), 
X_train_fold es la entrada que el modelo "observa" para aprender patrones y relaciones.

y_train_fold (Variable Dependiente / Objetivo):  (array 1D de NumPy)
Contiene solo la columna del objetivo (por ejemplo, 'CO2EMISSIONS') para las mismas filas que están en X_train_fold.
Para el modelo, esto se ve como un vector (array 1D de NumPy).
y_train_fold es la "respuesta correcta" o el "resultado" que el modelo intenta predecir. 
El algoritmo de regresión lineal ajusta sus coeficientes e intercepto para que sus predicciones (y_hat) 
se parezcan lo más posible a estos valores y_train_fold.

¿Por qué se añaden por separado?
La razón fundamental es la naturaleza de los algoritmos de aprendizaje supervisado:
Entrada (X): Necesitan un conjunto de características para aprender. Estas son las "pistas" o "atributos" sobre los cuales el modelo basará sus decisiones o predicciones.
Salida/Objetivo (y): Necesitan saber cuál es la respuesta correcta o el valor a predecir para cada conjunto de características de entrada. Esto es lo que el modelo intenta replicar o estimar.

El modelo de regresión lineal, al igual que muchos otros algoritmos de Machine Learning, está diseñado para recibir estas dos partes por separado: las características (X) y los valores objetivo (y). El objetivo del fit() es encontrar la función matemática que mejor mapee X a y.




¿Para qué se van a utilizar?
X_train_fold y y_train_fold: Se pasan al método model.fit(X_train_fold, y_train_fold) para entrenar una nueva instancia del modelo de regresión lineal 
en cada fold. El modelo aprende las relaciones entre las características y el objetivo basándose en estos datos.


DESPUES DE HABERSE ENTRENADO EL MODELO
X_test_fold y y_test_fold: 
Después de que el modelo se ha entrenado en los datos de _train_fold, 
X_test_fold(datos que no ha visto el modelo de las caracteristicas sin las etiquetas o salida osease Y ) 
se usa para generar predicciones (y_pred_fold = model.predict(X_test_fold)). 
Luego, estas y_pred_fold(predicciones) se comparan con los valores reales y_test_fold (las etiquetas o salida ) 
para calcular las métricas de evaluación (MSE, R2-score) para ese fold.

Explicación de X_scaled[train_index], X_scaled[test_index] y y[train_index], y[test_index]
Esto es una técnica estándar de indexación de NumPy (y funciona de manera similar con Pandas, aunque X_scaled y y ya son arrays de NumPy en tu código).

X_scaled[train_index]:
X_scaled es tu array de NumPy que contiene todas las características estandarizadas.

train_index es un array de NumPy que contiene una lista de enteros (los índices de las filas que queremos seleccionar).

IMPORTANTE
Cuando pasas un array de índices a otro array, 
NumPy selecciona las filas (o elementos) que corresponden a esos índices.

Resultado: Crea un nuevo array de NumPy que contiene solo las filas de X_scaled cuyos índices están listados en train_index. 
Este es tu X_train_fold.

X_scaled[test_index]:
Exactamente igual, pero selecciona las filas de X_scaled correspondientes a los índices en test_index, formando tu X_test_fold.


y[train_index] y y[test_index]:
Funcionan de la misma manera para el array y (tu variable objetivo). 
Seleccionan los valores de y que corresponden a los train_index y test_index respectivamente, 
creando y_train_fold y y_test_fold.

En esencia, estos comandos de indexación permiten extraer los subconjuntos específicos de datos (tanto características como objetivo) para entrenamiento y prueba en cada iteración de la validación cruzada K-Fold, basándose en los índices que proporciona el generador kf.split().
"""




# --- PASO 5: ENTRENAR Y EVALUAR EL MODELO CON K-FOLD ---
# Iteramos a través de cada fold generado por KFold.
for train_index, test_index in kf.split(X_scaled):
    fold_num += 1
    print(f"\n--- Fold {fold_num}/{n_splits} ---") # fold_num es la iteracion    "--- Fold 1/4 ---",  "--- Fold 2/4 ---"m
                                                   # n_splits} numero de iteraciones totales

    # Divide los datos en conjuntos de entrenamiento y prueba para el fold actual
    X_train_fold, X_test_fold = X_scaled[train_index], X_scaled[test_index]
    #X_scaled[train_index] datos de caracteristicas de entrenamiento como entrada
    #X_scaled[test_index]  datos de objetivo de entrenamiento como salida
    y_train_fold, y_test_fold = y[train_index], y[test_index]
    #y[train_index]  datos de caracteristicas (el modelo no los vio al entrenar) se usan para las predicciones
    # y[test_index] datos del objetivo (el modelo no los vio al entrenar ) se usan para comprar con predicciones y sacar rendimiento

    # La imagen  tiene 9 filas de datos completos (índices 0 a 8).
    # Si tenemos 9 puntos de datos y test_size=0.25 (que es 25%),
    # 9 * 0.25 = 2.25. Esto significa que el test set tendrá 2 o 3 puntos de datos.
    # KFold con n_splits=4 en 9 puntos de datos:
    # 9 / 4 = 2.25. Algunos folds tendrán 2, otros 3 elementos en el test set.
    # Por ejemplo, para 9 elementos, los índices de test podrían ser:
    # Fold 1: [0, 1] (2 elementos)
    # Fold 2: [2, 3] (2 elementos)
    # Fold 3: [4, 5, 6] (3 elementos)
    # Fold 4: [7, 8] (2 elementos)

    # Nota: Los índices de la imagen (6,7,8,9) como "Test" son solo un ejemplo de división estática.
    # Con KFold, los índices de test cambiarán en cada iteración.

    # Imprimimos los índices de las filas de train y test para este fold para entender la división
    # Esto es solo para propósitos de visualización y comprensión, no es necesario para el funcionamiento del modelo.
    print(f"Índices de entrenamiento para este fold: {train_index}")
    print(f"Índices de prueba para este fold: {test_index}")

    # CONFIGURAR Y ENTRENAR EL MODELO DE REGRESIÓN PARA EL FOLD ACTUAL
    model = LinearRegression()
    model.fit(X_train_fold, y_train_fold)

    print("Coeficientes (pesos) del modelo para este fold:", model.coef_)
    print("Intercepción (bias) del modelo para este fold:", model.intercept_)

    # HACER PREDICCIONES PARA EL FOLD ACTUAL
    y_pred_fold = model.predict(X_test_fold)

    # EVALUAR EL RENDIMIENTO DEL MODELO PARA EL FOLD ACTUAL
    mse_fold = mean_squared_error(y_test_fold, y_pred_fold)
    r2_fold = r2_score(y_test_fold, y_pred_fold)

    mse_scores.append(mse_fold)
    r2_scores.append(r2_fold)

    print(f"  Error Cuadrático Medio (MSE) para el Fold {fold_num}: {mse_fold:.2f}")
    print(f"  Coeficiente de Determinación (R-cuadrado) para el Fold {fold_num}: {r2_fold:.2f}")

# --- PASO 6: RESUMEN DE LAS MÉTRICAS DE VALIDACIÓN CRUZADA ---
# Calculamos el promedio de las métricas obtenidas en todos los folds.
# Esto da una estimación más fiable del rendimiento general del modelo.
print("\n--- Resumen de la Validación Cruzada K-Fold ---")
print(f"MSE promedio en {n_splits} folds: {np.mean(mse_scores):.2f} +/- {np.std(mse_scores):.2f}")
print(f"R-cuadrado promedio en {n_splits} folds: {np.mean(r2_scores):.2f} +/- {np.std(r2_scores):.2f}")


# --- PASO 7: PREDICCIÓN DE UN NUEVO VALOR (La fila 9 de tu imagen) ---
# Usamos el último modelo entrenado (o podrías entrenar uno final con todo el dataset completo
# si no te importa el sobreajuste ligero, o usar el modelo del fold con mejor métrica).
# Para este ejemplo, usaremos el último modelo 'model' entrenado.

if not df_to_predict_later.empty:
    print(f"\n--- Predicción de la fila con CO2EMISSIONS desconocidas (de la imagen) ---")
    # Asegúrate de que los nuevos datos tengan el mismo formato de características.
    X_new_predict_raw = df_to_predict_later[features_regresion].values

    # Es CRUCIAL escalar los nuevos datos usando el MISMO 'scaler' que se ajustó con los datos de entrenamiento.
    X_new_predict_scaled = scaler.transform(X_new_predict_raw)

    # Realizar la predicción
    new_prediction = model.predict(X_new_predict_scaled)

    print(f"\nDatos de la fila a predecir:")
    print(df_to_predict_later)
    print(f"Predicción de CO2EMISSIONS para la fila 9: {new_prediction[0]:.2f} g/km")
else:
    print("\nNo hay filas con valores nulos en la columna objetivo para predecir específicamente (todas las filas estaban completas).")

# --- PASO 8: VISUALIZACIÓN DE UNA PREDICCIÓN (Opcional, si solo una característica es fácil de visualizar) ---
# Si tuviéramos un solo fold y una sola característica para visualizar la línea de regresión.
# En K-Fold, se entrena un modelo diferente en cada fold. Visualizar todos a la vez es complejo.
# Podemos visualizar la relación para el último fold entrenado, o para la relación general.

# Para una visualización simple, usemos todos los datos originales (sin NaN) y el último modelo entrenado.
# Se crea un gráfico de dispersión que muestra los datos reales y las predicciones del modelo lineal sobre la relación entre el tamaño del motor y las emisiones de CO2.
plt.figure(figsize=(10, 6)) # Define el tamaño de la figura.
plt.scatter(df_train_eval['ENGINESIZE'], df_train_eval['CO2EMISSIONS'], color='blue', label='Datos reales') # Dibuja los puntos de datos reales en azul.
plt.plot(df_train_eval['ENGINESIZE'], model.predict(scaler.transform(df_train_eval[features_regresion].values)), 'ro', alpha=0.6, label='Predicciones del último modelo') # Superpone las predicciones del modelo como puntos rojos.
plt.xlabel("Tamaño del Motor (ENGINESIZE)") # Etiqueta el eje X.
plt.ylabel("Emisiones de CO2") # Etiqueta el eje Y.
plt.title("Relación entre Tamaño del Motor y Emisiones de CO2 (y Predicciones)") # Establece el título del gráfico.
plt.legend() # Muestra la leyenda del gráfico.
plt.grid(True) # Activa la cuadrícula en el gráfico.
plt.show() # Muestra el gráfico en pantalla.

# --- PASO 9: GUARDAR Y CARGAR EL ÚLTIMO MODELO (Opcional) ---
# Guardar el modelo entrenado del último fold. Si quieres guardar el "mejor" modelo
# de K-Fold, tendrías que guardar el modelo con el mejor R2 o MSE.
filename = 'modelo_regresion_kfold.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)
print(f"\nÚltimo modelo entrenado (del último fold) guardado como '{filename}'.")

# Cargar el modelo desde el archivo.
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)
print(f"Modelo cargado desde '{filename}'.")

# Puedes usar el modelo cargado para hacer nuevas predicciones
# Por ejemplo, predecir con los datos escalados de la fila 9 nuevamente
if not df_to_predict_later.empty:
    loaded_new_prediction = loaded_model.predict(X_new_predict_scaled)
    print(f"Predicción con modelo cargado para la fila 9: {loaded_new_prediction[0]:.2f} g/km")