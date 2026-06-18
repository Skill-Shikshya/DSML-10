from pydantic import BaseModel
from fastapi import FastAPI
from utils import SentimentAnalyser

app = FastAPI()

sentiment_analyser = SentimentAnalyser(
    model_path = "/home/shailesh/Desktop/education/DSML-10/Day-57/SVM_model.joblib", 
    vector_path = "/home/shailesh/Desktop/education/DSML-10/Day-57/Word2Vec_imdb_250.joblib"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


class UserInput(BaseModel):
    review : str
    

@app.post("/analyse/review")
def get_sentiment(user_input : UserInput)-> dict:
    
    response = sentiment_analyser.prediction_pipeline(
        str(user_input.review)
    )
    
    return {
        "response" : response
    }
