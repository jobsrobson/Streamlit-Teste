import streamlit as st
import pandas as pd

"""

#### Esse dashboard é um exemplo de aplicação da biblioteca Streamlit.
O Streamlit é uma biblioteca de código aberto que facilita a criação de aplicativos para visualização de dados na web. O Streamlit transforma os dados em aplicativos interativos e compartilháveis, sem a necessidade de conhecimento prévio de desenvolvimento web. 

O deploy é gratuito.

"""

"""
# Ocorrências de Aviação Civil Brasileira
"""

# Importar os dados
df = pd.read_csv('https://raw.githubusercontent.com/carlosfab/dsnp2/master/datasets/ocorrencias_aviacao.csv')

# Mostrar o dataframe
df

# Criar um gráfico de ocorrências por estado
st.bar_chart(df.ocorrencia_uf.value_counts())

# Criar um dropdown para o usuário selecionar a visualização por estado
uf_selection = st.selectbox('Selecione o UF desejado', df.ocorrencia_uf.unique())

# Filtrar os dados
df_selection = df[df.ocorrencia_uf == uf_selection]

# Mostrar o dataframe filtrado
df_selection

# Mostrar o gráfico filtrado
st.bar_chart(df_selection.ocorrencia_classificacao.value_counts())

