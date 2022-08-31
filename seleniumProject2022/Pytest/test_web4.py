#Running pytest tests using setup and teradown modules which should be running once before and after starting all tetsts/methods

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pytest, time
from selenium.webdriver import ActionChains


######################################################################


def setup_module(module):
    print('=======This is a setup module=======')
    print('starting chrome driver')
    service = Service("C://Drivers/chromedriver.exe")
    global driver
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)


def teardown_module(module):
    print('===Teardown module is running ====')
    print('closing the browser')
    driver.quit()


# def test_login():
#     print('Start logging page test...')
#     driver.get('https://opensource-demo.orangehrmlive.com/')
#     driver.find_element(By.ID, 'txtUsername').clear()
#     driver.find_element(By.ID, 'txtPassword').clear()
#     driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
#     driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
#     wait = WebDriverWait(driver, 6)
#     wait.until(EC.element_to_be_clickable((By.ID, 'btnLogin')))
#     driver.find_element(By.ID, 'btnLogin').click()
#
#
# def test_hover():
#     print('Starting Hover testing...')
#     wait = WebDriverWait(driver, 6)
#     wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/div/div[1]/h1'), 'Dashboard'))
#     adminEle = driver.find_element(By.ID, 'menu_admin_viewAdminModule')
#     userMgmtEle = driver.find_element(By.ID, 'menu_admin_UserManagement')
#     sysUsersEle = driver.find_element(By.ID, 'menu_admin_viewSystemUsers')
#     action = ActionChains(driver)
#     action.move_to_element(adminEle).move_to_element(userMgmtEle).move_to_element(sysUsersEle).click().perform()
#

def test_alerts():
    print('Start alerts testing...')
    driver.get('https://testautomationpractice.blogspot.com/%22')
    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    assert driver.switch_to.alert.text == 'Press a button!'
    driver.switch_to.alert.accept()
    driver.find_element(By.ID, 'demo').text == 'You pressed OK!'
    time.sleep(2)
    driver.save_screenshot('aerts1.png')
