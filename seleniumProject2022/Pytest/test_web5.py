from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pytest, time
from selenium.webdriver import ActionChains

###############################################
#Running tetst using fixture

@pytest.fixture()
def setup():
    print('Should run before  EACH mthod!')
    service = Service("C://Drivers/chromedriver.exe")
    global driver
    driver = webdriver.Chrome(service=service)
    driver.get('https://testautomationpractice.blogspot.com/%22')
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield
    print("should be running AFTER each method")
    driver.quit()
def  test1(setup):
    print('=====test1 ====')
    COPYtEXTeLE= driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
    action=ActionChains(driver)
    action.double_click(COPYtEXTeLE).perform()
    assert driver.find_element(By.ID, 'field2').get_attribute('value') == 'Hello World!'



def test_test(setup):
    print('=== test2 ddl ====')
    drop= Select(driver.find_element(By.ID, 'speed'))
    drop.select_by_index(1)
    driver.save_screenshot('speed1.png')




