# Streamlit Diary - Sentiment Analysis App

Welcome to the Streamlit Diary app! Streamlit Diary is a simple web application built with Streamlit that analyzes the tone of daily diary entries. The app processes text files containing diary entries, calculates positivity and negativity scores using NLTK's SentimentIntensityAnalyzer, and visualizes the results as interactive line charts.

## 📸 Screenshots

### 📊 Sentiment Analysis Graph  
![Sentiment Analysis](https://raw.githubusercontent.com/SorinaO/streamlit_diary/master/Diary_Tone_Analysis1.jpg)

### 📊 Graph with Hover Info  
![File Selection](https://raw.githubusercontent.com/SorinaO/streamlit_diary/master/Diary_Tone_Analysis2.jpg)

## ✨ Features

Automatically reads and processes diary entries from .txt files using the glob library.
Uses NLTK's VADER sentiment analysis to calculate positivity and negativity scores.
Displays results in a clean, interactive web interface powered by Streamlit.
Visualizes sentiment trends over time with line charts.
Easy-to-use and lightweight, with minimal setup required.

## 🛠️ Technologies Used

Python: Core programming language.
Streamlit: For building the web application.
NLTK: For sentiment analysis using the VADER lexicon.
Pandas: For data manipulation and analysis.
Glob: For locating and processing diary files.
