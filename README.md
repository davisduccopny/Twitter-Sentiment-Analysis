<div style="text-align:center;">
<h2 style="background-color:#ffffff;font-family:candaralight;color:#B0B0B0;font-size:150%;text-align:center;border-radius:10px 10px;">Twitter Sentiment Analysis</h2>
</div>


#### Dự án "Twitter Sentiment Analysis" sử dụng dữ liệu cung cấp bởi Twitter, tiến hành dùng các mô hình mạng thần kinh và học máy cơ bản để phân loại cảm xúc của các tweet. Kết quả phân loại theo các mục là tích cực, tiêu cực hoặc trung tính.
#### - Dự án đã xây dựng thành web-app bằng thư viện Streamlit:
**Xem web-app :** [TeamQuocChienDuc](https://twitter-sentiment-analysis-teamdata.streamlit.app/)

**Dữ liệu sử dụng :** [Twitter Data](https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset?select=Twitter_Data.csv)
#### Tóm tắt về dữ liệu: Dữ liệu được load từ API của Tweepy and PRAW. Dữ liệu đã được làm sạch bằng thư viện re và NLP, có label từ -1 đến 1
* [ 0 là label neutral ](#1)
* [ 1 là label positive](#2)
* [ -1 là label negative](#3)


#### - Mô hình sử dụng trong dự án:
* [Gate Recurrent Unit (GRU) ](#1)
* [Logistic Regression](#2)
* [Random Forest](#3)
* [Stochastic Gradient Descent (SGD)](#3)
   
 **<span style="color:red;"> Mong mọi người xem xét và cho ý kiến về Notebook.</span>**


   <a id='top'></a>
<div class="list-group" id="list-tab" role="tablist">
<p style="background-color:#3498db; font-family:'Candara Light', sans-serif; color:#ffffff; font-size:175%;border-radius:10px; padding:10px;">Các mục chính</p>


* [1. Data OverView](#1)
    
    - [Import library](#1.1)
    
    - [Load dataset](#1.2)
    
    - [Data Cleaning](#1.3)
        
* [2. Exploratory Data Analysis](#2)      

* [3. Data Preprocessing ](#3)

* [4. Modeling](#4)
    
    - [Gate Recurrent Unit (GRU)](#4.1)
    - [Data Preprocessing For Machine Learning Model](#4.2)
    - [Logistic Regression](#4.3)
    - [Random Forest](#4.4)
    - [Stochastic Gradient Descent (SGD)](#4.5)

* [5. Model Evaluation and Comparison](#5)

