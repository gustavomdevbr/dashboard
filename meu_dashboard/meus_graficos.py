import plotly.express as px
import streamlit as st

def gerar_grafico_barras(df, coluna):
    data = df[coluna].value_counts().reset_index()
    data.columns = [coluna, 'Frequência']
    fig = px.bar(data, x=coluna, y='Frequência', color=coluna,
                 title=f'Distribuição da coluna "{coluna}"',
                 template='plotly_white', text='Frequência')
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title=coluna, yaxis_title='Frequência')
    st.plotly_chart(fig, use_container_width=True)

def gerar_grafico_histograma(df, coluna):
    fig = px.histogram(df, x=coluna, nbins=20,
                       title=f'Histograma da coluna "{coluna}"',
                       template='plotly_white')
    fig.update_layout(xaxis_title=coluna, yaxis_title='Contagem')
    st.plotly_chart(fig, use_container_width=True)

def gerar_grafico_pizza(df, coluna):
    data = df[coluna].value_counts().reset_index()
    data.columns = [coluna, 'Frequência']
    fig = px.pie(data, values='Frequência', names=coluna,
                 title=f'Gráfico de Pizza da coluna "{coluna}"',
                 template='plotly_white')
    st.plotly_chart(fig, use_container_width=True)

def gerar_grafico_boxplot(df, coluna):
    fig = px.box(df, y=coluna,
                 title=f'Boxplot da coluna "{coluna}"',
                 template='plotly_white')
    fig.update_layout(yaxis_title=coluna)
    st.plotly_chart(fig, use_container_width=True)

def gerar_grafico_dispersao(df, col_x, col_y):
    fig = px.scatter(df, x=col_x, y=col_y,
                     title=f'Dispersão entre "{col_x}" e "{col_y}"',
                     template='plotly_white', trendline='ols')
    fig.update_layout(xaxis_title=col_x, yaxis_title=col_y)
    st.plotly_chart(fig, use_container_width=True)
