import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
# Simple Stock Price Application:

Shown are the stock **opening price**, **closing price** and **Volume** of Google:

""")

# Define the ticker symbol:It means the companies are mentioned in some short forms:
tickerSysbol = 'GOOGL'
# Get the data on this symbol:
tickerData = yf.Ticker(tickerSysbol)
# Get the historical prices for this ticker:
tickerDF = tickerData.history(
    period="1mo", start='2020-06-30', end='2020-07-30')
st.write("""
### This Shows the **Opening Value**:
""")
st.line_chart(tickerDF.Open)
st.write("""
### This Shows the **Closing Value**:
""")
st.line_chart(tickerDF.Close)
st.write("""
### This Shows the **Volume**:
""")
st.line_chart(tickerDF.Volume)
