import streamlit as st
import pandas as pd
from os.path import join


def drawTimeShiftPage():
    excel_file = '크웨 펀드레이징 타임 쉬프트.csv'
    path = join('..', 'Resources', excel_file)
    df5 = pd.read_csv(path)
    st.dataframe(df5)