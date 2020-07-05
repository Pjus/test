from get_stock_data import data_gan

data_gan = data_gan()
stock_data = data_gan.tickerDf
print(stock_data)

# import pandas as pd

# from Indicator import get_Bolinger_Band
# from Indicator import get_DMI
# from Indicator import get_MACD
# from Indicator import get_RSI

# bolingerband = get_Bolinger_Band.fnBolingerBand
# dmi = get_DMI.cal_dmi
# macd = get_MACD.fnMACD
# rsi = get_RSI.fnRSI

# df = pd.read_csv('H:\\test\\Stock\\raw_data\\AAPL.csv')
# bolingerband(df)
# dmi(df)
# macd(df)
# rsi(df)

# print(df.tail())