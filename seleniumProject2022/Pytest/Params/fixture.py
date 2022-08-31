import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
@pytest.fixture()
def setup():
    print('======== setup  ==========')
    global driver
    service = Service('C://Drivers/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get('https://google.com')
    yield
    print('===teardown  ==========')
    time.sleep(2)
    driver.quit()

def testNavigate(setup):
    print('testing nav to new website and validate the title')
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
    assert driver.title == 'OrangeHRM'



def test_loginParams(setup):
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
    print('Test login using user password')
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
    time.sleep(3)
