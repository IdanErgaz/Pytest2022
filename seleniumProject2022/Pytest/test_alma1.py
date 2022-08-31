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


@pytest.fixture()
def setup():
    print('Run before EACH test...')
    service = Service('C://Drivers/chromedriver.exe')
    global driver
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://demo.automationtesting.in/FileDownload.html')
    yield
    print('Run After EACH test!!!')
    driver.quit()


def test_details(setup):
    print('Test 1 is running...')
    more = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[9]/a')
    fileUpload = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[9]/ul/li[4]/a')
    action = ActionChains(driver)
    action.move_to_element(more).click(fileUpload).perform()
    driver.find_element(By.ID, 'input-4').send_keys(
        'C:\\Users\\user\\PycharmProjects\\seleniumProject2022\\Pytest\\pdf.png')
    ele = driver.find_element(By.XPATH, '//*[@id="input-4"]')
    time.sleep(5)


# def test_downloadPdf(setup):
#     print('test 2 is running ...')
#     driver.find_element(By.ID, 'pdfbox').send_keys('Idan')
#     wait = WebDriverWait(driver, 5)
#     ele = driver.find_element(By.ID, 'createPdf')
#     wait.until(EC.element_to_be_clickable(ele))
#     ele.click()
#
def test_drag(setup):
    print('drag and drop test')
    driver.get('https://testautomationpractice.blogspot.com/')
    # driver.switch_to.frame('formAnchor1434677811')
    source = driver.find_element(By.CSS_SELECTOR, 'div.ui-widget-content[id="draggable"]')
    dest = driver.find_element(By.CSS_SELECTOR, 'div.ui-widget-header[id="droppable"]')
    action = ActionChains(driver)
    action.drag_and_drop(source, dest).perform()
    driver.save_screenshot('./drag.png')


def test_checkbox(setup):
    print('test checkbox...')
    driver.get('https://testautomationpractice.blogspot.com/')
    driver.switch_to.frame('frame-one1434677811')
    ele = driver.find_element(By.XPATH, '/html/body/form/div[2]/div[17]/table/tbody/tr[3]/td/input')
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    driver.execute_script("arguments[0].click();", ele)
    driver.save_screenshot('./checkbox.png')


def test_upload(setup):
    print('test upload...')
    driver.get('https://testautomationpractice.blogspot.com/')
    driver.switch_to.frame('frame-one1434677811')
    driver.find_element(By.CSS_SELECTOR, 'input[name="RESULT_FileUpload-10"]').send_keys(
        'C:\\Users\\user\\PycharmProjects\\seleniumProject2022\\Pytest\\pdf.png')
    time.sleep(5)

@pytest.mark.idan
def test_search(setup):
    print('test search ...')
    driver.get('https://testautomationpractice.blogspot.com/')
    driver.find_element(By.XPATH, '//*[@id="Wikipedia1_wikipedia-search-input"]').send_keys('george michael')
    driver.find_element(By.XPATH, '//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input').click()
    resELE = driver.find_element(By.XPATH, '//*[@id="wikipedia-search-result-link"]')
    wait = WebDriverWait(driver, 6)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="wikipedia-search-result-link"]'), 'George Michael'
        )
    )
