import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression # Cambiamos a un modelo de regresión
from sklearn.metrics import mean_squared_error, r2_score # Métricas para regresión
import pickle

# --- PASO 1: CARGAR LOS DATOS ---
# Usaremos un dataset de precios de casas de Boston, que es común para ejemplos de regresión.
# Nota: Este dataset ya no se incluye directamente en scikit-learn debido a problemas éticos,
# pero se puede cargar desde otras fuentes o simular. Para este ejemplo, usaremos uno público.
# Si tienes un CSV de emisiones de CO2, simplemente reemplaza esta URL y ajusta las columnas.

# Ejemplo con un dataset de precios de casas (sustituir si tienes el CSV de CO2)
# URL de un dataset de precios de casas (Boston House Prices)
# Fuente alternativa para el dataset de Boston House Prices (simulada o descargada)
# Puedes reemplazar esto con la URL de un CSV real de emisiones si lo tienes.
# Por simplicidad, si no tienes una URL directa, podrías usar un dataset de sklearn.datasets
# O descargar uno y cargarlo localmente.
# Para este ejemplo, vamos a simular uno o usar uno disponible
try:
    from sklearn.datasets import fetch_california_housing
    housing_data = fetch_california_housing(as_frame=True)
    df = housing_data.frame
    # 'MedHouseVal' es el objetivo (precio medio de la vivienda en USD 100,000s)
    # Las características son otras columnas
    features_regresion = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    target_regresion = 'MedHouseVal'
except ImportError:
    print("No se pudo cargar California Housing. Usando un dataset de prueba simple.")
    # Crea un DataFrame de prueba si no se puede cargar el de California Housing
    #DATOS HISTORICOS
    data = {
        'ENGINESIZE': [2.0, 2.4, 1.5, 3.5, 3.5, 3.5, 3.5, 3.7, 3.7, 2.4],
        'CYLINDERS': [4, 4, 4, 6, 6, 6, 6, 6, 6, 4],
        'FUELCONSUMPTION_COMB': [8.5, 9.6, 5.9, 11.1, 10.6, 10.0, 10.1, 11.1, 11.6, 9.2],
        'CO2EMISSIONS': [196, 221, 136, 255, 244, 230, 232, 255, 267, np.nan] # np.nan para el valor a predecir
    }

    """
    np.nan (que significa "Not a Number" o "No es un Número") es un valor muy común y perfectamente válido para representar datos faltantes o ausentes en NumPy y Pandas.

¿Por qué se usa np.nan?
Representación Estándar: Es la forma estándar y reconocida en el ecosistema de Python
 para ciencia de datos (NumPy, Pandas) para indicar que un valor numérico está ausente 
 o no es aplicable.

Facilita el Manejo de Datos Faltantes: 
Pandas tiene funciones muy potentes (.isnull(), .notnull(), .fillna(), .dropna()) 
que están diseñadas específicamente para detectar y manipular np.nan
 (y otros tipos de valores nulos).

Diferenciación: Es diferente de None de Python. Aunque None también puede representar 
la ausencia de un valor, np.nan es específico para arreglos numéricos y DataFrames, 
y permite operaciones matemáticas que None no permite 
(aunque el resultado de una operación con nan generalmente es nan).

Flota de Números: np.nan es un tipo de número de punto flotante (float).
 Esto significa que si tienes una columna de enteros y le asignas np.nan, 
 Pandas convertirá automáticamente la columna a tipo float para poder acomodar np.nan.
    """

    df = pd.DataFrame(data)

    print(df)

    features_regresion = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']
    target_regresion = 'CO2EMISSIONS'

print("Primeras 5 filas del DataFrame:")
print(df.head())
print("\nInformación del DataFrame:")
df.info()

# --- PASO 2: PREPARAR LOS DATOS (X e y) ---

# Manejo de valores nulos:
# Para regresión, el objetivo es continuo y no debe tener nulos para el entrenamiento.
# Si hay NaNs en el objetivo 'y', esas filas deben ser eliminadas o el NaN rellenado de alguna manera.
# Aquí, si 'CO2EMISSIONS' tiene un NaN (como en tu ejemplo de la imagen para la fila 9),
# lo trataremos como la fila que queremos predecir, no para el entrenamiento.
# Identificamos la fila con el NaN para predecirla después del entrenamiento.
# Si el NaN estuviera en una característica, lo rellenaríamos con la media/mediana.

