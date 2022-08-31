from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)

driver.get('https://demo.guru99.com/test/radio.html')
option1_ele=driver.find_element(By.ID, 'vfb-7-1')
option2_ele=driver.find_element(By.ID, 'vfb-7-2')
print('the status of option1 is: ' + str(option1_ele.is_displayed()))
assert option1_ele.is_displayed() == True
print('The current  status of option1 is: '+ str(option1_ele.is_selected()))

print('Option1  Displayed ')
assert option1_ele.is_selected() == False
option1_ele.click() #click on option1
print('Clicking on option1 radio button ...')
print('The new status of option1 is: '+ str(option1_ele.is_selected()))
driver.quit()
