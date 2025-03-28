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

Follow these steps to install and run the **Streamlit Diary** app locally.

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/streamlit_diary.git
cd streamlit_diary

### 2. Install Dependencies
Ensure you have pip installed. Then, install the required Python libraries:
'''pip install -r requirements.txt'''

### 3. Run the Application
After installation, run the Streamlit app:
'''streamlit run app.py'''
The app will open in your browser at http://localhost:8501.

### 4. Access the Application
Open the app in your browser using the URL:
'''http://localhost:8501'''

📝 Usage
Run the app as mentioned in the installation instructions.

Select or upload your diary text file.

View sentiment analysis and graph visualizations of your text.

📄 Requirements
Make sure you have the following installed:

Python 3.7+

Streamlit

Other dependencies listed in requirements.txt

Feel free to make improvements or contact the author for suggestions and contributions.


### Steps to Add to Your GitHub:
1. Copy this `README.md` content.
2. In your repository, create a new file named `README.md`.
3. Paste the copied content into the `README.md`.
4. Commit and push the changes to your GitHub repository.

Let me know if you need further customization or help with anything else!




