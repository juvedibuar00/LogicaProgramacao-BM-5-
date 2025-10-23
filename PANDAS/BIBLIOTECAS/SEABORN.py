import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. CARREGAR E PREPARAR DADOS
df = pd.read_csv('data_limpo.csv')

# CORREÇÃO ESSENCIAL: CRIAR A COLUNA ANTES DE USAR
categorias_trabalho = ['Pouco (0-4h)', 'Moderado (5-8h)', 'Muito (9+h)']
df['Categoria_Trabalho'] = pd.cut(df['Hours_Work'], 
                                bins=[-1, 4, 8, 20], 
                                labels=categorias_trabalho)

print(" DataFrame preparado com sucesso!")
print(f"Colunas disponíveis: {df.columns.tolist()}")

# 2. CONFIGURAÇÃO DO SEABORN
sns.set_theme(style="whitegrid")

# 3. GRÁFICOS CORRIGIDOS
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Gráfico 1: Dispersão com Hours_Sleep
sns.scatterplot(data=df, x='Duration', y='Calories', hue='Hours_Sleep', 
                ax=axes[0,0], alpha=0.7)
axes[0,0].set_title('Duração vs Calorias (por Sono)')

# Gráfico 2: Dispersão com Categoria_Trabalho 
sns.scatterplot(data=df, x='Duration', y='Calories', hue='Categoria_Trabalho',
                ax=axes[0,1], alpha=0.7)
axes[0,1].set_title('Duração vs Calorias (por Trabalho)')

# Gráfico 3: Boxplot por Categoria_Trabalho 
sns.boxplot(data=df, x='Categoria_Trabalho', y='Calories', ax=axes[0,2])
axes[0,2].set_title('Calorias por Categoria de Trabalho')
axes[0,2].tick_params(axis='x', rotation=45)

# Gráfico 4: Violin plot 
sns.violinplot(data=df, x='Categoria_Trabalho', y='Calories', ax=axes[1,0])
axes[1,0].set_title('Distribuição por Categoria de Trabalho')
axes[1,0].tick_params(axis='x', rotation=45)

# Gráfico 5: Boxplot agrupado 
sns.boxplot(data=df, x='Hours_Sleep', y='Calories', hue='Categoria_Trabalho', 
           ax=axes[1,1])
axes[1,1].set_title('Calorias por Sono e Trabalho')

# Gráfico 6: Countplot 
sns.countplot(data=df, x='Categoria_Trabalho', ax=axes[1,2])
axes[1,2].set_title('Distribuição por Categoria de Trabalho')
axes[1,2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

print("Todos os gráficos gerados com sucesso!")