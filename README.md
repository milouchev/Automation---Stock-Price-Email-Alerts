# Project Overview

A simple python program for sending email alerts/notifications for real-time price changes on stocks, indexes, or currency pairs using Yahoo! Finance live data.

The user will input the ticker and alert price of their choice, and then input their sending email address and password, and destination email address for the alerts. The stock price will automatically be refreshed every second and displayed in the console until the alert price has been crossed, at which point the email alert will be sent.

<img width="695" alt="Screenshot 2022-11-17 at 1 38 06 PM" src="https://user-images.githubusercontent.com/98411949/202531347-b309b6cb-493c-405d-b14e-15c3545b5e04.png">

# Requirements & Setup:

<b>Python Packages:</b>
 - yfinance
 - time
 - datetime
 - smtplib
 
<b>Sender Email Requirements:</b>
 - Gmail account
 - App passwords enabled
 
 Once an App password is generated, use it as the email password in the console.
 
<img width="642" alt="Screenshot 2022-11-17 at 1 08 27 PM" src="https://user-images.githubusercontent.com/98411949/202529680-27e8df4a-243d-4234-a282-7993af8b0027.png">
