import sys
import yfinance as yf
import pandas as pd
import streamlit as st
from pathlib import Path
from datetime import datetime

import streamlit as st

# Make src package discoverable when running via ``streamlit run``
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from fetch_data import fetch_stock_data
from indicators import add_indicators
from signals import generate_signals
from predict import predict_next_close


def main():
    st.title("NSE/BSE Stock Analysis Bot")

    symbol = st.text_input("Ticker (e.g., INFY.NS or 500209.BO)", "INFY.NS")
    start_date = st.date_input("Start date", datetime(2020, 1, 1))
    end_date = st.date_input("End date", datetime.today())

    if st.button("Analyze"):
        with st.spinner("Fetching data..."):
            df = fetch_stock_data(symbol, str(start_date), str(end_date))
            df = add_indicators(df)
            df = generate_signals(df)
            prediction = predict_next_close(df)

        st.subheader(f"Next close prediction: {prediction:.2f}")

        st.line_chart(df[['Close', 'SMA_20', 'EMA_20']])
        st.write(df.tail())


if __name__ == "__main__":
    main()
