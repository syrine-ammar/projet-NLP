import streamlit as st
import time
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import pandas as pd
import spacy
from spacy import displacy

#nltk.download('punkt')

nlp = spacy.load("fr_core_news_sm")

def main():
    #importer les styles
    st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
    
    st.title("Bienvenue dans notre analyseur lexical et syntaxique !🔍")
    user_input = st.text_area("Écrivez votre texte ici ✍️", "", height=150, max_chars=1000,
                              help="Écrivez une phrase ou un paragraphe à analyser.")
    
    # devisier la page en deux parties : une pour l'analyse lexical et une pour l'analyse syntaxique
    col1 , col2 = st.columns(2)
    with col1:
        st.header("Analyser lexical 🧐")
        if st.button("Analyse lexicale 🧑‍💻"):
            if user_input:
                progress_bar = st.progress(0)
                for perc_completed in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(perc_completed+1)
                
                # faire l'analyse lexicale
                st.subheader("Tokenisation")
                tokens = word_tokenize(user_input)
                st.subheader(f"Tokens extraits ({len(tokens)} au total):")
                st.write(tokens)
                
                st.subheader("Classification des tokens")
                stop_words = set(stopwords.words("french")) 
                tokens_filtered = [token for token in tokens if token.isalnum()]
                stopwords_filtered = [token for token in tokens_filtered if token.lower() in stop_words]
                keywords = [token for token in tokens_filtered if token.lower() not in stop_words]
                st.write("**Mots-clés (sans les stopwords) :**", keywords)
                st.write("**Stopwords détectés :**", stopwords_filtered)

                st.subheader("Fréquence des tokens")
                freq_dist = FreqDist(keywords)
                freq_df = pd.DataFrame(freq_dist.items(), columns=["Token", "Fréquence"]).sort_values(by="Fréquence", ascending=False)
                st.dataframe(freq_df)

            else :
                st.markdown("<p class='error-text'>Veuillez entrer un texte à analyser 🚫.</p>", unsafe_allow_html=True)           
    
    with col2:
        st.header("Analyser syntaxique 🔠")
        #st.write("Ceci est la deuxième colonne.")
        if st.button("Analyse syntaxique 🖥️"):
            if user_input:
                progress_bar = st.progress(0)
                for perc_completed in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(perc_completed+1)
                # faire l'analyse syntaxique
                doc = nlp(user_input)
                token_data = [
                {"Token": token.text, "Lemma": token.lemma_, "POS": token.pos_, "Dependency": token.dep_}
                for token in doc] 
                st.dataframe(token_data)
                st.subheader("Arbre syntaxique")
                svg_tree = displacy.render(doc, style="dep", jupyter=False, options={"compact": True})
                st.markdown(f'<div>{svg_tree}</div>', unsafe_allow_html=True)
            
            
            else :
                st.markdown("<p class='error-text'>Veuillez entrer un texte à analyser 🚫.</p>", unsafe_allow_html=True)           
    