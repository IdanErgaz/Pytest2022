import pytest, time
import logging
import xdist
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert


##################################################

def setup_module(module):
    print('Starting running the tests ...')
    service = Service('C://Drivers/chromedriver.exe')
    global driver
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()


def teardown_module(module):
    print('Teardown module ....')
    driver.quit()


# def test_login():
#     print('Start Test login ... ')
#     driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#     assert driver.title == 'OrangeHRM'
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR, 'input.oxd-input').clear()
#     driver.find_element(By.CSS_SELECTOR, 'input.oxd-input').send_keys('Admin')
#     driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').clear()
#     driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('admin123')
#     wait = WebDriverWait(driver, 5)
#     wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
#     # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="start"]/button    ')))
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     adminEle = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
#     wait=WebDriverWait(driver, 6)
#     wait.until(
#         EC.text_to_be_present_in_element(
#             (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'), 'Admin'
#         )
#     )
#     adminEle.click()
#
#     driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
#     driver.find_element(By.LINK_TEXT, 'Pay Grades').click()
#     driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/label/span').click()
#     driver.save_screenshot('./grade3.png')

def test_alerts():
    driver.get('https://testautomationpractice.blogspot.com/%22')
    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    time.sleep(2)
    if(driver.switch_to.alert.text=='Press a button!'):
        assert True
    else:
        driver.save_screenshot('./alert.png')
        assert False
    driver.switch_to.alert.accept() #accept the alert
    # assert driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/p').get_attribute('value')== 'You pressed OK!'
# def test_datepicker():
#     print('Test date picker...')
#     driver.find_element(By.CSS_SELECTOR, '#datepicker').send_keys('08/31/2022')
#     driver.save_screenshot('./datepicker1.png')

# def test_ddl():
#     print('TEST DDL ...')
#     ddl=Select(driver.find_element(By.ID, 'files'))
#     ddl.select_by_value("2")#pdf file
#     driver.save_screenshot('./pdf.png')
#     time.sleep(3)
#     ddl.select_by_index("0")#select txt file
#     driver.save_screenshot('./txt.png')
#     ddl.select_by_visible_text('Other file')
#     driver.save_screenshot('./otherFile.png')
@pytest.mark.sanity
def test_table():
    print('test table value')
    assert driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[4]/td[2]').text == 'Animesh'

# def test_doubleClick():
#     print('test double click...')
#     buttonEle=driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
#     action=ActionChains(driver)
#     action.double_click(buttonEle).perform()
#     assert driver.find_element(By.ID, 'field2').get_attribute('value')=='Hello World!'

# def test_hover():
#     print('test hover...')
#     tooltipEle= driver.find_element(By.LINK_TEXT, 'Tooltips')
#     action=ActionChains(driver)
#     action.move_to_element(tooltipEle).perform()
#     # msgEle=driver.find_element(By.XPATH, '/html/body/div[7]/div')
#     # driver.execute_script("arguments[0]", msgEle)
#     assert driver.find_element(By.CLASS_NAME, 'ui-tooltip-content').text=="That's what this widget is"

# def test_slide():
#     print('test slide...')
#     action=ActionChains(driver)
#     slider= driver.find_element(By.ID, 'slider')
#     action.drag_and_drop_by_offset(slider, 100, 0).perform()
#     driver.save_screenshot('./slider.png')

def test_walla():
    driver.get('https://walla.co.il')
