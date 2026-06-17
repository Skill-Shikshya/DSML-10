import streamlit as st
from utils import SentimentAnalyser

analyser_object = SentimentAnalyser(
    model_path = "/home/shailesh/Desktop/education/DSML-10/Day-57/SVM_model.joblib", 
    vector_path = "/home/shailesh/Desktop/education/DSML-10/Day-57/Word2Vec_imdb_250.joblib"
)

## Streamlit Design
st.title(
    "Welcome to movie review sentiment prediction system", text_alignment="center"
)

user_review = st.text_area(
    "Enter your review ! ",
    height=300,
    placeholder= "Write you review or paste it from somewhere."
)

btn_click = st.button(
    label= "Find my sentiment",
    icon=":material/search:"
)

# Prediction
sentiment = ""
if btn_click:
    if len(user_review) > 50:
        sentiment = analyser_object.prediction_pipeline(
            user_input= user_review
        )
    else:
        print("At least 50 words")


# Output
if sentiment:
    icon = "✅" if sentiment == "Positive" else "❌"
    color = "green" if sentiment=="Positive" else "red"
    st.subheader(
        f"{icon} :{color}[{sentiment}]",
        text_alignment="center"
    )