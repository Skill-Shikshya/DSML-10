import re
import time
import joblib
import numpy as np
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

LABELS = {
    0 : "Negative", 1 : "Positive"
}

class SentimentAnalyser:
    def __init__(self, model_path, vector_path):
        self.model_path = model_path
        self.vector_path = vector_path
        
    def text_processor(self, text):
        text = text.lower()
        # Removing HTML Tags
        text = re.sub(r"<.+?>", "", text)
        # Removing URLs
        text = re.sub(r"(https?:\/\/\S+)|(www.\S+)", "", text)
        # Removing Puncuation and Sepcial Chars
        text = re.sub(r"[^\w\d\s]", " ", text)
        # Removing Spaces
        text = text.strip()
        # Removing Stop words
        text = [word for word in text.split() if (word not in ENGLISH_STOP_WORDS) and (len(word) > 1) ]
        text = " ".join(text)
            
        return text

    def read_joblib_file(self, file_path):
        try:
            file = joblib.load(
                filename= file_path
            )
            return file
        except Exception as e:
            print(f"Cannot load your file due to {e} !")
            
    def get_embeddings(self, tokens, model):
        vectors = [
            model[word] for word in tokens if word in model
        ]
        if len(vectors) == 0:
            return np.zeros(model.vector_size)
        
        return np.mean(vectors, axis=0)

    def prediction_pipeline(
        self,
        user_input, 
    ):
        classifier = self.read_joblib_file(self.model_path)
        vectorizer = self.read_joblib_file(self.vector_path)
        
        cleaned_text = self.text_processor(user_input)
        vector = self.get_embeddings(
            cleaned_text.split(" "), vectorizer.wv
        )
        
        label = classifier.predict(vector.reshape(1,-1))
        
        return LABELS.get(label[0])
        

if __name__ == "__main__":
    predictor = SentimentAnalyser(
        model_path = "/home/shailesh/Desktop/education/DSML-10/Day-57/SVM_model.joblib", 
        vector_path = "/home/shailesh/Desktop/education/DSML-10/Day-57/Word2Vec_imdb_250.joblib"
    )
    result = predictor.prediction_pipeline(
        user_input= "<br>Misery and Stand By Me were the best adaptations up until this one, now you can add Shawshank to that list.<br>This is simply one of the best films ever made and I know I am not the first to say that and I certainly won't be the last. The standing on the IMDb is a true barometer of that. #3 as of this date and I'm sure it could be number 1. So I'll just skip all the normal praise of the film because we all know how great it is. But let me perhaps add that what I find so fascinating about Shawshank is that Stephen King wrote it.<br><br>King is one of the best writers in the world. Books like IT and the Castle Rock series are some of the greatest stories ever told. But his best adaptations are always done by the best directors. The Shining was brilliantly interpreted by Kubrick and of course the aforementioned Misery and Stand By Me are both by Rob Reiner. Now Frank Darabont comes onto the scene and makes arguably the best King film ever."
    )
    print(result)