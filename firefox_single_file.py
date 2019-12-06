# download one file

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

download_folder = "/home/oshimamasara/★dev/3/file"

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2) 
profile.set_preference("browser.download.dir", download_folder)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
profile.set_preference("browser.download.manager.closeWhenDone", False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-msdownload,application/octet-stream")
try:
    browser = webdriver.Firefox(profile)
    browser.get("https://pythonchannel.com/media/codecamp/201908-/scrape-test.html")
    download_button = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/a")))
    print(download_button)
    #download_button = browser.find_element_by_tag_name("a")
    #print(download_button)
    download_button.click()
    time.sleep(3) 
    print (os.listdir(download_folder))
except Exception as ex:
    print(ex)
 
#browser.close()
