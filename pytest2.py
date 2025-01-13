import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

df_columns = []
y_list = []
per_list = ['ytd','1mo','3mo','6mo','1y','2y','5y','10y','max']
df = pd.DataFrame()

st.write("Enter a stock ticker to learn more about a company!")
box = st.text_input('Enter a Stock Ticker Here',key='BX1',value='TSLA')

tab_des, tab_mkt_data, tab_instit = st.tabs(['Company Description','Market Data','Institutional Holdings'])

with tab_des:
    tkr = yf.Ticker(box)
    tkr_dict = tkr.info
    
    name = st.write('Company Name: ',tkr_dict['longName'])
    sector = st.write('Sector: ',tkr_dict['sector'])
    bus_sum = st.write('Business Summary: ',tkr_dict['longBusinessSummary'])
    
with tab_mkt_data:
    dd_box = st.selectbox('Select Period',per_list)
    c1, c2, c3, c4, c5 = st.columns(5)
    cb_close = c1.checkbox('Close',value=True)
    cb_open = c2.checkbox('Open')
    cb_high = c3.checkbox('High')
    cb_low = c4.checkbox('Low')
    cb_volume = c5.checkbox('Volume',value=True)
    
    if cb_close:
        y_list.append('Close')
    
    if cb_open:
        y_list.append('Open')
    
    if cb_high:
        y_list.append('High')    

    if cb_low:
        y_list.append('Low')
    
    df = yf.download(box,period=dd_box)
    #df.reset_index(inplace=True)
    df.columns = ['Close','Open','High','Low','Adjusted','Volume']
    st.write(df)
    st.write(df.columns)
    st.line_chart(data = df,x ='Date',y=y_list)
    
    if cb_volume:
        st.bar_chart(data=df,x='Date',y='Volume')


with tab_instit:
    df_hldr = tkr.institutional_holders
    st.table(df_hldr)
