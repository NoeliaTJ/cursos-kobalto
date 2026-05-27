# Análisis de repositorios de GitHub

Este proyecto analiza un conjunto de datos de repositorios de GitHub utilizando múltiples indicadores de actividad, calidad y metadatos, como estrellas, forks, issues, pull requests, contribuidores, commits e información de licencias.[file:88]

## Dataset

El dataset contiene unos 5.500 repositorios con los siguientes tipos de variables:

**Actividad y popularidad**

- `stars`: número de estrellas.  
- `forks`: número de forks.  
- `watchers`: número de watchers.  
- `open_issues`: issues abiertas actualmente.  
- `closed_issues`: issues cerradas.  
- `open_pull_requests`: pull requests abiertas.  
- `merged_pull_requests`: pull requests fusionadas (merge).  
- `contributors`: número de contribuidores.  
- `commits`: número total de commits.  
- `releases`: número de versiones etiquetadas (releases).

**Metadatos del repositorio**

- `repo_name`: nombre del repositorio.  
- `description`: descripción breve del proyecto.  
- `size_kb`: tamaño del repositorio en kilobytes.

**Variables booleanas / categóricas**

- `has_ci`: indica si el repositorio tiene integración continua (CI) configurada.
- `test_coverage`: cobertura de tests aproximada para los repositorios que la reportan.
- `has_code_of_conduct`: existencia de un código de conducta.  
- `has_contributing_guide`: existencia de una guía de contribución.  
- `has_wiki`: si el proyecto utiliza wiki.  
- `has_pages`: si tiene GitHub Pages activado.  
- `has_discussions`: si utiliza GitHub Discussions.  
- `is_archived`: si el repositorio está archivado.  
- `is_fork`: si el repositorio es un fork.

**Licencias y rama por defecto**

Variables one‑hot de licencia, por ejemplo:

- `license_Apache-2.0`  
- `license_BSD-3`  
- `license_GPL-3.0`  
- `license_ISC`  
- `license_LGPL-3.0`  
- `license_MIT`  
- `license_MPL-2.0`  
- `license_Unlicense`  

y variables que indican la rama por defecto:

- `default_branch_main`  
- `default_branch_master`.

El notebook incluye estadísticas descriptivas para las variables numéricas (count, mean, std, min, max y cuartiles) sobre estas métricas.

## Objetivos del análisis

- Resumir y comprender la distribución de las métricas de actividad de los repositorios (stars, forks, issues, PRs, commits, releases, tamaño, etc.). 
- Explorar las relaciones entre popularidad (stars, forks) y colaboración (issues, PRs, contribuidores). 
- Investigar la presencia de buenas prácticas de proyecto, como CI, tests, código de conducta, guías de contribución y funcionalidades de documentación. 
- Analizar cómo varían las licencias y la rama por defecto entre distintos repositorios.

## Metodología

1. **Carga y limpieza de datos**  
   - Carga del dataset de repositorios de GitHub en un DataFrame de `pandas`.  
   - Revisión de valores nulos y consistencia básica de las métricas.

2. **Estadística descriptiva**  
   - Cálculo de resúmenes estadísticos para columnas numéricas como `stars`, `forks`, `watchers`, `open_issues`, `closed_issues`, `open_pull_requests`, `merged_pull_requests`, `contributors`, `commits`, `releases`, `size_kb`.[file:88]  
   - Análisis de rangos de distribución mediante count, mean, std, min, max y cuartiles.

3. **Ingeniería de variables y codificación**  
   - Uso de variables one‑hot para las licencias (por ejemplo `license_MIT`, `license_Apache-2.0`).  
   - Empleo de indicadores booleanos (`has_ci`, `has_code_of_conduct`, `has_contributing_guide`, etc.) para caracterizar las prácticas de gobernanza y tooling del proyecto.[file:88]

4. **Análisis exploratorio**  
   - Comparación de métricas de actividad entre distintos tipos de proyectos (por ejemplo, por licencia, rama por defecto, presencia de CI).
   - Identificación de repositorios con valores muy altos de estrellas o forks y revisión de sus metadatos como ejemplos representativos (por ejemplo, `serve-ml`, `easy-link`, `turbo-core-forge`, `deep-graph-dash`).[file:88]

## Requisitos

- Python 3.x  
- Librerías principales:
  - `pandas`
  - `numpy`
  - `matplotlib` y/o `seaborn` para visualización
  - Opcionalmente `scikit-learn` para análisis más avanzado.

Instalación recomendada:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Cómo ejecutar el notebook

1. Clona o descarga este repositorio.  
2. Asegúrate de que el dataset de repositorios de GitHub utilizado en `Github.ipynb` está en la misma carpeta que el notebook (por ejemplo `github_repos.csv` o un nombre similar).[file:88]  
3. Abre el notebook con Jupyter:

```bash
jupyter notebook Github.ipynb
```

4. Ejecuta las celdas en orden para:
   - cargar y explorar el dataset,  
   - calcular estadísticas descriptivas,  
   - analizar patrones de actividad y metadatos entre repositorios.

## Resultados esperados

Con este análisis se pretende:

- Entender los rangos típicos de stars, forks, issues y otras métricas de actividad en una muestra amplia de repositorios.  
- Observar cómo se relacionan las métricas de colaboración y mantenimiento (issues, PRs, contribuidores) con la popularidad y el tamaño del proyecto. 
- Analizar la adopción de licencias, integración continua, documentación y funcionalidades de comunidad en el conjunto de repositorios.

- ## Resultados esperados

Con este análisis se pretende:

- Entender los rangos típicos de stars, forks, issues y otras métricas de actividad en una muestra amplia de repositorios.  
- Observar cómo se relacionan las métricas de colaboración y mantenimiento (issues, PRs, contribuidores) con la popularidad y el tamaño del proyecto.  
- Analizar la adopción de licencias, integración continua, documentación y funcionalidades de comunidad en el conjunto de repositorios.
