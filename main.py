import streamlit as st 
import pandas as pd
import glob
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk


nltk.download("vader_lexicon")

def analyze_tone(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    positivity = sentiment["pos"] # Positivity score
    negativity = sentiment["neg"] # Negativity score
    return positivity, negativity

# Step 2: Read and Sort the Files
def get_sorted_diary_files():
    files = glob.glob("C:/MY-COMPUTER-1/streamlit_diary/diary/*.txt")
    return sorted(files, key=lambda x: datetime.strptime
                  (x.split("\\")[-1].split(".")[0], "%Y-%m-%d"))

# Step 3: Process Each File
def process_diary_entries(files):
    dates = []
    positivity_scores = []
    negativity_scores = []

    for file in files:
        with open(file, "r") as f:
            text = f.read()
            positivity, negativity = analyze_tone(text)
            dates.append(file.split("\\")[-1].split(".")[0])
            positivity_scores.append(positivity)
            negativity_scores.append(negativity)

    return dates, positivity_scores, negativity_scores

#Step 4: Plot the Results
def plot_tone_with_streamlit(dates, positivity_scores, negativity_scores):

    # Create a DataFrame for plotting
    data = pd.DataFrame({
        "Date": dates,
        "Positivity": positivity_scores,
        "Negativity": negativity_scores
    })
    data["Date"] = pd.to_datetime(data["Date"]) # Convert dates to datetime
    data = data.set_index("Date") # Set Date as index     

    # Plot using Streamlit
    st.line_chart(data) 

# Step 5: Integrate Everything in the Streamlit App  
def main():
    st.title("Diary Tone Analysis")
    st.write("This app analyzes the tone of your diary entries.")

    # Get and display the list of files
    files = get_sorted_diary_files()
    
    # Check if files exist
    if not files:
        st.error("No diary files found in the directory. Please add some files.")
        return

    # Process the files
    dates, positivity_scores, negativity_scores = process_diary_entries(files)

    # Display the results in a table format
    st.write("### Processed Diary Analysis")
    df = pd.DataFrame({
        "Date": dates,
        "Positivity Score": positivity_scores,
        "Negativity Score": negativity_scores
    })
    
    st.table(df)  # Display table in Streamlit

    # Check if data is valid before plotting
    if not dates or not positivity_scores or not negativity_scores:
        st.error("No data available to plot. Please check your diary files.")
        return

    # Plot the results
    plot_tone_with_streamlit(dates, positivity_scores, negativity_scores)

if __name__ == "__main__":
       main()  # Start the Streamlit app
