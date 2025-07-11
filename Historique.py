import streamlit as st
import json

def main():
    #importer les styles
    st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
    st.title("Historique des analyses 📜")
    try:
        with open("results.json", "r",encoding="utf-8") as f:
            history = json.load(f)

        dates = list(history.keys())
        selected_date = st.selectbox("Sélectionnez une date", dates)

        if selected_date:
            entries = history[selected_date]
            for entry in entries:
                st.markdown("<p class='title'>Journal :</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='content'>{entry['user_input']}</p>", unsafe_allow_html=True)

                st.markdown("<p class='title'>Sentiment détecté :</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='content'>{entry['vader_sentiment']}</p>", unsafe_allow_html=True)

                st.markdown("<p class='title'>Analyse mentale et remèdes :</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='content'>{entry['openai_analysis']}</p>", unsafe_allow_html=True)
    except json.JSONDecodeError:
        st.error("Le fichier JSON est corrompu ou mal formé.")