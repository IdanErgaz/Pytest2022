from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service =Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.implicitly_wait(10)
usernameElement= driver.find_element(By.ID, 'txtUsername')
passElement= driver.find_element(By.ID, 'txtPassword')

usernameElement.send_keys('Admin')
passElement.send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()
time.sleep(2)
assert (driver.title =='OrangeHRM')
driver.quit()