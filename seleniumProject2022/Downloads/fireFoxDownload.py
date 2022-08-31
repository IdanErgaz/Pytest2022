import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options  #for chaniging downloading path)
###########################################
#3 fir fox browser setings
ffOptions=Options()
fp=webdriver.FirefoxOptions()
fp.set_preference("browser.download.folderList", 2) #007
fp.set_preference("browser.download.manager.showWhenStarting", False )
fp.set_preference("browser.download.dir", "C:\DownloadFiles007")
fp.set_preference("pdfjs.disabled", True)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/pdf")
fp.set_preference("browser.helperApps.alwaysAsk.force", False)
fp.set_preference("browser.download.improvements_to_download_panel", True)
# downlaod_path= "C:\DownloadFiles007"
# options =webdriver.FirefoxOptions()
# options.set_preference("browser.download.folderList", '2')
# options.set_preference("browser.download.manager.showWhenStarting", False)
# options.set_preference("browser.download.dir", downlaod_path)
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

file2Upload= 'C://file2upload/test.txt'
service=Service('C:/Drivers/geckodriver.exe')
driver= webdriver.Firefox(service=service, options=fp)
driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()
#########################################
driver.find_element(By.ID, 'textbox').send_keys('This is my input text 4 testing!')
createTextEle=driver.find_element(By.ID, 'createTxt')
wait= WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(createTextEle))
createTextEle.click()
driver.find_element(By.ID, 'link-to-download').click()
time.sleep(2)
driver.quit()
###############################################