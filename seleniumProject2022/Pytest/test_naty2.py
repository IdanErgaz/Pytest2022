from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
import time


##################################
def setup_module(module):
    print('will be run once before starting all the tests!')
    service=Service("C://Drivers/chromedriver.exe")
    global driver
    driver= webdriver.Chrome(service=service)
    driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
    driver.maximize_window()
    driver.implicitly_wait(10)

def teardown_module(module):
    print('will be run at the END ONCE!')
    driver.quit()


def test_radio():
    print('test radio buttons...')
    element=driver.find_element(By.XPATH, '//*[@id="RESULT_RadioButton-7_0"]')
    driver.execute_script("arguments[0].click();", element)
    driver.save_screenshot('.radioButton.png')

def test_fillText():
    print('fill in text test 2...')
    driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Idan')
    driver.save_screenshot('./fillTextIdan.png')
