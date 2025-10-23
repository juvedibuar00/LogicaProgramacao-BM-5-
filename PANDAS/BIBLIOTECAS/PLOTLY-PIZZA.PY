
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
df = pd.read_csv('data_limpo.csv')
def plotly_analysis_completa():
    # 1. CARREGAR E PREPARAR DADOS
    df = pd.read_csv('data_limpo.csv')
# Pie Chart Interativo
fig = px.pie(df, names='Hours_Sleep', 
            title='Distribuição de Horas de Sono - Plotly')
fig.show()

# Donut Chart Interativo
fig = px.pie(df, names='Categoria_Trabalho', 
            hole=0.4,
            title='Gráfico de Donut Interativo - Plotly')
fig.show()

# Pie Chart com Dados Agregados
calories_por_sono = df.groupby('Hours_Sleep')['Calories'].sum().reset_index()
fig = px.pie(calories_por_sono, names='Hours_Sleep', values='Calories',
            title='Proporção de Calorias por Horas de Sono - Plotly')
fig.show()