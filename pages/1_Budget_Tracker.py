import streamlit as st
import pandas as pd
import os

st.title("📊 Budget & Expense Tracker")

# Load existing transactions
file_path = "data/transactions.csv"
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])

# Add new transaction
st.subheader("Add a new transaction")
date = st.date_input("Transaction Date")
category = st.selectbox("Category", ["Food", "Transport", "Rent", "Shopping", "Others"])
amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")

if st.button("Add Transaction"):
    new_data = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_path, index=False)
    st.success("Transaction Added!")

# Show transactions
st.subheader("Expense Summary")
st.dataframe(df)
