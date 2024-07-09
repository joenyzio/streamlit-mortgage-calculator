import streamlit as st

# Set the title of the app
st.title('Mortgage Calculator')

# Input fields for user to enter principal amount, interest rate, and loan term
principal = st.number_input('Principal Amount ($)', value=100000)
interest_rate = st.number_input('Annual Interest Rate (%)', value=5.0)
years = st.number_input('Term (Years)', value=30)

# Calculate monthly interest rate and number of payments (months)
monthly_rate = interest_rate / 100 / 12
months = years * 12

# Calculate monthly payment using the mortgage formula
monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

# Display the calculated monthly payment
st.write(f'Monthly Payment: ${monthly_payment:.2f}')
