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

genderMaleStatus= driver.find_element(By.ID, 'RESULT_RadioButton-7_0').is_selected()
print('Male status iselected is: {}'.format(genderMaleStatus))
time.sleep(1)
male=driver.find_element(By.ID, 'RESULT_RadioButton-7_0')
driver.execute_script("arguments[0].click();", male)




genderMaleStatus= driver.find_element(By.ID, 'RESULT_RadioButton-7_0').is_selected()
print('Male NEW status is: {}'.format(genderMaleStatus))
sunday=driver.find_element(By.ID, 'RESULT_CheckBox-8_0')
Saturday=driver.find_element(By.ID, 'RESULT_CheckBox-8_6')
driver.execute_script("arguments[0].click();", sunday)
driver.execute_script("arguments[0].click();", Saturday)
print('sunday is selected:{}'.format(sunday.is_selected()))
print('Saturday is selected:{}'.format(Saturday.is_selected()))
time.sleep(1)
driver.quit()