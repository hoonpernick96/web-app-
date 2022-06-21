import streamlit as st
import pandas as pd
import os

def drawTimeShiftPage():
    current_path = os.path.abspath(os.path.dirname(__file__))
    excel_file = '크웨 펀드레이징 타임 쉬프트.csv'
    excel_path = os.path.join(current_path, '..', 'Resources', excel_file)
    # path = join(join'..', 'Resources', excel_file)
    df5 = pd.read_csv(excel_path)
    st.dataframe(df5)