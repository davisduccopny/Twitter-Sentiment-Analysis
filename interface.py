import streamlit as st
import numpy as np
import re
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle
import joblib
import os

st.set_page_config(page_title="Twitter Sentiment Analysis",page_icon= '🤖' ,initial_sidebar_state='expanded')
# Load model function
@st.cache_resource
def load_model_check(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model
@st.cache_resource
def load_model_check_GRU(model_path):
    model = load_model(model_path)
    return model
@st.cache_resource
def load_model_check_RF(model_path):
    model = joblib.load(model_path)
    return model
# Run model 
model_GRU = load_model_check_GRU('model/best_model_GRU.h5')
model_logistic = load_model_check('model/clf_model.h5')
random_file_forest = 'model/grid_search_rfclass_model.pkl'
if os.path.exists(random_file_forest):
    model_random_forest =  load_model_check_RF(random_file_forest)
model_SGD = load_model_check('model/grid_search_sgd_model.h5')
class SentimentAnalysis:
    def __init__(self):
        self.max_len = 50

        with open('model/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        with open('model/vectorizer.pkl', 'rb') as f:
            self.vectorizer = pickle.load(f)

    def predict_class(self, text):
        sentiment_classes = ['Negative', 'Neutral', 'Positive']

        xt = self.tokenizer.texts_to_sequences([text])  
        xt = pad_sequences(xt, padding='post', maxlen=self.max_len)
        yt = model_GRU.predict(xt).argmax(axis=1)
        return sentiment_classes[yt[0]]
    def predict_class_mle(self, text, model):
        sentiment_classes = ['Negative', 'Neutral', 'Positive']
        features = self.vectorizer.transform([text])
        predicted_class_index = model.predict(features)
        predicted_class_index = int(predicted_class_index)
        predicted_class = sentiment_classes[predicted_class_index]
        return predicted_class

class MainApp:
    def __init__(self):
        self.sentiment_analysis = SentimentAnalysis()
    # Streamlit app
    def main(self):
        st.title("Sentiment Analysis of Tweets")
        self.model_options = ["GRU Model", "Multinomial Logistic Regression", "SGD Classifier","Random Forest"]
        self.selected_model = st.selectbox("Select Model:", self.model_options)
        # Input for tweet
        self.tweet_input = st.text_input("Enter Tweet:", "")

        # Predict button
        if st.button("Predict"):
            if self.tweet_input:
                if self.selected_model == "GRU Model":
                    st.markdown(  """
                        ---
                        """)
                    GRU_title = st.header("GRU Model")
                    self.result_check = self.sentiment_analysis.predict_class(self.tweet_input)
                    st.success(f"The predicted sentiment is: {self.result_check}")
                elif self.selected_model == "Multinomial Logistic Regression":
                    st.markdown(  """
                        ---
                        """)
                    logistic_title = st.header("Multinomial Logistic Regression")
                    self.result_check = self.sentiment_analysis.predict_class_mle(self.tweet_input,model_logistic)
                    st.success(f"The predicted sentiment is: {self.result_check}")
                elif self.selected_model == "SGD Classifier":
                    st.markdown(  """
                        ---
                        """)
                    SGD_title = st.header("SGD Classifier")
                    self.result_check = self.sentiment_analysis.predict_class_mle(self.tweet_input,model_SGD)
                    st.success(f"The predicted sentiment is: {self.result_check}")
                elif self.selected_model == "Random Forest":
                    st.markdown(  """
                        ---
                        """)
                    random_forest_title = st.header("Random Forest Model")
                    if os.path.exists(random_file_forest):
                        self.result_check = self.sentiment_analysis.predict_class_mle(self.tweet_input,model_random_forest)
                        st.success(f"The predicted sentiment is: {self.result_check}")
                    else:
                        st.error("Model not found")
if __name__ == "__main__":
    app = MainApp()
    app.main()
st.markdown(  """
            ---
            """)
st.info(
            "Created and designed by [Team Data Science - QuocChienDuc](https://github.com/davisduccopny/Stock-Prediction-with-Python-project/)")