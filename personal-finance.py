import streamlit as st
st.title('Personal Finance Dashboard')
st.write('Welcome to your personal finance dashboard.')
# Add a text input widget for expense description
expense_desc = st.text_input('Enter expense description')
# Add a number input widget for expense amount
expense_amount = st.number_input('Enter expense amount', min_value=0.0, step=0.01)
# Add a slider for expense category
expense_category = st.selectbox('Select expense category', ['Housing', 'Food', 'Transportation', 'Entertainment', 'Other'])
# Display the entered data
if st.button('Add Expense'):
    st.write(f'Added: {expense_desc} - ${expense_amount} in {expense_category}')
