import streamlit as st
import requests
import pandas as pd
import os

def drawCrimeLocationPage():
    current_path = os.path.abspath(os.path.dirname(__file__))
    csv_file = os.path.join(current_path, '..', 'Resources', '대검찰청_범죄발생지_20181231.csv')
    csv_read = pd.read_csv(csv_file, encoding = 'CP949')

    print(csv_read)
    # 위에서 기본 5줄 읽어오기
    # print(csv_read.head())

    # 뒤에서 기본 5줄 읽어오기
    # print(csv_read.tail())

    # 데이터프레임의 자료형, 행 인덱스의 종류와 개수, 열의 갯수와 자료형, 메모리 사용량 등의 정보를 확인 할 수 있음
    # print(csv_read.info())

    # 데이터프레임에 대한 통계정보를 요약해 줌. 열의 데이터 개수, 평균값, 표준편차, 최소값 등등
    # print(csv_read.describe())
    # column 선택하여 읽어오기
    # print(csv_read['서울_종로'])

    # column 삭제
    # csv_read['추가1'] = csv_read['서울_종로']
    # print(csv_read)
    # 뒤에 둘 옵션 꼭 필요함. 기존 데이터 프레임에 변경내용을 반영하기 위해서는 inplace=True 옵션 필요
    # csv_read.drop('추가1', axis = 1, inplace = True)
    # print(csv_read)

    # row 선택, 추가, 변경, 삭제
    # index를 이용하여 row 선책 출력하기
    # row1 = csv_read.iloc[0]
    # print(row1)

    # row 이름을 이용하여 선택 출력하기
    # row1 = csv_read.loc[0] # 지금 갖고 있는 데이터의 row가 숫자로 세팅 되어 있어서 0을 사용하게 되었음.
    # print(row1)
    # print(csv_read)

    # row 추가
    # csv_read.loc['추가1'] = 0
    # print(csv_read)

    # row 삭제
    # csv_read.loc['추가1'] = 0
    # csv_read.drop('추가1', axis = 0, inplace = True)
    # print(csv_read)

    # 각 아이템 선택 변경

    # 선택 - index
    # e1 = csv_read.iloc[0, 1]
    # print(e1)
    # print(csv_read)

    # 멀티 선택 - row, column 이름
    # e1 = csv_read.loc[0:5, '서울_종로':'서울_용산']
    # print(e1)
    # print(csv_read)

    # 아이템 값 변경 - index
    # csv_read.iloc[0, 2] = 'aaaa'
    # print(csv_read)

    # 멀티 아이템 값 변경 - index
    # csv_read.iloc[0:10, 0:2] = 'aaaa'
    # print(csv_read)

    csv_read.set_index('범죄분류', inplace = True)
    st.dataframe(csv_read, 1000, 1000)

    # api = 'https://infuser.odcloud.kr/oas/docs?namespace=15085726/v1'
    # response = requests.get(api).json()
    # st.write(response)

if __name__ == "__main__":
    drawCrimeLocationPage()