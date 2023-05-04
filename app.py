import streamlit as st
import spacy
import pandas as pd




import requests

base_currency = 'BRL'
#symbol = 'CORN' 
endpoint = 'latest'
access_key = 'i6yu38lnwbjo4bze22tc8ucj5343je63lqf39cguse742gxy3lnf96ousmqr'

def lookfor(symbol):
    #lista = ["SOYBEANS", "ARABICA COFFEE", "CORN", "SUGAR"]
    if lista==[]:
        return st.write('Escolha um ativo')
    else:
        #results =[]
        for symbol in lista:
            resp = requests.get(
            'https://commodities-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol)
            data = resp.json()
            # Convert the JSON object to a DataFrame
            df = pd.DataFrame(data)
        return (df)

st.title("Pesquisar a taxa")

form1= st.sidebar.form(key="Options")
st.sidebar.header("Commodities")

lista=st.sidebar.multiselect("Selecione o ativo que deseja consultar", ["ALU", "COFFEE", "CORN","CANO","COCOA", "SUGAR","COTTON","XAU","MILK","POTATOES","RICE","SOYBEAN"])


st.dataframe(lookfor(lista))