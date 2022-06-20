import streamlit as st
import pandas as pd
import requests

def drawFastFoodPage():


    url = 'https://floating-harbor-78336.herokuapp.com/fastfood'

    header = st.container()
    body = st.container()
    footer = st.container()

    old_input = ''
    h_input = header.text_input('패스트푸드 찾기:', placeholder='검색 키워드 입력')
    search_button = header.button('검색')

    if search_button or h_input != old_input:
        old_input = h_input
        params = {
            'searchKeyword': h_input
        }
        response = requests.get(url, params = params).json()
        total= response["total"]

        response = requests.get(url, params = params).json()
        body.write(f'총 {response["total"]}개의 패스트푸드점을 찾았습니다.')

        number = 1
        for i in response['list']:
            name = i['name']
            addr = i['addr']

            item_container = body.container()
            c1, c2 = item_container.columns([1, 7])

            c1.write(number)
            c2.write(name)
            c2.write(addr)

            number += 1

        total_pages = int(total / 10) + 1

        current = 1

        pages = footer.columns(7)
        pre_button = pages[0].button('이전', disabled = (current == 1))
        firstPage = (current * 5) - 4
        lastPage = current * 5
        for i in range(firstPage, lastPage + 1):
            pages[i].button(str(i))
        next_button = pages[-1].button('다음', disabled = (current == len(pages) - 1))

