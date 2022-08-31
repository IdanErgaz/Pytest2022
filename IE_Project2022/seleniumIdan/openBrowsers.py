from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
#initiate chrome driver
service = Service('c:\\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('http://google.co.il') #navigate to wall website
time.sleep(2) #sleep 3 seconds
driver.quit()  #closing the browser
#
#initiate firefox  driver
service_ff=Service('c:\\Drivers\geckodriver.exe')
driver_ff = webdriver.Firefox(service=service_ff)
driver_ff.get('http://selenium.dev/')
driver.quit()
