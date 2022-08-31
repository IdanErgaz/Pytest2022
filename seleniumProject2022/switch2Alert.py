from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://testautomationpractice.blogspot.com/%22')
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()  #click on the alert button
time.sleep(2)
driver.switch_to.alert.accept()  #select accept in the alert
# assert 'You pressed OK22!' == driver.find_element(By.XPATH, '//*[@id="demo"]').text
assert driver.find_element(By.XPATH, '//*[@id="demo"]').text == 'You pressed OK!'

driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()  #click on the alert button
time.sleep(2)
driver.switch_to.alert.dismiss()  #select accept in the alert
assert driver.find_element(By.XPATH, '//*[@id="demo"]').text == 'You pressed Cancel!'
time.sleep(2)

driver.quit()