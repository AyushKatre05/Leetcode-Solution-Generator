import streamlit as st
import pandas as pd

df = pd.read_csv('Fulldata.csv')

st.title('Code Snippet For Leetcode')

num_questions = len(df)

question_number = st.number_input('Enter the question number:', min_value=1, max_value=num_questions, value=1, step=1)

question_number -= 1

if st.button('Get Code Snippet'):
    code = df.loc[question_number, 'Answer']
    st.code(code)
