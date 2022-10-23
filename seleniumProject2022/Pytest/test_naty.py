import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service


#########################################
@pytest.fixture
def setup():
    print('before each test...')
    service = Service("C://Drivers/chromedriver.exe")
    global driver
    driver= webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    print("afterEach test!!!")
    driver.quit()

def test1(setup):
    print('Running test number1...')
    driver.get('https://google.com')


def test2(setup):
    print('running test number 2...')
    driver.get("http://walla.co.il")
