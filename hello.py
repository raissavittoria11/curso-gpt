import streamlit as st

st.title("Bem vindo à minha primeira página WEB")
st.subheader("Desenvolvido por: Platini")

nome = st.text_input("Digite o seu nome: ")
idade = st.text_input("Digite a sua idade: ")

if st.button("Cadastrar"):
    if nome and idade:
        st.success("Usuário cadastrado com sucesso!")
    else: 
        st.error("Dados incompletos")
    
    
    
    
    
