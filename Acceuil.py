import streamlit as st

def main():
    # importer les styles
    st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
    
    st.title("Bienvenue sur notre site d'analyse de sentiments 📝")
    st.markdown('<h2 class="header">Un outil puissant pour explorer vos textes 📊</h2>', unsafe_allow_html=True)
    st.markdown("""
        <p class="intro">
        Cette application vous permet de réaliser :
        <ul>
            <li>Une analyse lexicale et syntaxique détaillée 🔤.</li>
            <li>Une analyse des sentiments pour mieux comprendre les émotions dans vos textes.</li>
        </ul>
        </p>""", unsafe_allow_html=True)
    
    st.info("Utilisez le menu latéral pour commencer ! 🚀")
