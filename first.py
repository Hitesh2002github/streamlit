import streamlit as st
import pandas as pd

st.write("Hello, This is my first streamlit app")

df = pd.read_csv("Salary_Data.csv")
st.line_chart(df)
