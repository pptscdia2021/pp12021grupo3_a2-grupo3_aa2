# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OIcGgeRuzzS8-JpWpNpYWj5IeSKQx1se
"""

pip install yfinance

pip install investpy

pip install yahoofinancials

import investpy
import pandas as pd

#Obtener la tabla en tiempo real de la bolsa de españa

data = investpy.get_stock_historical_data(stock='bbva', country='spain', from_date='01/01/2018', to_date='01/01/2021')
data.to_csv('investipy.csv')
print ( data . head ())