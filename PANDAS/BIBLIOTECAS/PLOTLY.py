import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def plotly_analysis_completa():
    # 1. CARREGAR E PREPARAR DADOS
    df = pd.read_csv('data_limpo.csv')
    
    # 🛠️ CORREÇÃO ESSENCIAL
    categorias_trabalho = ['Pouco (0-4h)', 'Moderado (5-8h)', 'Muito (9+h)']
    df['Categoria_Trabalho'] = pd.cut(df['Hours_Work'], 
                                    bins=[-1, 4, 8, 20], 
                                    labels=categorias_trabalho)
    
    print("✅ DataFrame preparado para Plotly!")
    print(f"Colunas disponíveis: {df.columns.tolist()}")
    
    # 2. GRÁFICOS PRINCIPAIS CORRIGIDOS
    
    # Gráfico 1: Dispersão com Categoria_Trabalho
    fig1 = px.scatter(df, x='Duration', y='Calories',
                     color='Categoria_Trabalho',
                     title='Duração vs Calorias (Corrigido) - Plotly')
    fig1.show()
    
    # Gráfico 2: Boxplot por Categoria_Trabalho
    fig2 = px.box(df, x='Categoria_Trabalho', y='Calories',
                 title='Calorias por Categoria de Trabalho (Corrigido) - Plotly')
    fig2.show()
    
    # Gráfico 3: Histograma comparativo
    fig3 = px.histogram(df, x='Calories', color='Categoria_Trabalho',
                       barmode='overlay',
                       title='Distribuição por Categoria de Trabalho (Corrigido) - Plotly')
    fig3.show()
    
    # Gráfico 4: Gráfico 3D
    fig4 = px.scatter_3d(df, x='Duration', y='Pulse', z='Calories',
                        color='Categoria_Trabalho',
                        title='Gráfico 3D (Corrigido) - Plotly')
    fig4.show()
    
    print("🎉 Todos os gráficos Plotly gerados com sucesso!")

# Executar análise completa
plotly_analysis_completa()