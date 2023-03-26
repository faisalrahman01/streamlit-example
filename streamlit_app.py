import streamlit as st
import pandas as pd
import requests

# Define the API endpoints for Binance
BNB_URL = "https://api.binance.com/api/v3/klines?symbol=BNBUSDT&interval=15m&limit=50"
BTC_URL = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=50"

# Fetch data from the API
def get_data(url):
    data = requests.get(url).json()
    df = pd.DataFrame(data)
    df.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume',
                  'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
    return df

# Get Binance data
bnb_df = get_data(BNB_URL)
btc_df = get_data(BTC_URL)

# Plot the data
st.line_chart(bnb_df[['open_time', 'close']].set_index('open_time'))
st.line_chart(btc_df[['open_time', 'close']].set_index('open_time'))
