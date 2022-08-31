from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options  #for chaniging downloading path)
###########################################
chromOptions=Options()
chromOptions.add_experimental_option("prefs", {
  "download.default_directory": "C:\DownloadFiles007",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
file2Upload= 'C://file2upload/test.txt'
service=Service('C:/Drivers/chromedriver.exe')
driver= webdriver.Chrome(service=service, options=chromOptions)
driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()
#########################################
driver.find_element(By.ID, 'textbox').send_keys('This is my input text 4 testing!')
createTextEle=driver.find_element(By.ID, 'createTxt')
wait= WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(createTextEle))
createTextEle.click()
driver.find_element(By.ID, 'link-to-download').click()
# driver.quit()
###############################################