# Guardamos la fila que queremos predecir (si existe un NaN en el objetivo)
# y la eliminamos del set de entrenamiento/prueba.
df_predict = df[df[target_regresion].isnull()]
df_train_test = df.dropna(subset=[target_regresion]) # Eliminar filas con NaN en el objetivo para entrenamiento

# Seleccionar las características (X) y la variable objetivo (y)
X = df_train_test[features_regresion].values
y = df_train_test[target_regresion].values

print("\nForma de X (Características):", X.shape)
print("Forma de y (Objetivo):", y.shape)
print("\nPrimeras 5 filas de X (para entrenamiento):\n", X[:5])
print("\nPrimeros 5 valores de y (para entrenamiento):\n", y[:5])

# --- PASO 3: PREPROCESAMIENTO DE DATOS (Escalado/Estandarización) ---
# En regresión, como en clasificación, escalar los datos es a menudo beneficioso,
# especialmente para algoritmos sensibles a la escala (como los que usan regularización, o SVR).
# LinearRegression no es tan sensible, pero es una buena práctica general.

# Inicializa el escalador estándar.
# StandardScaler transforma tus características para que tengan una media de 0 y una desviación estándar de 1.
scaler = preprocessing.StandardScaler()

# Ajusta el escalador a los datos de entrenamiento (calcula media y desviación estándar)
# y luego transforma los datos X.
X_scaled = scaler.fit_transform(X)

print("\nPrimeras 5 filas de X después de la estandarización:\n", X_scaled[:5])


# --- PASO 4: DIVIDIR LOS DATOS EN CONJUNTOS DE ENTRENAMIENTO Y PRUEBA ---
# Dividimos el conjunto de datos estandarizado en partes para entrenar y evaluar el modelo.
# X_train, y_train: Se usan para enseñar al modelo.
# X_test, y_test: Se usan para probar qué tan bien el modelo predice datos que no ha visto.
# test_size=0.2: El 20% de los datos se usará para prueba, el 80% para entrenamiento.
# random_state=42: Asegura que la división sea la misma cada vez que ejecutas el código.
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("\nForma de X_train (Entrenamiento):", X_train.shape)
print("Forma de y_train (Entrenamiento):", y_train.shape)
print("Forma de X_test (Prueba):", X_test.shape)
print("Forma de y_test (Prueba):", y_test.shape)


# --- PASO 5: CONFIGURAR Y ENTRENAR EL MODELO DE REGRESIÓN ---
# Para problemas de regresión, un modelo común es la Regresión Lineal.

# Inicializa el modelo de Regresión Lineal.
# Este modelo busca la mejor línea (o hiperplano) que se ajusta a los datos.
model = LinearRegression()

# Entrena el modelo usando los datos de entrenamiento.
# 'fit' hace que el modelo aprenda la relación entre X_train e y_train.
model.fit(X_train, y_train)

print("\nModelo de Regresión Lineal entrenado.")
# Puedes ver los coeficientes (pendientes) y la intercepción de la línea aprendida
print("Coeficientes (pesos) del modelo:", model.coef_)
print("Intercepción (bias) del modelo:", model.intercept_)


# --- PASO 6: HACER PREDICCIONES ---
# Usamos el modelo entrenado para predecir los valores de 'y' para el conjunto de prueba (datos no vistos).
y_pred = model.predict(X_test)

print("\nPrimeras 10 predicciones del modelo (y_pred):")
print(y_pred[:10])
print("\nPrimeros 10 valores reales de y_test:")
print(y_test[:10])


# --- PASO 7: EVALUAR EL RENDIMIENTO DEL MODELO ---
# Para regresión, las métricas comunes incluyen:
# - Error Cuadrático Medio (Mean Squared Error - MSE): Promedio de los cuadrados de los errores.
# - R-cuadrado (R-squared): Proporción de la varianza en la variable dependiente que es predecible a partir de las variables independientes. Un valor más cercano a 1 es mejor.

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nError Cuadrático Medio (MSE): {mse:.2f}")
print(f"Coeficiente de Determinación (R-cuadrado): {r2:.2f}")

