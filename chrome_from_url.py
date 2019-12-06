# URL でダウンロード

from selenium import webdriver
import os
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib.request

driver = webdriver.Chrome()
url = "https://pythonchannel.com/media/codecamp/201908-/scrape-test.html"
driver.get(url)
file_url = driver.find_element_by_tag_name("a").get_attribute("href")
urllib.request.urlretrieve(file_url, "□my_download.csv")

time.sleep(3)
#driver.close()