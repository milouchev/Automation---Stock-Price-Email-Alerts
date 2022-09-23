#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:29:32 2022

@author: milouchev
"""

import smtplib
import yfinance as yf
import datetime as dt
import time
from email.message import EmailMessage

stock_info = yf.Ticker('AAPL').info
stock = 'Apple Inc.'
ticker = 'AAPL'
TargetPrice = 150
market_price = stock_info['regularMarketPrice']
previous_close_price = stock_info['regularMarketPreviousClose']
now = dt.datetime.now()

# Make sure to have App passwords enabled on your Gmail address
EMAIL_ADDRESS = input("Enter you Gmail address: ")
EMAIL_PASSWORD = input("Enter your Gmail password: ")
msg = EmailMessage()
msg['Subject'] = "Automatic Stock Alert for " + stock + " (" + ticker + ")"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'insert-destination-email-address-here@gmail.com'

alerted = False

while 1:
    stock_info = yf.Ticker('AAPL').info
    market_price = stock_info['regularMarketPrice']
    now = dt.datetime.now()
    condition = market_price >= TargetPrice
    if(condition == True and alerted == False):
        alerted = True
        message = stock + " (" + ticker + ")" + " has crossed the alert price of " + str(TargetPrice) + "."+\
          "\nCurrent Price: " + str(market_price) + "." + "\nPrevious Close: " + str(previous_close_price) + "."+\
          "\n\nTriggered on " + str(now) + "\nSource: Yahoo! Finance"
        msg.set_content(message)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email alert notification sent for threshold price of " + str(TargetPrice) +".")
    print(str(now) + "     " + ticker + " price: " + str(market_price), flush=True)
    time.sleep(1)
    