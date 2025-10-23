import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def plotly_analysis_completa():
    # 1. CARREGAR E PREPARAR DADOS
    df = pd.read_csv('data_limpo.csv')

    # Calcular a matriz de correlação
    correlation_matrix = df.corr()

    # Heatmap Interativo
    fig = px.imshow(correlation_matrix,
                   title='Heatmap de Correlação Interativo - Plotly',
                   color_continuous_scale='RdBu',
                   aspect='auto')
    fig.show()

# Chama a função principal para gerar o heatmap de correlação
if __name__ == '__main__':
    plotly_analysis_completa()

# Heatmap de Dados Agrupados Interativo
# garante que df exista e constrói uma pivot_table segura
df = pd.read_csv('data_limpo.csv')

if {'Sleep', 'Work', 'Calories'}.issubset(df.columns):
    pivot_table = df.pivot_table(index='Sleep', columns='Work', values='Calories', aggfunc='mean')
else:
    # fallback para evitar erro se as colunas esperadas não existirem
    pivot_table = df.corr()

fig = px.imshow(pivot_table,
               title='Heatmap de Calorias por Sono e Trabalho - Plotly',
               color_continuous_scale='YlOrRd',
               aspect='auto')
fig.show()

# Heatmap 2D de Densidade (somente se as colunas existirem)
if {'Duration', 'Calories'}.issubset(df.columns):
    fig = px.density_heatmap(df, x='Duration', y='Calories',
                       title='Heatmap 2D de Densidade - Plotly')
    fig.show()