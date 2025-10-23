import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde


# Carregar a base de dados
df = pd.read_csv('data_limpo.csv')

# Gráfico de Pizza Básico
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sono_counts = df['Hours_Sleep'].value_counts()
plt.pie(sono_counts.values, labels=sono_counts.index, autopct='%1.1f%%')
plt.title('Distribuição de Horas de Sono - Matplotlib')

# Gráfico de Pizza com Ênfase
plt.subplot(1, 2, 2)
work_top = df['Hours_Work'].value_counts().head(5)
explode = [0.1 if i == work_top.index[0] else 0 for i in range(len(work_top))]
plt.pie(work_top.values, labels=work_top.index, autopct='%1.1f%%', 
        explode=explode, shadow=True)
plt.title('Distribuição de Horas de Trabalho - Matplotlib')

plt.tight_layout()
plt.show()

# Gráfico de Donut
plt.figure(figsize=(8, 8))
categoria_counts = df['Categoria_Trabalho'].value_counts()
plt.pie(categoria_counts.values, labels=categoria_counts.index, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)
plt.title('Gráfico de Donut - Categorias de Trabalho - Matplotlib')
plt.show()