import streamlit as st
import pandas as pd
st.markdown('---')
st.title('Tabuada de multiplicação online')
numero1 = st.number_input('Insira um número para verificar sua tabuada: ', step =int());

botao = st.button('Calcular tabuada')
if (botao == True):
    for i in range(1, 11):
        st.write(str(numero1) + ' x ' + str(i) + ' = ' + str(numero1 * i))
st.caption('Esta tabuada é simplificada e busca auxiliar o processo de aprendizado!')
