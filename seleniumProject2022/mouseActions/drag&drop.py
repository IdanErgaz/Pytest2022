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

##########################
source =driver.find_element(By.XPATH, '//*[@id="draggable"]/p')
tAR =driver.find_element(By.XPATH, '//*[@id="droppable"]')
actions=ActionChains(driver)
actions.drag_and_drop(source,tAR).perform()
time.sleep(3)
res= driver.find_element(By.XPATH, '//*[@id="droppable"]/p')
assert res.text == 'Dropped!'
print('the drop down action ended successfully!')
driver.quit()
