import streamlit as st
import random


def food3():
  st.title("BMI에 따른 음식 및 운동 추천 웹")
  hi = st.number_input("키를 입력해주세요 (cm): ",value=0)
  we = st.number_input("몸무게를 입력해주세요 (kg): ",value=0)
 

  bmi = we / (hi / 100 * hi / 100)
  st.write(f"BMI: {bmi:.2f}")
  #if hi>0 and we>0:
  if bmi > 25:
    st.write("비만입니다.")
  elif bmi >= 23:
    st.write("과체중입니다.")
  elif bmi >= 18.5:
    st.write("정상체중입니다.")
  else:
    st.write("저체중입니다.")

  return bmi
    
def choice(bmi):
 

  diet = ["닭가슴살", "계란", "견과류", "우유", "채소"]
  normal = ["오트밀", "요구르트", "과일", "고기", "구운연어"]
  obese = ["샌드위치", "우유", "과일", "견과류", "채소"]

  if bmi > 25:
      
      st.write(f"당신의 추천 메뉴는:{random.choice(obese)}입니다.")
      
  elif bmi >= 23:
      
      st.write(f"당신의 추천 메뉴는 :{random.choice(diet)}입니다.")
     
  else:
      
      st.write(f"당신의 추천 메뉴는:{random.choice(normal)}입니다.")

def suggest_exercise(bmi):

  

  diet1 = ["유산소 운동(달리기, 수영, 자전거 타기)","근력 운동(웨이트 트레이닝, 역기능성 훈련)","스트레칭과 근력 운동 결합"]
  normal1 = ["유산소 운동(걷기, 조깅, 수영)", "요가 또는 필라테스", "근력 운동(체중 당겨올리기, 플랭크)", "체력 향상을 위한 훈련"]
  obese1 = ["유산소 운동(빠른 걷기, 조깅, 수영)","요가 또는 필라테스", "체력 향상을 위한 훈련","근력 운동(운동 공, 덤벨 스쿼트)"]

  if  bmi > 25:

    st.write(f"당신의 추천 운동은:{random.choice(obese1)}입니다.")

  elif bmi >= 23:

    st.write(f"당신의 추천 운동은 :{random.choice(diet1)}입니다.")

  else:

    st.write(f"당신의 추천 운동은:{random.choice(normal1)}입니다.")

def food():
    bmi=food3()
    menu=st.radio("메뉴선택",["음식추천","운동추천"],index=None)
    st.write(menu)
    if menu=="음식추천":
        choice(bmi)
    elif menu=="운동추천":
        suggest_exercise(bmi)
    else:
        st.write("음식및운동추천해주세요.")

if __name__=="__main__":
    food()