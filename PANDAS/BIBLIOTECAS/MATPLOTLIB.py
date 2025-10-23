import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde


# Carregar a base de dados
df = pd.read_csv('data_limpo.csv')
print(df.head())


# PASSO 1: Gráfico de dispersão básico
plt.figure(figsize=(10, 6))
plt.scatter(df['Duration'], df['Calories'], alpha=0.7)
plt.xlabel('Duração do Exercício (minutos)')
plt.ylabel('Calorias Queimadas')
plt.title('Relação entre Duração e Calorias - Matplotlib')
plt.grid(True, alpha=0.3)
plt.show()


# PASSO 2: Dispersão com cores por categoria
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['Duration'], df['Calories'], 
                     c=df['Hours_Sleep'], cmap='viridis', alpha=0.7)
plt.colorbar(scatter, label='Horas de Sono')
plt.xlabel('Duração (minutos)')
plt.ylabel('Calorias Queimadas')
plt.title('Duração vs Calorias (Colorido por Horas de Sono)')
plt.show()


# PASSO 3: Dispersão com tamanhos variáveis
plt.figure(figsize=(10, 6))
sizes = df['Pulse'] / df['Pulse'].max() * 100  # Normalizar para tamanhos entre 0-100
plt.scatter(df['Duration'], df['Calories'], s=sizes, alpha=0.6, color='red')
plt.xlabel('Duração (minutos)')
plt.ylabel('Calorias Queimadas')
plt.title('Duração vs Calorias (Tamanho = Pulsação)')
plt.show()




# Gráficos de Linha
# PASSO 1: Gráfico de linha simples
plt.figure(figsize=(12, 6))

# Ordenar por duração para ter uma linha coerente
df_sorted = df.sort_values('Duration')
plt.plot(df_sorted['Duration'], df_sorted['Calories'], 
         marker='o', linewidth=2, markersize=4)
plt.xlabel('Duração (minutos)')
plt.ylabel('Calorias Queimadas')
plt.title('Relação Duração-Calorias (Linha)')
plt.grid(True, alpha=0.3)
plt.show()



# PASSO 2: Múltiplas linhas
plt.figure(figsize=(12, 6))

# Agrupar por horas de sono e calcular médias
for sleep_hours in sorted(df['Hours_Sleep'].unique()):
    df_sleep = df[df['Hours_Sleep'] == sleep_hours]
    duration_means = df_sleep.groupby('Duration')['Calories'].mean()
    plt.plot(duration_means.index, duration_means.values, 
             marker='o', label=f'{sleep_hours}h sono', linewidth=2)

plt.xlabel('Duração (minutos)')
plt.ylabel('Calorias Médias')
plt.title('Calorias Médias por Duração e Horas de Sono')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()




# Histogramas e distribuições
# PASSO 1: Histograma básico
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.hist(df['Calories'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Calorias Queimadas')
plt.ylabel('Frequência')
plt.title('Distribuição de Calorias')

plt.subplot(2, 2, 2)
plt.hist(df['Calories'], bins=20, density=True, alpha=0.7, color='lightgreen')
density = gaussian_kde(df['Calories'])
xs = np.linspace(df['Calories'].min(), df['Calories'].max(), 200)
plt.plot(xs, density(xs), 'r-', linewidth=2)
plt.xlabel('Calorias Queimadas')
plt.ylabel('Densidade')
plt.title('Distribuição com Curva de Densidade')




# PASSO 3: Múltiplos histogramas
plt.subplot(2, 2, 3)
for sleep_hours in [7, 8]:
    data = df[df['Hours_Sleep'] == sleep_hours]['Calories']
    plt.hist(data, bins=15, alpha=0.6, label=f'{sleep_hours}h sono', density=True)
plt.xlabel('Calorias Queimadas')
plt.ylabel('Densidade')
plt.title('Comparação por Horas de Sono')
plt.legend()



# PASSO 4: Histograma cumulativo
plt.subplot(2, 2, 4)
plt.hist(df['Calories'], bins=20, cumulative=True, 
         color='orange', alpha=0.7, edgecolor='black')
plt.xlabel('Calorias Queimadas')
plt.ylabel('Frequência Acumulada')
plt.title('Distribuição Acumulativa de Calorias')

plt.tight_layout()
plt.show()





# Gráficos de Barras
# PASSO 1: Gráfico de barras vertical
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
calories_por_sono = df.groupby('Hours_Sleep')['Calories'].mean()
plt.bar(calories_por_sono.index, calories_por_sono.values, 
        color='lightblue', edgecolor='navy')
plt.xlabel('Horas de Sono')
plt.ylabel('Calorias Médias')
plt.title('Calorias Médias por Horas de Sono')

# PASSO 2: Gráfico de barras horizontal
plt.subplot(1, 2, 2)
work_counts = df['Hours_Work'].value_counts().head(8)
plt.barh(range(len(work_counts)), work_counts.values)
plt.yticks(range(len(work_counts)), work_counts.index)
plt.xlabel('Número de Pessoas')
plt.ylabel('Horas de Trabalho')
plt.title('Distribuição de Horas de Trabalho')

plt.tight_layout()
plt.show()

# PASSO 3: Barras agrupadas
plt.figure(figsize=(10, 6))
categorias_trabalho = ['Pouco (0-4h)', 'Moderado (5-8h)', 'Muito (9+h)']
df['Categoria_Trabalho'] = pd.cut(df['Hours_Work'], 
                                bins=[-1, 4, 8, 20], 
                                labels=categorias_trabalho)

calories_por_grupo = df.groupby(['Categoria_Trabalho', 'Hours_Sleep'])['Calories'].mean().unstack()

width = 0.25
x = np.arange(len(categorias_trabalho))

for i, sleep_hours in enumerate([7, 8]):
    plt.bar(x + i*width, calories_por_grupo[sleep_hours], 
            width=width, label=f'{sleep_hours}h sono')

plt.xlabel('Categoria de Trabalho')
plt.ylabel('Calorias Médias')
plt.title('Calorias por Trabalho e Sono')
plt.xticks(x + width/2, categorias_trabalho)
plt.legend()
plt.show()




# Boxplots e Visualizações Estatísticas
# PASSO 1: Boxplot básico
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.boxplot(df['Calories'])
plt.ylabel('Calorias Queimadas')
plt.title('Boxplot de Calorias')

# PASSO 2: Múltiplos boxplots
plt.subplot(1, 2, 2)
data_por_sono = [df[df['Hours_Sleep'] == i]['Calories'] for i in sorted(df['Hours_Sleep'].unique())]
plt.boxplot(data_por_sono, labels=sorted(df['Hours_Sleep'].unique()))
plt.xlabel('Horas de Sono')
plt.ylabel('Calorias Queimadas')
plt.title('Calorias por Horas de Sono')

plt.tight_layout()
plt.show()

# PASSO 3: Violin plot manual (simulado com múltiplas densidades)
plt.figure(figsize=(10, 6))
for i, sleep_hours in enumerate([7, 8]):
    data = df[df['Hours_Sleep'] == sleep_hours]['Calories']
    density = gaussian_kde(data)
    xs = np.linspace(data.min(), data.max(), 100)
    plt.fill_betweenx(xs, i + 0.4 * density(xs)/density(xs).max(), 
                     i - 0.4 * density(xs)/density(xs).max(), 
                     alpha=0.5, label=f'{sleep_hours}h sono')

plt.yticks([0, 1], ['7h', '8h'])
plt.xlabel('Densidade')
plt.ylabel('Horas de Sono')
plt.title('Distribuição de Calorias por Sono (Violin Simulado)')
plt.legend()
plt.show()