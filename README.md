# Monitor Foreign Exchange Rate with Azure Function (Python)

A Python program that automatically collects exchange rate fors desired currency pairs.    
The program uses Twilio API to send SMS when the monitor rates exceed preset threshold (aka. real-time FX rate alert)  

### Screenshot
<p align="center">
  <img src="https://jixjiastorage.blob.core.windows.net/blog-resources/python-serverless-function/complete.gif" width="900">
</p>

### SMS Notification

<p align="center">
  <img src="https://jixjiastorage.blob.core.windows.net/blog-resources/python-serverless-function/demo.png" width="500">
</p>

This app is also part of tutorial showing how to turn a Python program into serverless function using **Azure Functions**. The function app can be triggered ad-hoc by HTTP request or excuted routinely on a regular schedule using CRON. 

For an easy-to-follow tutorial read my blog post:   
(English) https://jixjia.com/2020/02/18/python-serverless-function      
(中文) Coming soon
