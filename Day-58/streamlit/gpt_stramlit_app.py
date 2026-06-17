import streamlit as st
from utils import SentimentAnalyser

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Movie Review Sentiment Analysis",
    page_icon="🎬",
    layout="wide"
)

# -------------------- Model Loading --------------------
analyser_object = SentimentAnalyser(
    model_path="/home/shailesh/Desktop/education/DSML-10/Day-57/SVM_model.joblib",
    vector_path="/home/shailesh/Desktop/education/DSML-10/Day-57/Word2Vec_imdb_250.joblib"
)

# -------------------- Header --------------------
st.markdown(
    """
    <div style="text-align:center; padding:20px;">
        <h1>🎬 Movie Review Sentiment Analyzer</h1>
        <p style="font-size:18px; color:gray;">
            Discover whether your movie review expresses a Positive or Negative sentiment.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------- Input Section --------------------
with st.container(border=True):

    st.subheader("✍️ Enter Your Review")

    user_review = st.text_area(
        label="Enter Review",
        height=250,
        placeholder="Write your movie review here or paste it from another source..."
    )

    btn_click = st.button(
        "🔍 Find My Sentiment",
        use_container_width=True
    )

# -------------------- Prediction --------------------
sentiment = ""

if btn_click:

    if len(user_review.split()) < 50:
        st.warning("⚠️ Please enter at least 50 words for better prediction accuracy.")
    else:
        with st.spinner("Analyzing sentiment..."):
            sentiment = analyser_object.prediction_pipeline(
                user_input=user_review
            )

# -------------------- Output --------------------
if sentiment:
    st.divider()
    if sentiment == "Positive":
        st.success(f"✅ Sentiment Detected: **{sentiment}**")
    else:
        st.error(f"❌ Sentiment Detected: **{sentiment}**")

    # st.metric(
    #     label="Prediction Result",
    #     value=sentiment
    # )