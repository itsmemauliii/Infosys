import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf

# App Title
st.title("💰 Financial Empowerment for Women")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Budget Tracker", "SIP Calculator", "EMI Calculator", "Investment Analysis", "Financial Learning Hub"])

# Home Page
if page == "Home":
    st.image("assets/logo.png", use_column_width=True)
    st.header("Empower Yourself Financially! 🚀")
    st.write("This app helps women achieve financial independence through budgeting, investment tracking, and financial education.")

# Budget Tracker
elif page == "Budget Tracker":
    st.header("📊 Budget & Expense Tracker")
    st.write("Record your daily expenses and track your spending.")
    
    if "transactions" not in st.session_state:
        st.session_state["transactions"] = []
    
    with st.form("budget_form"):
        date = st.date_input("Date", datetime.today())
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Shopping", "Other"])
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        submit = st.form_submit_button("Add Transaction")
    
    if submit:
        st.session_state["transactions"].append({"Date": date, "Category": category, "Amount": amount})
    
    if st.session_state["transactions"]:
        df = pd.DataFrame(st.session_state["transactions"])
        st.write(df)

# SIP Calculator
elif page == "SIP Calculator":
    st.header("📈 SIP Calculator")
    
    monthly_investment = st.number_input("Monthly Investment (₹)", min_value=0.0, format="%.2f")
    annual_return = st.number_input("Expected Annual Return (%)", min_value=0.0, max_value=100.0, format="%.2f")
    years = st.number_input("Investment Duration (Years)", min_value=1, format="%d")
    
    if st.button("Calculate SIP"):
        months = years * 12
        r = (annual_return / 100) / 12
        future_value = monthly_investment * (((1 + r) ** months - 1) / r) * (1 + r)
        st.success(f"Estimated Future Value: ₹{future_value:,.2f}")

# EMI Calculator
elif page == "EMI Calculator":
    st.header("🏠 EMI Calculator")
    
    loan_amount = st.number_input("Loan Amount (₹)", min_value=0.0, format="%.2f")
    interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=100.0, format="%.2f")
    tenure = st.number_input("Loan Tenure (Years)", min_value=1, format="%d")
    
    if st.button("Calculate EMI"):
        monthly_rate = (interest_rate / 100) / 12
        months = tenure * 12
        emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        st.success(f"Your Monthly EMI: ₹{emi:,.2f}")

# Investment Analysis
elif page == "Investment Analysis":
    st.header("💹 AI Investment Forecasting")
    
    stock = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, RELIANCE.NS)")
    if st.button("Get Stock Data") and stock:
        data = yf.download(stock, period="6mo")
        st.line_chart(data["Close"])

# Financial Learning Hub
elif page == "Financial Learning Hub":
    st.header("📖 Financial Learning Hub")
    
    st.write("Expand your financial knowledge with these courses:")
    st.markdown("- [Personal Finance Basics - Coursera](https://www.coursera.org/learn/personal-finance)")
    st.markdown("- [Investment Strategies - Udemy](https://www.udemy.com/course/investment-strategies/)")
    st.markdown("- [Budgeting & Saving - Khan Academy](https://www.khanacademy.org/college-careers-more/personal-finance)")
    st.markdown("- [Financial Planning - edX](https://www.edx.org/course/financial-planning)")

st.sidebar.write("💡 Created with ❤️ using Streamlit")
