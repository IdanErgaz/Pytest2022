import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def setup():
    print('Start running a NEW test')
    global driver
    service= Service('C://Drivers/chromedriver.exe')
    driver= webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    print('Finish running the test')
    driver.quit()

def test_login(setup):
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
    assert driver.title == 'OrangeHRM'

def test_openWalla(setup):
    driver.get('http://google.com')
    assert driver.title == 'Google'
# @pytest.fixture()
# def setup():
#     print('======== setup  ==========')
#     global driver
#     service = Service('C://Drivers/chromedriver.exe')
#     driver = webdriver.Chrome(service=service)
#     driver.implicitly_wait(5)
#     driver.get('https://google.com')
#     yield
#     print('===teardown  ==========')
#     time.sleep(2)
#     driver.quit()
#
# def testNavigate(setup):
#     print('testing nav to new website and validate the title')

#