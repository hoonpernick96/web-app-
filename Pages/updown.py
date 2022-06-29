import streamlit as st
import random
import os
from PIL import Image

def getRandomNum():
    ss = st.session_state
    computer_key = 'Computer Number'
    ss[computer_key] = random.randint(1, 10)

def disabledOrNot():
    ss = st.session_state
    computer_key = 'Computer Number'
    if computer_key not in ss:
        return True
    return False

def getImage(image1):
    current_path = os.path.abspath(os.path.dirname(__file__))
    image_file = os.path.join(current_path, '..', 'Resources', image1)
    return image_file

def drawUpDownPage():
    ss = st.session_state

    container1 = st.container()
    header = container1.container()
    header.title('위아래게임')
    start_button = header.button("start")

    num = 0
    if "Computer Number" in ss:
        num = ss["Computer Number"]
    if start_button:
        getRandomNum()
    body = container1.container()
    footer = container1.container()
    num1 = body.text_input("숫자를 입력하세요(1 ~ 100000)", disabled = disabledOrNot())
    num1 = num1.strip()
    if num1 != '':
        num1 = int(num1)
    submit_button = body.button("submit", disabled=(num1 == ''))
    if submit_button:
        if num == num1:
            image1 = Image.open(getImage("correct.jpg"))
            footer.image(image1, caption='정답입니다!!!!!!')

        elif num != num1:
            if num > num1:
                image1 = Image.open(getImage("UP.jpg"))
                footer.image(image1, caption = 'Up')
            else:
                image1 = Image.open(getImage("DOWN.png"))
                footer.image(image1, caption='Down')








if __name__ == "__main__":
    drawUpDownPage()






