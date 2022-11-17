# Email alerts/notifications for real-time price changes on stocks/indexes using Yahoo! Finance live data

import yfinance as yf

# Enter stock ticker... Examples: ^GSPC, ^DJI, AAPL, TSLA, MC.PA, SHEL.L, RY.TO
while True:  
    ticker = input("Enter the stock ticker: ")
    try:
        company_name = yf.Ticker(ticker).info["longName"]
        break
    except KeyError:
        pass
    try:
        company_name = yf.Ticker(ticker).info["shortName"]
        break
    except KeyError:
        print("\nIncorrect ticker entered. Please enter the ticker as it appears in Yahoo! Finance.\n"+\
              "Examples: ^GSPC, ^DJI, AAPL, TSLA, MC.PA, SHEL.L, RY.TO\n")
        pass

# Getting stock info
stock_info = yf.Ticker(ticker).info
market_price = stock_info['regularMarketPrice']
previous_close_price = stock_info['regularMarketPreviousClose']
print("\nThe current price of " + ticker.upper() + " is " + str(market_price))
alert_price = float(input("Enter your alert price: "))

# Checking if alert is for a price increase or decrease
if alert_price > market_price:
    change = 1
elif alert_price < market_price:
    change = 0

import datetime as dt
import time
from email.message import EmailMessage

# Setting up email alerts... Make sure to have App passwords enabled on the sending Gmail address
email_address = input("\nEnter you Gmail address: ")
email_password = input("Enter your Gmail password: ")
msg = EmailMessage()
msg['Subject'] = "Automatic Stock Alert for " + company_name + " (" + ticker.upper() + ")"
msg['From'] = email_address
msg['To'] = input("Enter the destination email address: ")

import smtplib

# Setting up email alert content and conditions - price increase
alerted = False
while True and change == 1:
    stock_info = yf.Ticker(ticker).info
    market_price = stock_info['regularMarketPrice']
    now = dt.datetime.now()
    condition = market_price >= alert_price
    print(str(now) + "     " + ticker.upper() + " price: " + str(market_price), flush=True)
    time.sleep(1)
    if(condition == True and alerted == False):
        alerted = True
        message = company_name + " (" + ticker.upper() + ")" + " has crossed the alert price of " + str(alert_price) + "."+\
          "\nCurrent Price: " + str(market_price) + "\nPrevious Close: " + str(previous_close_price) +\
          "\n\nTriggered on " + str(now) + "\nSource: Yahoo! Finance"
        msg.set_content(message)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            print("\nEmail alert/notification sent for threshold price of " + str(alert_price) +".")
        break

# Setting up email alert content and conditions - price decrease 
while True and change == 0:
    stock_info = yf.Ticker(ticker).info
    market_price = stock_info['regularMarketPrice']
    now = dt.datetime.now()
    condition = market_price <= alert_price
    print(str(now) + "     " + ticker.upper() + " price: " + str(market_price), flush=True)
    time.sleep(1)
    if(condition == True and alerted == False):
        alerted = True
        message = company_name + " (" + ticker.upper() + ")" + " has crossed the alert price of " + str(alert_price) + "."+\
          "\nCurrent Price: " + str(market_price) + "\nPrevious Close: " + str(previous_close_price) +\
          "\n\nTriggered on " + str(now) + "\nSource: Yahoo! Finance"
        msg.set_content(message)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
            print("\nEmail alert/notification sent for threshold price of " + str(alert_price) +".")
        break
