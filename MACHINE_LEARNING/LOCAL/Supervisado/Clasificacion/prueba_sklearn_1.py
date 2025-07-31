from sklearn import preprocessing
# Básicamente, los algoritmos de aprendizaje automático se benefician de la estandarización del conjunto de datos.
# Si hay algunos valores atípicos o campos de diferentes escalas en tu conjunto de datos, tienes que corregirlos.
# El paquete de preprocesamiento de Scikit Learn proporciona varias funciones de utilidad comunes y clases transformadoras para cambiar vectores de características en bruto a una forma adecuada de vector para modelar.
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split
# Tienes que dividir tu conjunto de datos en conjuntos de entrenamiento y prueba para entrenar tu modelo y luego probar la precisión del modelo por separado.
# Scikit Learn puede dividir arreglos o matrices en subconjuntos aleatorios de entrenamiento y prueba por ti en una línea de código.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

from sklearn import svm
# Luego puedes configurar tu algoritmo. Por ejemplo, puedes construir un clasificador utilizando un algoritmo de clasificación de vectores de soporte.
# Llamamos a nuestra instancia estimadora CLF y inicializamos sus parámetros.
clf = svm.SVC(gamma=0.001, C=100.)

# Ahora puedes entrenar tu modelo con el conjunto de entrenamiento.
# Al pasar nuestro conjunto de entrenamiento al método fit, el modelo CLF aprende a clasificar casos desconocidos.
clf.fit(X_train, y_train)

# Luego, podemos usar nuestro conjunto de prueba para hacer predicciones.
# Y el resultado nos dice cuál es la clase de cada valor desconocido.
clf.predict(X_test)

from sklearn.metrics import confusion_matrix
# Además, puedes usar diferentes métricas para evaluar la precisión de tu modelo.
# Por ejemplo, utilizando una matriz de confusión para mostrar los resultados.
print(confusion_matrix(y_test, yhat, labels=[1,0]))

import pickle
# Y finalmente, guardas tu modelo.
s = pickle.dumps(clf)