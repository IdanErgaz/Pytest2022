from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
##############################################################
service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()

#find how many inboxes are presented????
inputBoxes= driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputBoxes))

#provide value to a text bo
box1_displayStatus= driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
box1_enabled_status= driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print('Box1 display status:{}, enabled status:{}'.format(box1_displayStatus, box1_enabled_status))
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Idan')
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys('Er')
driver.find_element(By.ID, 'RESULT_TextField-3').send_keys('0525444181')
driver.find_element(By.ID, 'RESULT_TextField-4').send_keys('Israel')
driver.find_element(By.ID, 'RESULT_TextField-5').send_keys('Rishon')
driver.find_element(By.ID, 'RESULT_TextField-6').send_keys('idan@gmail.com')
time.sleep(4)
driver.quit()