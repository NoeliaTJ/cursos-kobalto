# Análisis del impacto de las redes sociales en estudiantes

Este proyecto analiza cómo el uso diario de redes sociales se relaciona con el rendimiento académico, las horas de sueño y la salud mental de estudiantes a partir del dataset `social.csv`.

## Datos

El archivo `social.csv` contiene, entre otros, los siguientes campos:

- `Student_ID`: identificador del estudiante.  
- `Age`: edad (18–24 años).  
- `Gender`: género.  
- `Academic_Level`: nivel académico (High School, Undergraduate, Graduate, etc.).  
- `Country`: país o región.  
- `Avg_Daily_Usage_Hours`: horas de uso diario medio de redes sociales.  
- `Most_Used_Platform`: plataforma más utilizada (Snapchat, etc.).  
- `Affects_Academic_Performance`: indica si el uso afecta al rendimiento académico.  
- `Sleep_Hours_Per_Night`: horas de sueño por noche.  
- `Mental_Health_Score`: puntuación de salud mental (escala 4–9 aprox.).  
- `Overall_Impact`: impacto percibido de las redes (Positive, Neutral, Negative).

En total hay 1.705 registros con información cuantitativa y categórica.

## Objetivos del análisis

- Explorar el uso medio de redes sociales entre estudiantes (distribución de horas al día).
- Analizar la relación entre uso de redes y:
  - horas de sueño,  
  - rendimiento académico,  
  - puntuación de salud mental.[file:86]  
- Detectar grupos de estudiantes con patrones similares mediante técnicas de clustering.

## Metodología

1. **Carga y exploración de datos**  
   - Lectura del CSV con `pandas` (`df = pd.read_csv("social.csv")`).
   - Descripción estadística de variables numéricas (media, desviación típica, mínimos, máximos, cuartiles para edad, horas de uso, sueño y salud mental).

2. **Preprocesado**  
   - Codificación de variables categóricas mediante dummies/one‑hot encoding (edad, nivel académico, género, país, impacto, etc.), generando más de 300 columnas binarias.

3. **Modelado / Clustering**  
   - Aplicación de un algoritmo de clustering (por ejemplo K‑Means) sobre las variables transformadas para agrupar estudiantes según sus patrones de uso, sueño e impacto percibido. 
   - Asignación de la etiqueta `Cluster` a cada fila del dataset original.

4. **Análisis de resultados**  
   - Comparación de los clusters en términos de:
     - horas de uso de redes,  
     - horas de sueño,  
     - puntuación de salud mental,  
     - impacto percibido (`Overall_Impact`).

## Requisitos

- Python 3.x  
- Bibliotecas principales:
  - `pandas`
  - (Opcional) `numpy`, `scikit-learn`, `matplotlib`/`seaborn` para visualización y clustering.

Instalación de dependencias recomendada:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Cómo ejecutar el notebook

1. Clona o descarga este repositorio.  
2. Asegúrate de que el archivo `social.csv` está en la misma carpeta que `Social.ipynb`.
3. Abre el notebook con Jupyter:

```bash
jupyter notebook Social.ipynb
```

4. Ejecuta las celdas en orden para:
   - cargar el dataset,  
   - generar estadísticas descriptivas,  
   - preprocesar los datos,  
   - entrenar el modelo de clustering,  
   - visualizar y analizar los grupos resultantes.

## Resultados esperados

El análisis permite identificar perfiles de estudiantes, por ejemplo:

- Estudiantes con alto uso de redes, menos horas de sueño y peor puntuación de salud mental.  
- Estudiantes con uso moderado, buen descanso y percepción positiva del impacto de las redes.[file:86]

Estos insights pueden ayudar a comprender mejor cómo los hábitos digitales se relacionan con el bienestar y el rendimiento académico en población estudiantil.
