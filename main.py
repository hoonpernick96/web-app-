import streamlit as st
from Pages import fastfood
from Pages import timeshift
from Pages import crimeLocation

choice = st.sidebar.selectbox('Select: ', ['선택하세요', 'fastfood', 'timeshift', '대검찰청_범죄발생지'])

if choice == 'fastfood':
    fastfood.drawFastFoodPage()

elif choice == 'timeshift':
    timeshift.drawTimeShiftPage()

elif choice == '대검찰청_범죄발생지':
    crimeLocation.drawCrimeLocationPage()