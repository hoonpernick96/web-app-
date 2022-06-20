import streamlit as st
from Pages import fastfood
from Pages import timeshift

choice = st.sidebar.selectbox('Select: ', ['선택하세요', 'fastfood', 'timeshift'])

if choice == 'fastfood':
    fastfood.drawFastFoodPage()

elif choice == 'timeshift':
    timeshift.drawTimeShiftPage()