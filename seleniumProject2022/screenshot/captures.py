from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

service = Service('C://Drivers/chromedriver.exe')
driver= webdriver.Chrome(service=service)
driver.get('https://www.amazom.in')
driver.maximize_window()
driver.save_screenshot('C:/screenshots/homepage.png') #save screenshot with ONLY png
driver.get_screenshot_as_file('C:/screenshots/homepage.jpeg') #save the screenshot with every extenstion

driver.quit()