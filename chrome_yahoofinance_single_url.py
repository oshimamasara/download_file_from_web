# download one file

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import urllib.request

try:
    browser = webdriver.Chrome()
    browser.get("https://finance.yahoo.com/quote/4151.T/history?period1=946652400&period2=1575558000&interval=1d&filter=history&frequency=1d")
    download_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a')))
    download_button.click()
    time.sleep(3) 

except Exception as ex:
    print(ex)
 
#browser.close()


