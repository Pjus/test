import csv
import pandas as pd
import time

import matplotlib.dates as mdates
import datetime as dt

df = pd.read_csv("./AAPL.csv")


fieldnames = ["Date", "Close"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

i = 0
while i < len(df) - 1:
    x_val = df['Date'].values[i]
    
    y_val = df['Close'].values[i]
    print(x_val, y_val)

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "Date" : x_val,
            "Close" : y_val
        }

        csv_writer.writerow(info)
    i += 1
    time.sleep(0.5)
