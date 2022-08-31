import wait as wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service =Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
###############################
usernameElement= driver.find_element(By.ID, 'txtUsername')
passElement= driver.find_element(By.ID, 'txtPassword')

usernameElement.send_keys('Admin')
passElement.send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()

wait =WebDriverWait(driver,10)

element1=wait.until(EC.element_to_be_clickable((By.ID, "menu_admin_viewAdminModule")))
element1.click()
