import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

def simples_plot(title,data,rotulo):

    # Define o tamanho da figura com base nas entradas do usuário
    plt.figure(figsize=(10, 4))
    plt.title(f"{title}")
    plt.scatter(data[:,0], data[:,1], c=rotulo)
    return plt

st.set_page_config(page_title="Maykoll Rocha - Portifolio Pessoal",
            page_icon=None ,
            layout="wide",
            initial_sidebar_state="collapsed",
        )

st.write("Hello Word")
st.text("Hello Word")
st.latex(r"P(n, k) = \frac{1}{k!} \sum_{j=1}^{k} (-1)^{k-j} \binom{k}{j} j^n ")
st.markdown(r"""
            $$ P(n, k) = \frac{1}{k!} \sum_{j=1}^{k} (-1)^{k-j} \binom{k}{j} j^n $$  
            maykoll 
            rocha
            """)

# Baixa os dados dos arquivos
#data_response = requests.get('https://raw.githubusercontent.com/MaykollRocha/Data_Sets/main/data.txt')
#rotulo_response = requests.get('https://raw.githubusercontent.com/MaykollRocha/Data_Sets/main/rotulos.txt')

# Carrega os dados no NumPy
#data = np.loadtxt(data_response.text.splitlines())
#rotulo = np.loadtxt(rotulo_response.text.splitlines())

#st.pyplot(simples_plot("Base de Dados Tratada",data,rotulo))
# my_dataframe = pd.read_csv("Funcionarios.csv") 
# st.dataframe(my_dataframe)



entra = st.number_input("Entra numero")
st.write(entra)
color  = st.color_picker('Pick a color',)
st.write(color)

data = st.date_input("Entre com o dia")
st.write(data)


with st.sidebar:
    valor = ''

    if st.button("Valor"):
        valor = 'entre'

    match valor:    
        case "entre":
            st.write("saiu")

        case _: st.write("defalt")
