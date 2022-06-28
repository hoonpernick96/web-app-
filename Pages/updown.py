import streamlit as st
import random

def getRandomNum():
    ss = st.session_state
    computer_key = 'Computer Number'
    ss[computer_key] = random.randint(1, 100000)


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
    num1 = body.text_input("숫자를 입력하세요(0 ~ 100000)")
    num1 = num1.strip()
    if num1 != '':
        num1 = int(num1)
    submit_button = body.button("submit", disabled=(num1 == ''))
    if submit_button:
        if num == num1:
            footer.write("축하합니다")
        elif num != num1:
            if num > num1:
                footer.write("Up")
            else:
                footer.write("Down")







if __name__ == "__main__":
    drawUpDownPage()






