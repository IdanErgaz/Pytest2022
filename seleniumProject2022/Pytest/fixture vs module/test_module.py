import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def setup_module(module):
    service=Service('C:/Drivers/chromedriver.exe')
    global driver
    driver=webdriver.Chrome(service=service)
    print('====setup module =======')
    driver.implicitly_wait(5)
    driver.maximize_window()
def teardown_module(module):
    print('====Teardown module===========')
    driver.quit()

def test_nav2Google():
    print('navigate to google test')
    driver.get("http://google.com")
    assert driver.title == "Google"

def test_ynet():
    driver.get('http://ynet.co.il')
    print('navigate to ynet test')