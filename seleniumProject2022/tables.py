from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://testautomationpractice.blogspot.com')
driver.maximize_window()

#count the row number:

rows= len(driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr'))
columns=len(driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th' ))
print('row length is:{}'.format(rows))
print('HEADER length is:{}'.format(columns))
print(driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]').text)
print(driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]').text)
print("product          "+ "Article    "+"Price    ")
for r in range( 2,rows+1):
    for c in range (1, columns+1):
        value= driver.find_element(By.XPATH, ("//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]")).text
        print(value,end='      ')
    print()
