import streamlit as st
import requests

def drawCrimeLocationShiftPage():
    api = 'https://infuser.odcloud.kr/oas/docs?namespace=15085726/v1'
    response = requests.get(api).json()
    st.write(response)