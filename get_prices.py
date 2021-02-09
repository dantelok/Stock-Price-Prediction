import pandas as pd
import yfinance as yf

def get_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="max").reset_index()
    data.to_csv(ticker + '_full.csv', index=False)

get_price('AMZN')