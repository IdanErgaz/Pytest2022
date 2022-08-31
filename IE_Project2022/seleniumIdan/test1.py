from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service=Service('c:\\Drivers\chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('http://ynet.co.il')
time.sleep(5)
driver.quit()

