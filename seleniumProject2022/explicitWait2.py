from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
######################################
service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
wait= WebDriverWait(driver, 10)
###################################
emailElement= driver.find_element(By.ID, 'txtUsername')
emailElement.clear()
emailElement.send_keys('Admin')
#####################################
passElement= driver.find_element(By.ID, 'txtPassword')
passElement.clear()
passElement.send_keys('admin123')
####################################
driver.find_element(By.CLASS_NAME, 'button').click() #click on the login button

#ELEMENT
wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="panel_resizable_1_0"]/legend'), 'Employee Distribution by Subunit'))
driver.find_element(By.LINK_TEXT, 'My Timesheet').click()
driver.quit()