# --- PASO 8: PREDECIR UN NUEVO VALOR (como la fila 9 de tu imagen) ---
if not df_predict.empty:
    # Asegúrate de que los nuevos datos tengan el mismo formato y escala que los datos de entrenamiento.
    X_new_predict_raw = df_predict[features_regresion].values

    # Es crucial escalar los datos de la misma manera que se escalaron los datos de entrenamiento.
    # Usamos el mismo 'scaler' que se ajustó en X_train.
    X_new_predict_scaled = scaler.transform(X_new_predict_raw)

    # Realizar la predicción
    new_prediction = model.predict(X_new_predict_scaled)

    print(f"\nValor a predecir (fila original de CO2EMISSIONS con '?', o tu fila de ejemplo):")
    print(df_predict)
    print(f"Predicción de CO2EMISSIONS para la nueva fila: {new_prediction[0]:.2f}")
else:
    print("\nNo hay filas con valores nulos en la columna objetivo para predecir específicamente.")


# --- PASO 9: GUARDAR Y CARGAR EL MODELO (Opcional) ---
# Guardar el modelo entrenado en un archivo.
# Esto permite reutilizar el modelo sin tener que reentrenarlo cada vez.
filename = 'modelo_regresion.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)
print(f"\nModelo guardado como '{filename}'.")

# Cargar el modelo desde el archivo.
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)
print(f"Modelo cargado desde '{filename}'.")

# Puedes usar el modelo cargado para hacer nuevas predicciones
# Por ejemplo, volver a predecir con X_test para verificar que funciona igual
loaded_y_pred = loaded_model.predict(X_test)
loaded_mse = mean_squared_error(y_test, loaded_y_pred)
print(f"MSE con modelo cargado: {loaded_mse:.2f} (debería ser igual al original)")


"""
La imagen muestra la predicción de CO2EMISSIONS (un valor continuo) basándose en características como ENGINESIZE, CYLINDERS, y FUELCONSUMPTION_COMB. Esto es un claro ejemplo de regresión.

Usaremos un dataset de ejemplo similar que es comúnmente utilizado para regresión: los precios de las casas.
"""

