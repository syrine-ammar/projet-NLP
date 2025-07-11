import streamlit as st
import Acceuil as acceuil
import AnalyseLS as analyse_ls
import AnalyseSentiment as analyse_sentiment

st.set_page_config(page_title="Analyse des Sentiments", page_icon=":speech_balloon:", layout="wide")
#page = st.sidebar.radio("Naviguer vers", ["Accueil", "Analyse Lexicale et Syntaxique", "Analyse des Sentiments"])
page = st.sidebar.selectbox("Naviguer vers",
    options=["Accueil", "Analyse Lexicale & Syntaxique", "Analyse des Sentiments"])

if page == "Accueil":
    acceuil.main()
elif page == "Analyse Lexicale & Syntaxique":
    analyse_ls.main()
elif page == "Analyse des Sentiments":
    analyse_sentiment.main()

st.markdown("""<hr><footer>Réalisé avec ❤️ par ING1-Info</footer>""", unsafe_allow_html=True)