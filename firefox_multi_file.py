# multifile downloader

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import requests
import urllib.request

try:
    browser = webdriver.Firefox()
    browser.get("https://pythonchannel.com/media/codecamp/201908-/scrape-test2.html")

    elems = browser.find_elements_by_xpath("//a[@href]")
    print(elems)
    count = 1

    for elem in elems:
        download_url = elem.get_attribute("href")
        print(download_url)
        urllib.request.urlretrieve(download_url, str(count))
        print("ダウンロード　ファイル数: " + str(count) )

        time.sleep(3)
        count = count + 1

except Exception as ex:
    print(ex)
 
#browser.close()
