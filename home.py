import streamlit as st

def run_home():
    st.subheader('버스 정류장 데이터를 분석하고 예측합니다')
    st.text('데이터는 인천 데이터포털에 있는 incheon_bus_station.csv 파일을 사용합니다.')
    st.text('탐색적 데이터 분석과 정류장별 승객 수를 예측하는 앱입니다.')
    
    url = 'https://cdn.safetimes.co.kr/news/photo/202106/96020_76507_2517.jpg'
    st.image(url, use_column_width= True)