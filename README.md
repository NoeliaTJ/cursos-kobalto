# Análisis de ventas de juegos de PS4

Este proyecto analiza las ventas de juegos de PlayStation 4 por regiones, año y género, identificando patrones y grupos de títulos similares mediante técnicas de análisis de datos, clustering y reducción de dimensionalidad.[file:87]

## Datos

El dataset utilizado contiene información de ventas de juegos de PS4 con, entre otros, los siguientes campos:[file:87]

- `Game`: título del juego.  
- `Year`: año de lanzamiento (2013–2020).  
- `Genre`: género del juego (Action, Shooter, Sports, Action-Adventure, etc.).  
- `Publisher`: compañía distribuidora.  
- `North America`: ventas en Norteamérica (millones de unidades).  
- `Europe`: ventas en Europa (millones de unidades).  
- `Japan`: ventas en Japón (millones de unidades).  
- `Rest of World`: ventas en el resto del mundo (millones de unidades).  
- `Global`: ventas globales totales (millones de unidades).[file:87]

A partir de estas variables se calculan estadísticas descriptivas por año y región, incluyendo media, desviación estándar, mínimos, máximos y cuartiles.[file:87]

## Objetivos del análisis

- Explorar la distribución de ventas de juegos de PS4 por región y año.[file:87]  
- Comparar el rendimiento de distintos géneros y publishers a nivel global.[file:87]  
- Identificar grupos (clusters) de juegos con patrones de ventas similares.[file:87]  
- Reducir la dimensionalidad de los datos de ventas para visualizar mejor las relaciones entre juegos (PCA).[file:87]

## Metodología

1. **Exploración y estadísticas descriptivas**  
   - Cálculo de estadísticas por año y región (`Year`, `North America`, `Europe`, `Japan`, `Rest of World`, `Global`).[file:87]  
   - Resúmenes como media, desviación estándar y percentiles para entender la distribución de ventas.[file:87]

2. **Clustering de juegos**  
   - Uso de las ventas por región y/o ventas globales para agrupar juegos en clusters.[file:87]  
   - Asignación de una etiqueta `Cluster` a cada juego, que indica el grupo de comportamiento de ventas al que pertenece.[file:87]  
   - Ejemplos de juegos con altas ventas globales dentro de un mismo cluster:  
     - *Grand Theft Auto V*  
     - *Call of Duty: Black Ops 3*  
     - *Red Dead Redemption 2*  
     - *Call of Duty: WWII*  
     - *FIFA 18*.[file:87]

3. **Reducción de dimensionalidad (PCA)**  
   - Aplicación de Análisis de Componentes Principales (PCA) para combinar la información de ventas de varias regiones en pocas componentes.[file:87]  
   - Obtención de coordenadas `PC1` y `PC2` para cada juego, que permiten visualizar los juegos en un plano, coloreados por género o por cluster.[file:87]

## Requisitos

- Python 3.x  
- Bibliotecas principales:
  - `pandas`
  - `numpy`
  - `scikit-learn` (para clustering y PCA)
  - `matplotlib` y/o `seaborn` para visualización.[file:87]

Instalación recomendada:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Cómo ejecutar el notebook

1. Clona o descarga este repositorio.  
2. Asegúrate de que el dataset (por ejemplo `ps4_games.csv` o el nombre correspondiente) está en la misma carpeta que `Ps4.ipynb`.[file:87]  
3. Abre el notebook con Jupyter:

```bash
jupyter notebook Ps4.ipynb
```

4. Ejecuta las celdas en orden para:
   - cargar el dataset,  
   - generar estadísticas descriptivas,  
   - entrenar el modelo de clustering,  
   - aplicar PCA y visualizar los resultados.[file:87]

## Resultados esperados

El análisis permite:[file:87]

- Detectar qué géneros y títulos concentran las mayores ventas globales.  
- Ver diferencias de preferencias entre regiones (por ejemplo, ventas relativamente más altas en Europa que en Norteamérica o Japón para ciertos juegos).[file:87]  
- Visualizar agrupaciones de juegos con patrones de ventas similares en el plano de componentes principales `PC1`–`PC2`.[file:87]

Estos resultados facilitan entender el comportamiento del mercado de juegos de PS4 y apoyar decisiones sobre lanzamiento, marketing y catálogo según región y género.[file:87]
