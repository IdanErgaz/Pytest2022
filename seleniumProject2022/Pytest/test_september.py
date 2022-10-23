from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time, pytest, openpyxl
from selenium.webdriver import ActionChains


##########################################
@pytest.fixture()
def setup():
    print('setup is running....')
    service = Service('C://Drivers/chromedriver.exe')
    global driver
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    # driver.delete_cookie()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    yield
    print('after each test')
    driver.quit()


def test_login(setup):
    print('run Login test...')
    driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys('Admin')
    driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys('admin123')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    driver.save_screenshot('./loginScreenshoot.png')
    time.sleep(5)


def test_DoubleClick(setup):
    print('test rightClick...')
    driver.get('https://testautomationpractice.blogspot.com/%22')
    button = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
    action = ActionChains(driver)
    action.double_click(button).perform()
    driver.save_screenshot('./doubleClick.png')


@pytest.mark.idan
def test_alerts(setup):
    print('test alerts...')
    driver.get('https://testautomationpractice.blogspot.com/%22')
    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    assert driver.switch_to.alert.text == 'Press a button!'
    time.sleep(2)
    driver.switch_to.alert.accept()
    msg = driver.find_element(By.CSS_SELECTOR, '#demo').text
    assert msg == "You pressed OK!"
