import streamlit as st
import joblib
import numpy as np
def run_ml():
    st.subheader('일 평균 승하차 건수 예측하기')
        
    st.text('승차(총합계)를 입력하세요')
    ariding = st.number_input('승차(총합계) 입력', min_value=0)
    
    st.text('하차(총합계)를 입력하세요.')
    aquit = st.number_input('하차(총합계) 입력',  min_value=0)
    
    st.text('승차(카드)를 입력하세요.')
    criding = st.number_input('승차(카드) 입력',  min_value=0)
    
    st.text('하차(카드)를 입력하세요.')
    cquit = st.number_input('하차(카드) 입력',  min_value=0)
    
    st.text('승차(현금)를 입력하세요')
    mriding = st.number_input('승차(현금) 입력',  min_value=0)
    
    st.subheader('버튼을 누르면 예측합니다.')
    
    if st.button('예측하기'):
        
    
        # 2. 예측한다.
        # 2-1. 모델이 있어야 한다.
        regressor = joblib.load('./model/regressor.pkl')
        print(regressor)
        # 2-2. 유저가 입력한 데이터를, 모델에 예측할 수 있도록 가공해야 한다.
        new_data = [ariding, aquit, criding, cquit, mriding]
        print(new_data)
        print(np.array(new_data).reshape(1, -1))
        
        new_data = np.array(new_data).reshape(1, -1)
        
        # 2-3. 모델의 predict 함수로 예측한다.
        y_pred = regressor.predict(new_data)

        print(y_pred)
        
        # 위의 데이터로 예측한 자동차 구매 가능 금액은 6,746달러 입니다.
        # 1. y_pred 에서 숫자만 가져온다.
        y_pred = y_pred[0]
        print(y_pred)
        # 2. 숫자의 소수점 뒤 제거
        y_pred = round(y_pred)
        print(y_pred)
        # 3. 문자열 조합하기
        st.text(f'위의 데이터로 예측한 일 평균 승하차 건수는 {y_pred}  입니다.')
        