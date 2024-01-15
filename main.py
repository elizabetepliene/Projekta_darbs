import pandas as pd
import yfinance as yf
import numpy as np

#getting user input
stock = input("Lūdzu ievadiet vēlamas akcijas tickeri (piem., AAPL): ")
start_date = input("Ievadiet invsetīciju sākuma datumu (formā yyyy-mm-dd): ")
end_date = input("Ievadiet beigu datumu (formā yyyy-mm-dd): ")
freq = input("Ievadiet 1, ja vēlatie iemaksas veikt reizi gadā, 2, ja vēlaties tās veikt reizi mēnesī: ")
cap = input("Ievadiet sākuma kapitāla summu: ")
sum = input("Ievadiet kādu summu vēlaties iemaksāt katrā reizē: ")

# iemaksa reizi mēnesī
df = yf.download(stock,
    start=start_date,
    end=end_date,
    progress=False)
df['Date'] = df.index
df_first_of_month = df.groupby(df['Date'].dt.to_period("M")).first()
df_last_of_month = df.groupby(df['Date'].dt.to_period("M")).last()
print(df_first_of_month['Open'])

portfelis = float(cap)/float(df_first_of_month.iloc[0]['Open'])

for i in range (1, len(df_first_of_month)):
    portfelis=portfelis+float(sum)/df_first_of_month.iloc[i]['Open']
protfela_vertiba=portfelis*float(df_last_of_month.iloc[len(df_last_of_month)-1]['Open'])
pelna=protfela_vertiba-float(cap)-(float(sum)*int(len(df_first_of_month)))
print(portfelis)
print(protfela_vertiba)
print(pelna)