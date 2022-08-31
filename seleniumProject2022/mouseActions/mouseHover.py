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
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
####################################
##login to##
driver.find_element(By.ID, 'txtUsername').clear()
driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
driver.find_element(By.ID, 'txtPassword').clear()
driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()
#####################################

adminEle= driver.find_element(By.ID, 'menu_admin_viewAdminModule')
adminUserMgmtElement= driver.find_element(By.ID, 'menu_admin_UserManagement')
sysUsersEle=driver.find_element(By.ID, 'menu_admin_viewSystemUsers')
actions=ActionChains(driver)
actions.move_to_element(adminEle).move_to_element(adminUserMgmtElement).move_to_element(sysUsersEle).click().perform()
time.sleep(2)
driver.quit()