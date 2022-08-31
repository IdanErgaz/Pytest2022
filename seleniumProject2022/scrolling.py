from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://testautomationpractice.blogspot.com')
driver.maximize_window()

# saturday=driver.find_element(By.ID, 'RESULT_CheckBox-8_6')
# driver.execute_script("window.scrollBy(0,100)", "")  #scroll down 1000 pixels
time.sleep(2)
# scroll down untill element is visible
mrJohn=driver.find_element(By.XPATH, '//*[@id="gallery"]/li[1]/img')
driver.execute_script("arguments[0].scrollIntoView(true);", mrJohn)
time.sleep(2)

#scroll down to the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

driver.quit()