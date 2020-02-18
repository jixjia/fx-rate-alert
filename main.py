'''
Author:         Jixin Jia (Gin)
Date:           16-Feb-2020
Version:        1.0

Description:
This program uses BeautifulSoup (no headless browser used) to automatically gather Forex information.
Depending on which site the program runs against it could implicitly violate source provider's T&C.
Use the program at your own discretion.
'''
from bs4 import BeautifulSoup
import requests
import config
import datetime
import logging
from modules import SMSNotification

# Initiate SMS Notification
sms = SMSNotification()

# Runtime parameter
sms_template = '[{}] {} >> Time to {} {} ({})'

# Main program
for currency in config.TO_CURRENCY_LIST:
    
    current_dt = datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    
    # Make GET request to target URL
    r = requests.get(config.BASE_URL.format(config.BASE_CURRENCY, currency))
    soup = BeautifulSoup(r.text, 'html.parser')

    # Extract FX live rate
    fx_pair = config.BASE_CURRENCY + '/' + currency
    fx_rate = round(float(soup.select_one(
        '.ccOutputRslt').text.split(' ')[0]), 5)
    fx_pair_inverse = currency + '/' + config.BASE_CURRENCY
    fx_rate_inverse = round(1 / fx_rate, 4)

    print("{} [{}] {} ({}: {})".format(
        current_dt, fx_pair, fx_rate, fx_pair_inverse, fx_rate_inverse))
    
    logging.info("{} [{}] {} ({}: {})".format(current_dt, fx_pair,
                                                  fx_rate, fx_pair_inverse, fx_rate_inverse))

    for thres in config.ALERT_THRESHOLD:
        if fx_pair == thres['fx_pair'] and fx_rate >= thres['sell-threshold']:
            sms.send(config.TO, sms_template.format(
                fx_pair, fx_rate, 'SELL', config.BASE_CURRENCY, current_dt
            ))
        elif fx_pair == thres['fx_pair'] and fx_rate <= thres['buy-threshold']:
            sms.send(config.TO, sms_template.format(
                fx_pair, fx_rate, 'BUY', config.BASE_CURRENCY, current_dt
            ))
        else:
            pass
