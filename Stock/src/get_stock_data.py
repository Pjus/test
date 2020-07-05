import csv
import pandas as pd
import time

import matplotlib.dates as mdates
import datetime as dt
import yfinance as yf
import datetime

# set today
dt = datetime.datetime.now()
dt = dt.replace(hour=0, minute=0, second=0, microsecond=0) 
today = datetime.date(dt.year, dt.month, dt.day)

#define the ticker symbol
tickerSymbol = input("Input Stock Code : \n")
sDay = input("Start Date YYYY-MM-DD : \n")

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=sDay, end=str(today))

#see your data
print(tickerDf.tail())

#set colums
fieldnames = tickerDf.columns

# write stock data
with open('H:\\test\\Stock\\raw_data\\{}.csv'.format(tickerSymbol), 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


i = 0
while i < len(tickerDf) - 1:
    Date = str(tickerDf.index[i])[:10]
    Open = tickerDf['Open'].values[i]
    High = tickerDf['High'].values[i]
    Low = tickerDf['Low'].values[i]
    Close = tickerDf['Close'].values[i]
    Volume = tickerDf['Volume'].values[i]
    Dividends = tickerDf['Dividends'].values[i]
    Stock_Splits = tickerDf['Stock Splits'].values[i]

    # print(date, Close)

    with open('H:\\test\\Stock\\raw_data\\{}.csv'.format(tickerSymbol), 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "Date" : Date,
            "Open" : Open,
            "High" : High,
            "Low" : Low,
            "Close" : Close,
            "Volume" : Volume,
            "Dividends" : Dividends,
            "Stock Split" = Stock_Splits
        }

        csv_writer.writerow(info)
    i += 1
    time.sleep(0.5)
