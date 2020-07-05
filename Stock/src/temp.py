import csv
import pandas as pd
import time

import matplotlib.dates as mdates
import datetime as dt
import yfinance as yf
import datetime

class data_gan:
    def __init__(self):        
        self.dt = datetime.datetime.now()
        self.dt = self.dt.replace(hour=0, minute=0, second=0, microsecond=0)
        self.today = datetime.date(self.dt.year, self.dt.month, self.dt.day)
    
        #define the ticker symbol & start date
        self.tickerSymbol = input("Input Stock Code : \n")
        self.sDay = input("Start Date YYYY-MM-DD : \n")

        #get data on this ticker
        self.tickerData = yf.Ticker(self.tickerSymbol)

        #get the historical prices for this ticker
        self.tickerDf = self.tickerData.history(period='1d', start=self.sDay, end=str(self.today))

        #set colums
        self.fieldnames = self.tickerDf.columns
    
        # write stock data
        with open('./Stock/raw_data/{}.csv'.format(self.tickerSymbol), 'w') as self.csv_file:
            self.csv_writer = csv.DictWriter(self.csv_file, fieldnames=self.fieldnames)
            self.csv_writer.writeheader()

        self.num = 0
        while self.num < len(self.tickerDf) - 1:
            self.Date = str(self.tickerDf.index[self.num])[:10]
            self.Open = self.tickerDf['Open'].values[self.num]
            self.High = self.tickerDf['High'].values[self.num]
            self.Low = self.tickerDf['Low'].values[self.num]
            self.Close = self.tickerDf['Close'].values[self.num]
            self.Volume = self.tickerDf['Volume'].values[self.num]
            self.Dividends = self.tickerDf['Dividends'].values[self.num]
            self.Stock_Splits = self.tickerDf['Stock Splits'].values[self.num]

            # print(date, Close)

            with open('./Stock/raw_data/{}.csv'.format(self.tickerSymbol), 'a') as self.csv_file:
                self.csv_writer = csv.DictWriter(self.csv_file, fieldnames=self.fieldnames)

                self.info = {
                    "Date" : self.Date,
                    "Open" : self.Open,
                    "High" : self.High,
                    "Low" : self.Low,
                    "Close" : self.Close,
                    "Volume" : self.Volume,
                    "Dividends" : self.Dividends,
                    "Stock Split" : self.Stock_Splits
                }

                self.csv_writer.writerow(self.info)
            self.num += 1
            time.sleep(0.5)


