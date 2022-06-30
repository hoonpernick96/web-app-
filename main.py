import streamlit as st
from Pages import fastfood
from Pages import timeshift
from Pages import crimeLocation
from Pages import updown
from Pages import flex

my_list = ['선택하세요',
           'fastfood',
           'timeshift', '대검찰청_범죄발생지', '위아래', '복권행운의번호']

choice = st.sidebar.selectbox('Select: ', my_list)
if choice == 'fastfood':
    fastfood.drawFastFoodPage()

elif choice == 'timeshift':
    timeshift.drawTimeShiftPage()

elif choice == '대검찰청_범죄발생지':
    crimeLocation.drawCrimeLocationPage()

elif choice == "위아래":
    updown.drawUpDownPage()

elif choice == "복권행운의번호":
    flex.drawFlexPage()

