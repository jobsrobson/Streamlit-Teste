import streamlit as st
import pandas as pd

"""

#### Esse dashboard é um exemplo de aplicação da biblioteca Streamlit.
O Streamlit é uma biblioteca de código aberto que facilita a criação de aplicativos para visualização de dados na web. O Streamlit transforma os dados em aplicativos interativos e compartilháveis, sem a necessidade de conhecimento prévio de desenvolvimento web. 
O código é desenvolvido em Python usando a biblioteca Streamlit.

Para fazer o deploy, basta criar um novo repositório público no GitHub (gratuito) com os arquivos app.py e requirements.txt. Após, basta conectar esse repositório ao site do Streamlit. A plataforma gera um URL e hospeda todo o aplicativo.
Também é possível inserir o aplicativo em um website próprio, por meio de um iframe.

---

"""

"""
# Ocorrências na Aviação Civil Brasileira
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