"""
"""
"""
Explicación del Código en Español:
Este código realiza un flujo completo de un problema de regresión, desde la carga de datos hasta la evaluación del modelo y la predicción de un nuevo valor.

Importaciones Necesarias:

numpy y pandas: Para el manejo y manipulación de datos.

sklearn.preprocessing: Para estandarizar los datos.

sklearn.model_selection.train_test_split: Para dividir los datos.

sklearn.linear_model.LinearRegression: El algoritmo de regresión lineal.

sklearn.metrics.mean_squared_error, r2_score: Métricas para evaluar modelos de regresión.

pickle: Para guardar y cargar el modelo entrenado.

Paso 1: Cargar los Datos (df = ...)

Aquí se carga el conjunto de datos. En este ejemplo, se intenta cargar un dataset de precios de viviendas de California de sklearn.datasets.

IMPORTANTE: Si tuvieras un archivo CSV con los datos de emisiones de CO2 como en la imagen, reemplazarías esta sección por df = pd.read_csv('tu_archivo_de_emisiones.csv').

Se identifica claramente qué columnas serán las características (X) y cuál será la variable objetivo (y). En la imagen, ENGINESIZE, CYLINDERS, FUELCONSUMPTION_COMB son X, y CO2EMISSIONS es y.

Paso 2: Preparar los Datos (X e y)

Manejo de valores nulos: Se identifica si hay filas en la variable objetivo (CO2EMISSIONS) que tienen valores nulos (como el ? en la imagen para la fila 9).

Las filas con nulos en el objetivo se separan en df_predict para ser predichas después de que el modelo esté entrenado.

Las filas completas (sin nulos en el objetivo) se usan para el entrenamiento y prueba (df_train_test). Esto es crucial: no puedes entrenar un modelo si su "respuesta correcta" (el valor y) es desconocida.

Las columnas seleccionadas como características (features_regresion) se extraen y se convierten a un array de NumPy (.values) para X.

La columna objetivo (target_regresion) se extrae y se convierte a un array de NumPy para y.

Se imprimen las "formas" (.shape) de X e y para verificar las dimensiones (número de filas y columnas).

Paso 3: Preprocesamiento de Datos (Escalado/Estandarización)

preprocessing.StandardScaler(): Crea un objeto "escalador". Este escalador aprenderá la media y la desviación estándar de cada característica en tus datos.

scaler.fit_transform(X): Este método realiza dos pasos:

fit(): Calcula la media y la desviación estándar para cada característica basándose en X.

transform(): Usa esas medias y desviaciones estándar para estandarizar (escalar) X. Cada valor se transforma a (valor−media)/desviacion_estandar.

¿Por qué estandarizar? Pone todas las características en una escala similar (media 0, desviación estándar 1). Esto es vital para muchos algoritmos de Machine Learning, ya que evita que las características con valores más grandes dominen sobre las que tienen valores más pequeños, asegurando que todas contribuyan de manera equitativa al aprendizaje del modelo.

Paso 4: Dividir los Datos en Conjuntos de Entrenamiento y Prueba

train_test_split(X_scaled, y, test_size=0.2, random_state=42): Esta función divide tus datos en cuatro partes:

X_train, y_train: Los datos que el modelo usará para aprender.

X_test, y_test: Los datos que el modelo nunca verá durante el entrenamiento y que se usarán para evaluar su rendimiento.

test_size=0.2: Indica que el 20% de los datos se usarán para el conjunto de prueba, y el 80% para el entrenamiento.

random_state=42: Asegura que la división sea reproducible; si ejecutas el código varias veces, siempre obtendrás la misma división.

Paso 5: Configurar y Entrenar el Modelo de Regresión

model = LinearRegression(): Se inicializa el modelo de Regresión Lineal. Este es un algoritmo que encuentra la relación lineal que mejor se ajusta a los datos para predecir la variable objetivo continua.

model.fit(X_train, y_train): Este es el paso de entrenamiento. El modelo "aprende" de los datos de entrenamiento (X_train e y_train) ajustando sus parámetros internos (coeficientes y la intercepción) para minimizar el error entre sus predicciones y los valores reales.

Paso 6: Hacer Predicciones

y_pred = model.predict(X_test): Una vez que el modelo está entrenado, se le pide que haga predicciones (y_pred) sobre el conjunto de prueba (X_test), que contiene datos que nunca ha visto.

Paso 7: Evaluar el Rendimiento del Modelo

Para la regresión, las métricas más comunes son:

Error Cuadrático Medio (Mean Squared Error - MSE): Mide el promedio de los cuadrados de los errores. Un MSE más bajo indica un mejor ajuste del modelo.

R-cuadrado (R-squared): Indica qué proporción de la varianza en la variable dependiente (el objetivo) es predecible a partir de las variables independientes. Un valor más cercano a 1 (o 100%) indica que el modelo explica una gran parte de la variabilidad del objetivo, lo que generalmente es bueno.

mean_squared_error(y_test, y_pred) y r2_score(y_test, y_pred): Calculan estas métricas comparando las predicciones del modelo (y_pred) con los valores reales (y_test).

Paso 8: Predecir un Nuevo Valor (como la fila 9 de la imagen)

Esta sección demuestra cómo usar el modelo entrenado para predecir el valor de CO2EMISSIONS para una fila específica donde el valor es desconocido (np.nan).

Crucial: Antes de hacer la predicción, los nuevos datos (X_new_predict_raw) DEBEN ser escalados usando el MISMO scaler que se usó para los datos de entrenamiento. Esto asegura que los nuevos datos estén en la misma escala que el modelo aprendió.

Paso 9: Guardar y Cargar el Modelo (Opcional)

pickle.dump(model, file): Permite "serializar" el modelo entrenado, es decir, convertir el objeto Python (model) en una secuencia de bytes que se puede guardar en un archivo (.pkl). Esto es útil para no tener que reentrenar el modelo cada vez que lo quieras usar.

pickle.load(file): Lee el archivo .pkl y "deserializa" los bytes de nuevo en un objeto Python (el modelo).

Después de cargarlo, puedes usar el loaded_model para hacer nuevas predicciones de la misma manera que el modelo original.
"""