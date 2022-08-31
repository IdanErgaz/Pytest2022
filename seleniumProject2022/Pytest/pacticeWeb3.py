from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time,pytest
####################################################################
def setup_module(module):
    print('===== Setup Module ========')
    service = Service("C:/Drivers/chromedriver.exe")
    global driver
    driver=webdriver.Chrome(service=service)
    # driver.delete_all_cookies()
    driver.implicitly_wait(5)

def teardown_module(module):
    print('=====Teardown Module ====')
    driver.quit()

def test_nav2Google():
    print('navigate to google test')
    driver.get("http://google.com")
    assert driver.title == "Google"

def test_login():
    print('Starting Test login... ')
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    wait = WebDriverWait(driver,5)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnLogin")))
    driver.find_element(By.ID, 'btnLogin').click()


def test_ddl():
    wait = WebDriverWait(driver,8)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/div/div[1]/h1'), 'Dashboard'))
    driver.find_element(By.ID, 'menu_directory_viewDirectory').click()
    select=Select(driver.find_element(By.CSS_SELECTOR, '#searchDirectory_job_title'))
    select.select_by_visible_text('BTest')
    driver.save_screenshot('BTest.png')
