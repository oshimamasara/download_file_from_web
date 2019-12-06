# クリックでダウンロード

from selenium import webdriver
import os
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://pythonchannel.com/media/codecamp/201908-/scrape-test.html"
driver.get(url)
download_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/a")))
print(download_button)
download_button.click()
time.sleep(3)
#driver.close()