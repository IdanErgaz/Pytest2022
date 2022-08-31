from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#setting the brouser
service=Service('C:/Drivers/chromedriver.exe')
driver= webdriver.Chrome(service=service)
driver.get('https://testautomationpractice.blogspot.com')
driver.maximize_window()

#################################
button=driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
action =ActionChains(driver)
action.double_click(button).perform()
# assert (driver.find_element(By.ID, 'field2')).text == 'Hello World!'
field2=driver.find_element(By.XPATH, '//*[@id="field2"]')
assert (field2.get_attribute('value')) == 'Hello World!'
driver.quit()
