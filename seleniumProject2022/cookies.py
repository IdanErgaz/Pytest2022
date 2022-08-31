from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

service = Service('C://Drivers/chromedriver.exe')
driver= webdriver.Chrome(service=service)
driver.get('https://www.amazom.in')
driver.maximize_window()


cookies= driver.get_cookies()
print('Number of cookies:{}'.format(len(cookies)))#Capture all the cookies

print(cookies) #Print all the cookies pairs

#Adding a NEW cookie to the browser
cookie= { 'name': 'myCookie', 'value': '1234567890'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print('Number of cookies after adding a cookie:{}'.format(len(cookies)))#Capture all the cookies
print(cookies) #Print all the cookies pairs


#Delete a cookie
driver.delete_cookie('myCookie')
cookies= driver.get_cookies()
print(len(cookies))  #print the number of cookies after deleting

#Delete All COOKIES:
driver.delete_all_cookies()
time.sleep(1)
cookies= driver.get_cookies()
print('The number of cookies after deleting all '+ str(len(cookies)))
driver.quit()