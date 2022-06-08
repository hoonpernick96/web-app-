import streamlit as st

st.markdown('# first page')
b = st.button('click')

if b:
    st.markdown('''
    * aaa
    * bbb
    ''')