import streamlit as st

st.title('Hello, Streamlit!')
st.write('Welcome to your first Streamlit app.')

# Add a text input widget
name = st.text_input('Enter your name')

# Display a personalized greeting
st.write(f'Hello, {name}!')

# Add a button
if st.button('Click me'):
    st.write('Button clicked!')

# Add a slider
age = st.slider('Select your age', 0, 100, 25)
st.write(f'Your age is {age}')

# Add a checkbox
agree = st.checkbox('I agree')
if agree:
    st.write('You agreed!')

# Add a selectbox
option = st.selectbox('Choose a number', [1, 2, 3, 4, 5])
st.write(f'You selected {option}')
