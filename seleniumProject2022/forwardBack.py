import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service=Service('c://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)

driver.get('http://newtours.demoaut.com')
print(driver.title)
time.sleep(2)
driver.get('http://ynet.co.il')
print(driver.title)
time.sleep(3)
driver.back()
print(driver.title)

time.sleep(2)
driver.forward()
print(driver.title)
driver.quit()