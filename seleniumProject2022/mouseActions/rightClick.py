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
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()

#################################
button=driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/p/span')
edit=driver.find_element(By.XPATH, '/html/body/ul/li[1]/span')
actions=ActionChains(driver)
actions.context_click(button).click(edit).perform()
assert driver._switch_to.alert.text == 'clicked: edit'
time.sleep(2)
driver.switch_to.alert.accept()
print('Finish RightClick, validate ert text cept the message')
driver.quit()