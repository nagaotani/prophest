import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from pandas_datareader.yahoo.daily import YahooDailyReader
from datetime import datetime

date_st = datetime(2010, 1, 1)
date_fn = datetime(2021, 4, 1)

df1 = YahooDailyReader('MSFT', date_st, date_fn).read()

print(df1.head())

from prophet import Prophet


data = df1.reset_index().rename(columns={'Date': 'ds', 'Close': 'y'})

print(data.head())

# インスタンス化
model = Prophet()

# 学習
#model.fit(data)