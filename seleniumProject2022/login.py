from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service =Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)

driver.get('https://opensource-demo.orangehrmlive.com/')
usernameElement= driver.find_element(By.ID, 'txtUsername')
passElement= driver.find_element(By.ID, 'txtPassword')

usernameElement.send_keys('Admin')
passElement.send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()
time.sleep(2)
assert (driver.title =='OrangeHRM')
driver.quit()
