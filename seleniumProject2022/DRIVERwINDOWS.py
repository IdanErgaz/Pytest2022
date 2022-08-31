from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('http://demo.automationtesting.in/Windows.html')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()
print('currentWindow:{}'.format(driver.current_window_handle))
print(driver.window_handles)
handles=driver.window_handles
for h in handles:
    driver.switch_to.window(h)
    print(driver.title)
    if driver.title == 'Frames & windows': #clossing the parent window
        driver.close()
time.sleep(2)
driver.quit()
# driver.current_window_handle
# driver.window_handles
