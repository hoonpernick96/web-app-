import streamlit as st
import requests

url = 'https://floating-harbor-78336.herokuapp.com/fastfood'

header = st.container()
body = st.container()

h_input = header.text_input('패스트푸드 찾기:', placeholder='검색 키워드 입력')
search_button = header.button('검색')

if search_button:
    params = {
        'searchKeyword': h_input
    }

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