import pandas as pd
import yfinance as yf
import numpy as np

df = yf.download("AAPL",
    start="2010-01-01",
    end="2020-12-31",
    progress=False)
df = df.loc[:, ["Adj Close"]]

df["simple_rtn"] = df["Adj Close"].pct_change()
df["log_rtn"] = np.log(df["Adj Close"]/df["Adj Close"].shift(1))

print(df)

def realized_volatility(x):
    return np.sqrt(np.sum(x**2))

df_rv = (
    df.groupby(pd.Grouper(freq="M"))
    .apply(realized_volatility)
    .rename(columns={"log_rtn": "rv"})
)

df_rv.rv = df_rv["rv"] * np.sqrt(12)

print(df_rv)