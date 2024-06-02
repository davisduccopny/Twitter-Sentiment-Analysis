from streamlit_option_menu import option_menu
import streamlit as st
import base64
import datetime
import os
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.subplots as sp
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from collections import Counter


st.set_page_config(layout='wide',page_title="Dianosis prediction",page_icon= '🖥️' ,initial_sidebar_state='expanded')
def run():
    st.markdown("<h1 style='text-align: center;'>Diagnosing cancer with the KNN algorithm</h1>", unsafe_allow_html=True)

    st.sidebar.markdown("""
        <div style="display: flex; justify-content: center;margin-bottom:0">
            <img src='https://avatars.githubusercontent.com/u/129922030?v=4' alt='Ten_Hinh_Anh' width='60%' style='border-radius:50%;margin-bottom:12%;'>
        </div>
        """, unsafe_allow_html=True)
    st.sidebar.info('❤🌤️Welcome to project🌤️❤️')
    st.sidebar.markdown("---")
run()
def streamlit_menu():
    # 1. as sidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title="🏚️Main Menu",  # required
            options=["Overview", "Descriptive statistics","Model", "Contact"],  # required
            icons=["house", "book", "envelope","phone"],  # optional
            menu_icon=None,  # optional
            default_index=0,  # optional
        )
    return selected
@st.cache_resource
def upload_data():
    file_path = '../data/data.csv'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_file_path = os.path.join(current_dir, file_path)
    
    if os.path.exists(full_file_path):
        data = pd.read_csv(full_file_path, encoding='utf-8')
        return data
    else:
        st.warning(f"File '{full_file_path}' không tồn tại.")
        return None

data = upload_data()

if data is not None:  # Kiểm tra nếu data không phải là None
    data = data.reset_index(drop=True)
    data.drop(['Unnamed: 32','id'], axis=1, inplace=True) 

def embed_image( file_path,width,height):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_file_path = os.path.join(current_dir, file_path)
    with open(full_file_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    html_code = f"""
    <div style="display: flex; justify-content: center;">
        <img src='data:image/jpeg;base64,{encoded_image}' alt='Ten_Hinh_Anh' width='{width}%' height='{height}' style='border-radius:10%; margin-bottom:5%;'>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
def display_file_content( file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_file_path = os.path.join(current_dir, file_path)

    if os.path.exists(full_file_path):
        with open(full_file_path, "r", encoding="utf-8") as file:
            try:
                lines = file.readlines()
                content = "\n".join(lines).strip()
                return content
            except UnicodeDecodeError:
                st.error(
                    f"Tệp tin '{full_file_path}' không thể đọc với encoding utf-8.")
    else:
        st.error(f"Tệp tin '{full_file_path}' không tồn tại.")
def introduction():
    total_rows = data.shape[0]
    total_columns = data.shape[1]
    dimension_data = data.shape
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(f"**Total Rows:**\n\n{total_rows} rows")
    with col2:
        st.success(f"**Total Columns:**\n\n{total_columns} columns")

    with col3:
        st.warning(f"**Dimension:**\n\n{dimension_data} ")
    st.subheader("Overview")
    st.dataframe(data.head(),width=13*80)
    file_path = "../asset/image/knn_overview.png"
    embed_image(file_path=file_path,width=60,height='auto')
    st.header("Về thuật toán")
    st.info(display_file_content('../info/KNN_kn.txt'))
    col4,col5 = st.columns(2)
    with col4:
        st.subheader("Nguyên lý hoạt động cơ bản")
        st.info(display_file_content('../info/KNN_nlhdcb.txt'))
        
    with col5:
        st.subheader("Bài toán giải quyết")
        st.info(display_file_content('../info/KNN_vdgq.txt'))
    st.subheader("Giải thích nguyên lý")
    st.info(display_file_content('../info/KNN_nlhdct.txt')) 
    embed_image('../asset/image/nguyenlihoatdong_knn.png',width=40,height='auto')   

def main(selected):
    if selected == "Overview":
        st.header("K-Nearest Neighbors")
        introduction()
    if selected == "Descriptive statistics":
        st.header("Thống kê mô tả")
        descriptive = DESCRIPTIVE_STATISTICS(data)
        st.dataframe(descriptive.describe(),width=13*80)
        st.subheader('Histogram')
        st.plotly_chart(descriptive.subplot_histograms())
        st.subheader("Pairplot")
        st.plotly_chart(descriptive.pairplot())
        st.subheader("Heatmap")
        st.plotly_chart(descriptive.heatmap())
    if selected == "Model":
        st.header("Mô hình chẩn đoán ")
        train_model = TRAIN_MODELS(data)
        train_model.run_knn()
    if selected == "Contact":
        st.header("Liên hệ")
        col_info1,col_info2,col_info3 = st.columns(3)
        with col_info1:
            embed_image('../asset/image/quoc_info.jpg',width=100,height=225)
            st.info("🔥**Hoàng Xuân Quốc - 2156210125**🔥💯")
            st.code("email: 2156210125@hcmussh.edu.vn")
        with col_info2:
            embed_image('../asset/image/chien_info.jpg',width=100,height=225)
            st.info("🔥**Đặng Hoàng Chiến - 2156210095**🔥💯")
            st.code("email: 2156210095@hcmussh.edu.vn")
        with col_info3:
            embed_image('../asset/image/duc_info.png',width=100,height=225)
            st.info("🔥**Nguyễn Viết Đức - 2156210100**🔥💯")
            st.code("email: 2156210100@hcmussh.edu.vn")
        st.info("Created and designed by [Team Data Science - QuocChienDuc](https://github.com/davisduccopny/Diagnosing-cancer-with-the-KNN-algorithm)") 
        st.info("Instructors: Nguyễn Tấn Công")
        st.markdown("<h2 style='text-align: center;'>Một chút meme cho đỡ căng thẳng</h2>", unsafe_allow_html=True)
        embed_image('../asset/image/meme_ntcong.jpg',width=50,height='500')
if __name__ == '__main__':
    selected = streamlit_menu()
    main(selected)
st.sidebar.markdown(  """
            ---
            """)
st.sidebar.info(
            "Created and designed by [Team Data Science - QuocChienDuc](https://github.com/davisduccopny/Stock-Prediction-with-Python-project/)")