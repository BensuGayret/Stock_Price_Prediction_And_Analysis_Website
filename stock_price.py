#Imports and Data Collection
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from pandas_datareader import data as pdr
from keras.models import load_model
import streamlit as st
import yfinance as yf
yf.pdr_override()
#Visualizations
import plotly.express as px

start_date = '2012-12-12'
end_date = '2022-12-12'

st.title('Stock Trend Prediciton')  

user_input = st.text_input('Enter Stock Ticker EX: TSLA, AAPL, AMZN', 'AAPL')
data = pdr.get_data_yahoo(user_input, start_date, end_date)

#Describing Data
st.subheader('Data from 2012 - 2022')
st.write(data.describe())

 #Visualizations
st.subheader(" Stock Prices of Last 10 Years")
tickers = yf.Ticker(user_input)
aapl_df = tickers.history(period="10y")
fig= plt.figure(figsize=(12,6))
plt.plot(aapl_df.Close, color ='olive')
st.pyplot(fig)

# Largest Investors
investors_df=tickers.institutional_holders # largest investors

#Describing Data
st.subheader('Investors')
st.write(investors_df.head())

st.subheader("Largest Investors")
investors_df = tickers.institutional_holders 
fig= plt.figure(figsize=(12,6))
plt.bar(investors_df["Holder"],investors_df["% Out"], color ='maroon', width = 0.4)
plt.xticks(rotation=70)
plt.xticks(fontsize=12)
st.pyplot(fig)

#Number of shares traded per year
data.reset_index(inplace = True)
dataframe=pd.DataFrame.from_dict(data)
dataframe['Year'] = pd.DatetimeIndex(dataframe['Date']).year


volume_year= dataframe.groupby('Year')["Volume"].sum()
vol= pd.DataFrame.from_dict(volume_year)
vol.reset_index(inplace = True)


st.subheader("Number of Shares Traded Per Year")
fig= plt.figure(figsize=(12,6))
plt.bar(vol["Year"],vol["Volume"], color ='darkkhaki', width = 0.4)
plt.xticks(rotation=70)
plt.xticks(fontsize=12)
st.pyplot(fig)