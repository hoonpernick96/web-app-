import streamlit as st
from Pages import fastfood

choice = st.sidebar.selectbox('Select: ', ['선택하세요', 'fastfood'])

if choice == 'fastfood':
    fastfood.drawFastFoodPage()