from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
driver.maximize_window()
driver.switch_to.frame('packageListFrame')  #switch to the top left frame
driver.find_element(By.LINK_TEXT, 'org.openqa.selenium.devtools.idealized.browser.model').click()
driver.switch_to.default_content()  #going back to the default content
driver.switch_to.frame('packageFrame')#switch to the bottom left frame
driver.find_element(By.LINK_TEXT, 'BrowserContextID').click()
# driver.execute_script("arguments[0].click();", element)
time.sleep(2)
driver.switch_to.default_content()  #going back to the default content
driver.switch_to.frame('classFrame')#switch to the bottom left frame
driver.find_element(By.CSS_SELECTOR ,'body > header > nav > div.fixedNav > div.topNav > ul > li:nth-child(6) > a').click()