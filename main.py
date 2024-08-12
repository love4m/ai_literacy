import streamlit as st
import electric_car as ec
import pybasic as pb
import food3_1 as fo


#로그인 화면
st.sidebar.title("로그인")
user_id = st.sidebar.text_input("아이디(ID)입력",value="",max_chars=10)
user_pw = st.sidebar.text_input("패스워드 입력",value="",type='password')


if user_id == "abc" and user_pw == "1234":
    st.sidebar.title("★ 승신 포트폴리오 ★")
    #st.image('mo_p.jpg')


    menu = st.sidebar.radio('메뉴선택',['자기소개','파이썬 기초','탐색적 분석 : 전기자동차','머신러닝','파이썬 기초 미니프로젝트'],index=None)
    st.sidebar.write(menu)


    if menu == '탐색적 분석 : 전기자동차':
        ec.elec_exe()
    elif menu == '머신러닝':
        st.header('공사중')
    elif menu == '파이썬 기초':
        pb.basic()
    elif menu == '파이썬 기초 미니프로젝트':
        fo.food()
    elif menu == '자기소개':
        st.header("자기소개")

