
# Análisis de ventas de café

Este proyecto analiza un conjunto de datos de ventas de café a partir del archivo `Cafe.csv`.  
Incluye exploración de datos, visualización de distribuciones, comparación de precios según el tipo de café y el método de pago, clasificación del tipo de café con KNN, clustering con KMeans y reducción de dimensionalidad con PCA.

## Dataset

El archivo `Cafe.csv` contiene información sobre ventas de café con variables como:

- `date`: fecha de la venta.
- `datetime`: fecha y hora de la transacción.
- `money`: precio o importe de la venta.
- `coffee_name`: tipo de café vendido.
- `cash_type`: método de pago.

A partir de estas columnas se crean variables derivadas como:

- `hour`: hora de la venta.
- `weekday`: día de la semana.

## Objetivos del análisis

- Explorar la estructura y calidad del dataset.
- Analizar la distribución de precios.
- Comparar precios por tipo de café y método de pago.
- Estudiar la relación entre número de ventas diarias y precio medio.
- Clasificar el tipo de café usando variables como precio, hora, día de la semana y método de pago.
- Agrupar ventas similares mediante clustering.
- Visualizar los datos reduciendo la dimensionalidad con PCA.

## Análisis exploratorio

En el notebook se estudian aspectos básicos del dataset con:

- `info()`
- `describe()`
- `dtypes`
- `nunique()`
- `shape`

Esto permite conocer el tipo de variables, su distribución y el número de valores únicos.

## Visualizaciones

El proyecto incluye varias gráficas:

### Histograma de precios
Muestra la distribución de los precios del café.

### Scatter plot
Relaciona:

- número de ventas por día,
- precio medio diario.

Sirve para comprobar si existe relación entre el volumen de ventas y el precio promedio.

### Boxplot por tipo de café
Compara la distribución de precios entre los distintos tipos de café.

### Boxplot por método de pago
Permite ver si el precio cambia según el método de pago usado.

### Barras de ventas por tipo de café
Muestra cuántas ventas tiene cada tipo de café.

### Codo para KMeans
Se usa para elegir un número razonable de clusters según la inercia.

### PCA
Se representan los datos en dos componentes principales para observar si los tipos de café se agrupan visualmente.

## Clasificación con KNN

Se entrena un modelo de clasificación para predecir `coffee_name` usando:

- `money`
- `hour`
- `weekday`
- `cash_type`

Para ello, la variable `cash_type` se transforma con one-hot encoding.

### Modelo usado
- `KNeighborsClassifier`

### Evaluación
- `accuracy`
- `classification_report`

Este modelo permite comprobar hasta qué punto se puede predecir el tipo de café a partir de los datos de la compra.

## Clustering con KMeans

También se aplica clustering para agrupar ventas similares usando:

- `money`
- `hour`
- `weekday`
- `cash_type`

Antes de aplicar KMeans, las variables se estandarizan con `StandardScaler`.

### Proceso
1. Crear variables temporales.
2. Codificar `cash_type`.
3. Estandarizar los datos.
4. Calcular el codo para elegir `K`.
5. Entrenar el modelo KMeans.
6. Guardar la etiqueta de cluster en el dataset.

## PCA

Se aplica `PCA(n_components=2)` para reducir los datos a dos dimensiones y facilitar su visualización.

### Resultado
- `PC1`
- `PC2`

Después se dibuja un scatter plot coloreado por `coffee_name` para comprobar si los cafés forman grupos distinguibles en el espacio reducido.

## Requisitos

- Python 3.x
- pandas
- matplotlib
- numpy
- scikit-learn

Instalación recomendada:

```bash
pip install pandas matplotlib numpy scikit-learn
```

## Cómo ejecutar el notebook

1. Coloca `Cafe.csv` en la misma carpeta que el notebook.
2. Abre el archivo `.ipynb` con Jupyter Notebook o JupyterLab.
3. Ejecuta las celdas en orden.
4. Revisa las gráficas, los resultados del modelo y los clusters obtenidos.

## Resultados esperados

Este análisis permite:

- entender cómo se distribuyen los precios del café,
- comparar tipos de café y métodos de pago,
- detectar patrones temporales en las ventas,
- clasificar cafés a partir de sus características,
- agrupar transacciones similares,
- visualizar el conjunto de datos en dos dimensiones con PCA.

## Archivos del proyecto

- `Cafe.csv`: dataset principal.
- `README.md`: descripción del proyecto.
- `histograma.png`: histograma de precios.
- `scatter.png`: relación entre ventas diarias y precio medio.
- `boxplot.png`: distribución de precios por tipo de café.
- `boxplot_pago.png`: distribución de precios por método de pago.
- `barras.png`: ventas por tipo de café.
