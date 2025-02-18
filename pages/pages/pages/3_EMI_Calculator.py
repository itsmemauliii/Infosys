import streamlit as st

st.title("🏠 EMI Calculator")

loan_amount = st.number_input("Loan Amount (₹)", min_value=10000)
interest_rate = st.number_input("Annual Interest Rate (%)", min_value=1.0, max_value=30.0)
loan_term = st.number_input("Loan Term (Years)", min_value=1, max_value=30)

if st.button("Calculate EMI"):
    monthly_rate = interest_rate / 12 / 100
    months = loan_term * 12
    emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    st.success(f"Your EMI: ₹{emi:,.2f} per month")
