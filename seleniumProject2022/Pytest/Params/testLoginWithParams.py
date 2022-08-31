import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def setup_module(module):
    print('======== setup  ==========')
    global driver
    service = Service('C://Drivers/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get('https://google.com')

def teardown_module(module):
    print('===teardown  ==========')
    time.sleep(2)
    driver.quit()


def testNavigate():
    print('testing nav to new website and validate the title')
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
    assert driver.title == 'OrangeHRM'

@pytest.mark.parametrize("username", ["Admin", "admin2"])
@pytest.mark.parametrize("password", ["admin", "admin123"])
def test_loginParams(username, password):
    print('Test login using user password')
    # driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    # driver.find_element(By.ID, 'txtPassword').send_keys('admin123')

    driver.find_element(By.ID, 'txtUsername').clear()
    driver.find_element(By.ID, 'txtUsername').send_keys(username)
    driver.find_element(By.ID, 'txtPassword').clear()
    driver.find_element(By.ID, 'txtPassword').send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
    

