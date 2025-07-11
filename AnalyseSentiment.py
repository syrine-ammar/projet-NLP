import requests
import streamlit as st
import time
import nltk
import json
from datetime import datetime

nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

#avec vader
def vader_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    vader_result = sia.polarity_scores(text)
    compound_score = vader_result['compound']
    if compound_score > 0.05:
        sentiment = "Positif 😊"
    elif compound_score < -0.05:
        sentiment = "Négatif 😞"
    else:
        sentiment = "Neutre 😐"
    return sentiment
    #print(f"Sentiment global : {sentiment}")

#avec TextBlob
def textblob_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    if sentiment.polarity > 0:
        sentiment_interpretation = "Positif 😊"
    elif sentiment.polarity < 0:
        sentiment_interpretation = "Négatif 😞"
    else:
        sentiment_interpretation = "Neutre 😐"
    return sentiment_interpretation
    #print(f"Sentiment global : {sentiment_interpretation}")

# Fonction pour interagir avec OpenAI via le backend Node.js
def openai_analysis(user_input):
    try:
        response = requests.post("http://localhost:3000/api/analyze", json={"message": user_input})
        if response.status_code == 200 and response.json().get("success"):
            return response.json().get("result")
        else:
            return "Erreur avec l'API OpenAI."
    except Exception as e:
        return f"Erreur: {e}"
    
def save_results_with_date(user_input, vader_result, openai_result):
    current_date = datetime.now().strftime("%Y-%m-%d")
    try:
        with open("results.json", "r",encoding="utf-8") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = {}
    if current_date not in history:
        history[current_date] = []
    
    history[current_date].append({
        "user_input": user_input,
        "vader_sentiment": vader_result,
        "openai_analysis": openai_result
    })
    with open("results.json", "w",encoding="utf-8") as f:
        json.dump(history, f, indent=4,ensure_ascii=False)
def main():
    #importer les styles
    st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

    st.title("Bienvenue sur l'analyseur de sentiments avec historique 😃📜")
    user_input = st.text_area("Écrivez votre texte ici ✍️", "", height=150, max_chars=2000,
                              help="Écrivez une phrase ou un paragraphe pour analyser le sentiment.")
    if st.button("Analyser le sentiment 🧐"):
        progress_bar = st.progress(0)
        for perc_completed in range(100):
            time.sleep(0.02)
            progress_bar.progress(perc_completed + 1)
        
        if user_input:
            vader_result = vader_sentiment(user_input)
            st.markdown(f"### Sentiment détecté : {vader_result}")
  
            openai_result = openai_analysis(user_input)
            st.markdown(f"### Analyse détaillée : {openai_result}")
            save_results_with_date(user_input, vader_result, openai_result)
        else:
            st.error("Veuillez entrer du texte pour l'analyse. 🚫")