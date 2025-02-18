import streamlit as st

st.title("📈 SIP Calculator")

investment = st.number_input("Monthly Investment (₹)", min_value=500)
rate = st.number_input("Expected Annual Return (%)", min_value=1.0, max_value=20.0)
time = st.number_input("Investment Duration (Years)", min_value=1, max_value=40)

if st.button("Calculate SIP"):
    n = time * 12
    r = rate / 12 / 100
    sip_future_value = investment * (((1 + r)**n - 1) / r) * (1 + r)
    st.success(f"Estimated Maturity Amount: ₹{sip_future_value:,.2f}")
