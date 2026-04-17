"""
Playground — Seaborn: Gráficos de relaciones
Módulo: SEABORN
Fecha: 2026-04-17 11:47

Enunciado:
Código escrito en el playground durante el estudio de la teoría

"""
import seaborn as sns
import matplotlib.pyplot as plt
penguins = sns.load_dataset('penguins').dropna()

# hue CATEGÓRICA: paleta discreta (un color por categoría)
sns.scatterplot(data=penguins, x='bill_length_mm',
                y='bill_depth_mm',
                hue='species',          # 3 categorías -> 3 colores
                palette='Set2')

# hue NUMÉRICA: paleta continua (gradiente)
sns.scatterplot(data=penguins, x='bill_length_mm',
                y='bill_depth_mm',
                hue='body_mass_g',      # Valores continuos -> gradiente
                palette='viridis')