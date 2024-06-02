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
@st.cache_resource()
def download_and_merge_files():
    if not os.path.exists('model/grid_search_rfclass_model_merged.h5'):
        file_parts = [
            'model/grid_search_rfclass_model.h5.part0',
            'model/grid_search_rfclass_model.h5.part1',
            'model/grid_search_rfclass_model.h5.part2',
            'model/grid_search_rfclass_model.h5.part3',
            'model/grid_search_rfclass_model.h5.part4',
        ]

        output_file = 'model/grid_search_rfclass_model_merged.h5'

        with open(output_file, 'wb') as merged_file:
            for part in file_parts:
                with open(part, 'rb') as part_file:
                    merged_file.write(part_file.read())
download_and_merge_files()
# Load model function
@st.cache_resource()
def load_model_check(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model
@st.cache_resource()
def load_model_check_GRU(model_path):
    model = load_model(model_path)
    return model
def load_model_check_RF(model_path):
    model = joblib.load(model_path)
    return model
# Run model 
model_GRU = load_model_check_GRU('model/best_model_GRU.h5')
model_logistic = load_model_check('model/clf_model.h5')
model_random_forest =  load_model_check_RF('model/grid_search_rfclass_model_merged.h5')
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
        # Transforms text to a sequence of integers using a tokenizer object
        xt = self.tokenizer.texts_to_sequences([text])  # Note: pass text as a list
        # Pad sequences to the same length
        xt = pad_sequences(xt, padding='post', maxlen=self.max_len)
        # Do the prediction using the loaded model
        yt = model_GRU.predict(xt).argmax(axis=1)
        # Return the predicted sentiment
        return sentiment_classes[yt[0]]
    def predict_class_mle(self, text, model):
        sentiment_classes = ['Negative', 'Neutral', 'Positive']
        # Biến đổi văn bản thành vector đặc trưng bằng TF-IDF
        features = self.vectorizer.transform([text])
        # Dự đoán nhãn bằng mô hình logistic regression
        predicted_class_index = model.predict(features)
        predicted_class_index = int(predicted_class_index)
        # Chuyển đổi chỉ số lớp dự đoán thành nhãn cảm xúc tương ứng
        predicted_class = sentiment_classes[predicted_class_index]
        # Trả về nhãn dự đoán
        return predicted_class

class MainApp:
    def __init__(self):
        self.sentiment_analysis = SentimentAnalysis()
    # Streamlit app
    def main(self):
        st.title("Sentiment Analysis of Tweets")
        self.model_options = ["Random Forest", "GRU Model", "Multinomial Logistic Regression", 'SGD Classifier']
        self.selected_model = st.selectbox("Select Model:", self.model_options)
        # Input for tweet
        self.tweet_input = st.text_input("Enter Tweet:", "")

        # Predict button
        if st.button("Predict"):
            if self.tweet_input:
                if self.selected_model == "Random Forest":
                    random_forest_title = st.write("Random Forest Model")
                    self.result_check = self.sentiment_analysis.predict_class_mle(self.tweet_input,model_random_forest)
                    st.write(f"The predicted sentiment is: {self.result_check}")
                elif self.selected_model == "GRU Model":
                    GRU_title = st.title("GRU Model")
                    self.result_check = self.sentiment_analysis.predict_class(self.tweet_input)
                    st.write(f"The predicted sentiment is: {self.result_check}")
                elif self.selected_model == "Multinomial Logistic Regression":
                    logistic_title = st.title("Multinomial Logistic Regression")
                    self.result_check = self.sentiment_analysis.predict_class_mle(self.tweet_input,model_logistic)
                    st.write(f"The predicted sentiment is: {self.result_check}")
                elif self.selected_model == "SGD Classifier":
                    SGD_title = st.title("SGD Classifier")
                    self.result_check = self.sentiment_analysis.predict_class_mle(self.tweet_input,model_SGD)
                    st.write(f"The predicted sentiment is: {self.result_check}")
                

if __name__ == "__main__":
    app = MainApp()
    app.main()
st.markdown(  """
            ---
            """)
st.info(
            "Created and designed by [Team Data Science - QuocChienDuc](https://github.com/davisduccopny/Stock-Prediction-with-Python-project/)")