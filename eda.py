import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


def run_eda():
    st.subheader('탐색적 데이터 분석')
    
    st.text('데이터프레임 보기 / 통계치 보기를 할 수 있습니다.')
    
    df = pd.read_csv('./data/incheon_bus_station.csv',encoding='cp949')
    
    print(df)

    radio_menu = ['데이터 프레임', '통계치'] 
        
    choice_radio = st.radio('선택하세요.', radio_menu)
    
    if choice_radio == radio_menu[0] :
        st.dataframe(df)
    elif choice_radio == radio_menu[1] :
        st.dataframe(df.describe())
        
    # 각 컬럼별로 최대/최소 값을 보여주는 화면 개발.
    # 유저가 컬럼을 선택하면, 해당 컬럼의 최대/최소 데이터를 보여주도록 하자.
    
    st.text('컬럼을 선택하면, 각 컬럼별 최대/최소 데이터를 보여드립니다.')
    column_list = ['승차건수(총합계)', '하차건수(총합계)', '승차건수(카드)', '하차건수(카드)','승차건수(현금)','일평균 승하차건수']
    choice_column = st.selectbox('컬럼을 선택하세요', column_list)
    
    st.info(f'선택하신 {choice_column}의 최대 데이터는 다음과 같습니다.')
    st.dataframe(df.loc[df[choice_column] == df[choice_column].max() , ])

    st.info(f'선택하신 {choice_column}의 최소 데이터는 다음과 같습니다.')
    st.dataframe(df.loc[df[choice_column] == df[choice_column].min() , ])
    
    st.subheader('상관관계 분석')
    st.text('컬럼들을 2개 이상 선택하면, 컬럼들의 상관계수를 보여드립니다.')
    
    corr_column_list = ['승차건수(총합계)', '하차건수(총합계)', '승차건수(카드)', '하차건수(카드)','승차건수(현금)','일평균 승하차건수']
    selected_columns = st.multiselect('컬럼을 선택하세요.', corr_column_list)
    
    # 2개 이상 선택했을 때와 그렇지 않을때로 개발
    if len(selected_columns) >= 2 :
        # 1. 페어플롯을 그린다.
        fig1 = sb.pairplot(data= df, vars= selected_columns)
        st.pyplot(fig1)
        
        # 2. 상관계수 보여준다.
        st.dataframe(df[selected_columns].corr())
        
        
    else :
        st.text('컬럼은 2개 이상 선택해야 합니다.')