import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
###################################################
# driver =None
from selenium.webdriver.support.select import Select


def setup_module(module):
    service=Service('C:/Drivers/chromedriver.exe')
    global driver
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.maximize_window()
    print('====setup module ===')

def teardown_module(module):
    print('===== Teardown module ======')
    driver.quit()

# def test_countImages():
#     print('starting count images test')
#     driver.get('https://practice.automationtesting.in/')
#     images= driver.find_elements(By.CLASS_NAME, 'woocommerce-LoopProduct-link')
#     print('Thhe number of images is: {}'.format(len(images)))
#
# def test_OpenShopPageAndCountProducts():
#     driver.find_element(By.LINK_TEXT, 'Shop').click()
#     catalogElements= len(driver.find_elements(By.CLASS_NAME, 'size-shop_catalog'))
#     print('The catalog has {} products'.format(catalogElements))
#     assert driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a[1]/span/span').text =='₹250.00'

def test_doubbleClick():
    driver.get('https://testautomationpractice.blogspot.com/')
    time.sleep(2)
    btn = driver.find_element(By.CSS_SELECTOR, 'button[ondblclick="myFunction1()"]')
    action = ActionChains(driver)
    action.double_click(btn).perform()
    res=driver.find_element(By.CSS_SELECTOR, 'input[id="field2"]').get_attribute('value')
    assert res=='Hello World!'
def test_drag():
    source=driver.find_element(By.XPATH, "//div[@id='draggable']")
    dest= driver.find_element(By.XPATH, "//div[@id='droppable']")
    action= ActionChains(driver)
    action.drag_and_drop(source, dest).perform()
def test_ddl():
    drp = Select(driver.find_element(By.ID, 'files'))
    drp.select_by_value('3')#select doc file option from the ddl

def test_checkbox():
    driver._switch_to.frame('frame-one1434677811')
    wednesday=driver.find_element(By.ID, 'RESULT_CheckBox-8_2')
    driver.execute_script("arguments[0].click();", wednesday)
    time.sleep(2)

def test_Alert():
    driver.switch_to.default_content()

    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    assert driver.switch_to.alert.text == 'Press a button!'
    driver.switch_to.alert.accept()
    assert driver.find_element(By.ID,'demo').text == 'You pressed OK!'
    driver.save_screenshot('alerts.png')

