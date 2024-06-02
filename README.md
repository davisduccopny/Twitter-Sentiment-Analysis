<div style="text-align:center;">
<h2 style="background-color:#ffffff;font-family:candaralight;color:#B0B0B0;font-size:150%;text-align:center;border-radius:10px 10px;">Twitter Sentiment Analysis</ h2>
</div>


#### The "Twitter Sentiment Analysis" project uses data provided by Twitter, using basic machine learning and neural network models to classify the sentiment of tweets. Results are classified into categories as positive, negative or neutral.
#### - The project has been built into a web-app using the Streamlit library:
**See web-app :** [TeamQuocChienDuc](https://twitter-sentiment-analysis-teamdata.streamlit.app/)

**Usage data:** [Twitter Data](https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset?select=Twitter_Data.csv)
#### Data summary: Data is loaded from the Tweepy and PRAW API. The data has been cleaned using re and NLP libraries, with labels from -1 to 1
* [ 0 is label neutral ](#1)
* [ 1 is label positive](#2)
* [ -1 is a negative label](#3)


#### - Model used in the project:
* [Gate Recurrent Unit (GRU) ](#1)
* [Logistic Regression](#2)
* [Random Forest](#3)
* [Stochastic Gradient Descent (SGD)](#3)

#### - Library used in the project:
* [requirements.txt) ](#1)
* [main-classification.ipynb](#2)

   
 **<span style="color:red;"> Hope everyone will review and give their opinion about Notebook.</span>**


   <a id='top'></a>
<div class="list-group" id="list-tab" role="tablist">
<p style="background-color:#3498db; font-family:'Candara Light', sans-serif; color:#ffffff; font-size:175%;border-radius:10px; padding:10px;">The main section</p>


* [first. Data OverView](#1)
    
    - [Import library](#1.1)
    
    - [Load dataset](#1.2)
    
    - [Data Cleaning](#1.3)
        
* [2. Exploratory Data Analysis](#2)      

* [3. Data Preprocessing ](#3)

* [4. Modeling](#4)
    
    - [Gate Recurrent Unit (GRU)](#4.1)
    - [Data Preprocessing For Machine Learning Model](#4.2)
    - [Logistics Regression](#4.3)
    - [Random Forest](#4.4)
    - [Stochastic Gradient Descent (SGD)](#4.5)

* [5. Model Evaluation and Comparison](#5)
  
### Installation APP Guide <a id="6"></a>

To run this project locally, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/davisduccopny/Twitter-Sentiment-Analysis.git
    ```
    Download Random Forest Model from link and move file to Twitter-Sentiment-Analysis/model : [RandomForestModel](https://drive.google.com/file/d/1eu-PX2uWr5hLFXAQ2eJfaI4KHMmFhds1/view?usp=sharing)

2. Navigate to the project directory:
    ```
    cd Twitter-Sentiment-Analysis
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the web app:
    ```
    streamlit run interface.py
    ```

5. Open your web browser and go to `http://localhost:8501` to access the Twitter Sentiment Analysis web app.

---

That's it! You have successfully installed and run the Twitter Sentiment Analysis project locally. Enjoy analyzing sentiments of tweets!
