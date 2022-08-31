from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
###########################################
file2Upload= 'C://file2upload/test.txt'
service=Service('C:/Drivers/chromedriver.exe')
driver= webdriver.Chrome(service=service)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
############################################
driver.switch_to.frame('frame-one1434677811')  #switch2frame
driver.find_element(By.ID, 'RESULT_FileUpload-10').send_keys(file2Upload)
print('upload action ended successfully!')