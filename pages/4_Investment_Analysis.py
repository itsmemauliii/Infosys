import streamlit as st
import yfinance as yf

# Title
st.title("💹 AI Investment Forecasting")

# Input for Stock Ticker
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, RELIANCE.NS)", "AAPL")

# Download stock data
data = yf.download(ticker, period="5y")

# Check if the data is empty
if data.empty:
    st.error("Stock data not found. Please check the ticker symbol.")
else:
    # Display stock price data
    st.subheader("Stock Price Data")
    st.line_chart(data["Close"])

    # Ensure 'Close' column exists
    if "Close" in data.columns:
        # Calculate Moving Averages
        data['MA50'] = data['Close'].rolling(window=50).mean()
        data['MA200'] = data['Close'].rolling(window=200).mean()
        
        # Handle missing values in moving averages (e.g., drop rows with NaNs)
        data = data.dropna(subset=["MA50", "MA200"])

        # Display Moving Average Forecast
        st.subheader("Moving Average Forecast")
        st.line_chart(data[["Close", "MA50", "MA200"]])
    else:
        st.error("The 'Close' column is missing from the data.")
