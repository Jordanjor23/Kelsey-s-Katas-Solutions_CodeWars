import streamlit as st

#Title
st.title("My first streamlit app")

#Write text
st.write("Welcome to my first streamlit app")

#Add a slider
number = st.slider("Pick a number", 1, 10)

#Display the result
st.write(f"You selected: {number}")



