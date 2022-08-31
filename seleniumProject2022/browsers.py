from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
service = Service('c:\\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('http://ynet.co.il')
print('The page title is: '+driver.title)
print(driver.current_url)
driver.quit()