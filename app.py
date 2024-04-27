import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('Fulldata.csv')

# Set page title and favicon
st.set_page_config(page_title='Leetcode Code Snippet', page_icon=":computer:")

# Define the title and introduction
st.title('Leetcode Code Snippet Finder')
st.write("Welcome to the Leetcode Code Snippet Finder! Enter the question number below to get the code snippet.")

# Input field for question number
question_number = st.number_input('Enter the question number:', min_value=1, max_value=len(df), value=1, step=1)

# Adjust question number to zero-based indexing
question_index = question_number - 1

# Get the code snippet for the selected question
if st.button('Get Code Snippet'):
    code = df.loc[question_index, 'Answer']
    st.code(code, language='cpp')  # Assuming the code snippets are in C++

# Add a footer with additional information or links
st.markdown("---")
st.markdown("Created with ❤️ by Ayush Katre")
