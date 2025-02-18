import streamlit as st
import yfinance as yf

st.title("💹 AI Investment Forecasting")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, RELIANCE.NS)", "AAPL")
data = yf.download(ticker, period="5y")

st.subheader("Stock Price Data")
st.line_chart(data["Close"])

st.subheader("Moving Average Forecast")
data["MA50"] = data["Close"].rolling(50).mean()
data["MA200"] = data["Close"].rolling(200).mean()
st.line_chart(data[["Close", "MA50", "MA200"]])
