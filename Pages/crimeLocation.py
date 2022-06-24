import streamlit as st
import requests
import pandas as pd
import os
import matplotlib.pyplot as plt

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

    # csv_read.set_index('범죄분류', inplace = True)
    # st.dataframe(csv_read, 1000, 1000)
    # print(csv_read)

    # api = 'https://infuser.odcloud.kr/oas/docs?namespace=15085726/v1'
    # response = requests.get(api).json()
    # st.write(response)

    sort_list = sorted(csv_read.columns)
    sort_list.remove('범죄분류')
    choice = st.selectbox('Sort ', sort_list)
    # df = pd.DataFrame(csv_read)
    # df = df.sort_values(by=[choice])

    # st.dataframe(df, 1000, 1000)

    header = st.container()
    body = st.container()
    footer = st.container()

    col1, col2 = body.columns([10, 7])
    df = pd.DataFrame(csv_read[['범죄분류', choice]])
    df = df.sort_values(by=['범죄분류'])
    df.reset_index(drop=True, inplace=True)
    col1.dataframe(df, 1000, 7200)
    # print([csv_read['범죄분류'], csv_read[choice]])

    x = df['범죄분류']
    y = df[choice]
    plt.plot()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(
        x,
        y,
    )

    col2.write(fig)






if __name__ == "__main__":
    drawCrimeLocationPage()

import matplotlib.pyplot as plt
# plt.plot([1, 3, 7, 4])
# plt.show()

# plt.plot([1, 3, 7, 4], [1, 4, 9, 16])
# plt.show()

# 스타일 지정하기
# plt.plot([1, 3, 7, 4], [1, 4, 9, 16], 'r*-') # red에 *로 표시, r-, r*, ro
# plt.axis([0, 8, 0, 20]) # x축: 0~8, y축: 0~20
# plt.show()

# 여러 개의 그래프 그리기
# import numpy as np
# t = np.arange(0., 5., 0.2)

#  빨간 대쉬, 파란 사각형, 녹색 삼각형
# plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
# plt.show()

# 레이블 패딩
# plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
# plt.xlabel('X-Axis', labelpad=15)
# plt.ylabel('Y-axis', labelpad=20)
# plt.show()

# front 정하기
# font1 = {'family': 'serif',
#          'color': 'b',
#          'weight': 'bold',
#          'size': 14
#          }
#
# font2 = {'family': 'fantasy',
#          'color': 'deeppink',
#          'weight': 'normal',
#          'size': 'xx-large'
#          }
# plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
# plt.xlabel('X-axis', labelpad=15, fontdict=font1)
# plt.xlabel('Y-axis', labelpad=20, fontdict=font2)
# plt.show()


