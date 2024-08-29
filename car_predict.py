import pandas as pd
#데이타 스케일링
from sklearn.preprocessing import MinMaxScaler
# 데이타 7:3으로 나누기 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import csv
import streamlit as st

def indata():
    fields = ['id','model','year','transmission','mileage','fuelType','tax','mpg','engineSize']
    data = {}

    #데이타 입력
    for i in fields:
        #value=input(f'{i}:')
        value=st.text_input(f'{i}:')
        data[i] = value

    filename = 'used_car_x_test1.csv'
    #저장시 W 읽어오면 r
    with open(filename,'w',newline='') as f:
        w = csv.DictWriter(f,fieldnames=fields)
        w.writeheader()    #열 제목을 파일에 작성
        w.writerow(data)    #사용자 입력 데이터를 파일에 작성

    return filename

def model(filename):
    #데이타 불러오기 
    df_X_train = pd.read_csv('aidata/used_car_x_train.csv')
    #df_X_test = pd.read_csv('data/used_car_x_test.csv')
    df_X_test = pd.read_csv(filename)
    df_y_train=pd.read_csv('aidata/used_car_y_train.csv')


    #전처리 ===============================================================
    # 범주형, 숫자형 데이타로 분리
    # 범주형데이타
    df_X_train['model'] = df_X_train['model'].str.replace(' ','') #공백 없애기 
    X_train_word = df_X_train[['model','transmission','fuelType']]
    X_test_word = df_X_test[['model','transmission','fuelType']]

    #수치데이타(drop으로 삭제)
    X_train_num = df_X_train.drop(['id','model','transmission','fuelType'],axis=1)
    X_test_num = df_X_test.drop(['id','model','transmission','fuelType'],axis=1)


    #개체생성->데이타 스케일링 =================================
    scaler = MinMaxScaler()

    #학습(test데이타는 적용(transform)만 가능)-->수치형데이타 
    X_train_num_scale = scaler.fit_transform(X_train_num)
    X_test_num_scale = scaler.transform(X_test_num)

    #데이타 프레임 설정
    df_train_num = pd.DataFrame(X_train_num_scale,columns=X_train_num.columns)
    df_test_num = pd.DataFrame(X_test_num_scale,columns=X_test_num.columns)

    #원핫인코딩 : 주의점 --> 범주형 데이타 판다스에 갯더미즈로 만듦
    df_train_word =  pd.get_dummies(X_train_word)
    df_test_word = pd.get_dummies(X_test_word)

    #원핫인코딩 후에 훈련데이터랑 테스트 데이터 열칼럼 체크 꼭! 열을 똑같이 만들어야 함 
    # 훈련데이타 목록
    train_cols = set(df_train_word.columns) #집합,{},키값이 없는 딕셔너리,합집합/교집합

    #테스트 데이타 목록
    test_cols = set(df_test_word.columns)

    missing_test = train_cols-test_cols
    missing_train = test_cols-train_cols

    # df_test_word('model_ S8') = 0
    # df_test_word('model_ S5') = 0

    if len(missing_test)>0:
        for i in missing_test:
            df_test_word[i] = 0

    if len(missing_train)>0:
        for i in missing_train:
            df_test_word[i] = 0


    # 데이타 통일시키 트레인과 테스트를(수치형+범주형)  합치기 
    df_train=pd.concat([df_train_num,df_train_word],axis=1)
    df_test=pd.concat([df_test_num,df_test_word],axis=1)  

    #모델링 ===============================================
    #머신러닝 지도학습 
    # 독립변수 종속변수 
    X = df_train
    y = df_y_train["price"]



    #2.데이타 7:3으로 나누기 
    X_train, X_val,y_train,y_val = train_test_split(X,y,test_size=0.3,random_state=0)

    #3.회귀예측 모델 생성및 학습,평가
    #모델 개체생성
    Rforest_model = RandomForestRegressor(random_state=0)

    #학습
    Rforest_model.fit(X_train,y_train)
    #평가 - score(=R2)
    st.write('R2 score',Rforest_model.score(X_val,y_val))
    #평가 - RMSE
    x_predit = Rforest_model.predict(X_val)
    st.write('Randomforest:',root_mean_squared_error(y_val,x_predit))

    #활용
    #print(X_train.columns)
    df_test=df_test[['year', 'mileage', 'tax', 'mpg', 'engineSize', 'model_A1', 'model_A2',
        'model_A3', 'model_A4', 'model_A5', 'model_A6', 'model_A7',        
        'model_A8', 'model_Q2', 'model_Q3', 'model_Q5', 'model_Q7',        
        'model_Q8', 'model_R8', 'model_RS3', 'model_RS4', 'model_RS5',     
        'model_RS6', 'model_RS7', 'model_S3', 'model_S4', 'model_S5',      
        'model_S8', 'model_SQ5', 'model_SQ7', 'model_TT',
        'transmission_Automatic', 'transmission_Manual',
        'transmission_Semi-Auto', 'fuelType_Diesel', 'fuelType_Hybrid',
        'fuelType_Petrol']]
    

    y_predict = Rforest_model.predict(df_test)
    st.write(f'예상가격은:{y_predict[0]}입니다')

    #df_result.to_csv('car_predict_result.csv')

def aiml_main():
    filename=indata()
    if st.button('예측'):  #st.button('예측')==True
        model(filename)
    
if __name__=='__main__':
    aiml_main()