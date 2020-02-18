# Monitor Foreign Exchange Rate with Azure Function (Python)

A Python program that automatically collects exchange rate for a list of configurable currency pairs.    
The program uses Twilio API to send SMS if any of the monitor rate exceeds pre-defined threshold (aka. realtime exchange rate alert)  

![Monitor FX Rate](https://jixjiastorage.blob.core.windows.net/blog-resources/python-serverless-function/complete.gif)

This app is part of tutorial demonstrating how to setup (any) Python programs as serverless function using **Azure Function**.    
The  function can be invoked via HTTP webhock or routinely executed using CRON schedule. 

For an easy-to-follow tutorial read my blog post:   
(English) https://jixjia.com/2020/02/18/python-serverless-function      
(中文) Coming soon
