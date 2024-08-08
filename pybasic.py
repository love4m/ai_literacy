import streamlit as st
import random

def gugudan():
    dan = st.number_input("단입력>>",value=1)

    if dan>1:
        for i in range(1,10):
        #gop5=a*i
            st.write(f"{dan}*{i}={dan*i}")


def recommand_food():
#음식추천프로그램

    c_food=['짜장면','짬뽕','팔보채']
    k_food=['갈비탕','육개장','된장찌개','비빔밥','김치찌개']

    menu=st.radio("음식추천",["중식","한식"],index=None)
    if menu=="중식":
        st.write(f"오늘의 중식 추천 메뉴: {random.choice(c_food)}")
    elif menu=="한식":
        st.write(f"오늘의 한식 추천 메뉴: {random.choice(k_food)}")
    else:
        st.write("음식종류를 선택하세요")



def basic():
    tab1, tab2 = st.tabs(["구구단", "음식추천"])

    with tab1:
        gugudan()
    with tab2:
        recommand_food()