import streamlit as st

def run_home():
    st.subheader('버스 정류장 데이터를 분석 및 예측합니다')
    st.text('데이터는 인천 데이터포털에 있는 incheon_bus_station.csv 파일을 사용합니다.')
    st.text('인천광역시의 버스 정류장 승하차 데이터 분석 앱입니다.')
    
    url = 'https://cdn.safetimes.co.kr/news/photo/202106/96020_76507_2517.jpg'
    st.image(url, use_column_width= True)
    
    
    st.text('사진 출처 : https://www.safetimes.co.kr/news/articleView.html?idxno=96020')
    st.text('데이터 출처 : https://data.incheon.go.kr/findData/publicDataDetail?dataId=15048264&srcSe=7661IVAWM27C61E190')