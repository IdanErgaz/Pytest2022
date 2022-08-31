from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import pytest, time
from selenium.webdriver.support.wait import WebDriverWait


###################################
@pytest.fixture()
def setup():
    print('=======setup method =======')
    service = Service('C://Drivers/chromedriver.exe')
    global driver
    driver = webdriver.Chrome(service=service)
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    print('====teardown method ======')
    driver.quit()

@pytest.mark.regression
def testLogin(setup):
    print('start login test')
    driver.find_element(By.CSS_SELECTOR, 'INPUT[name="txtUsername"]').send_keys('Admin')
    driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    driver.find_element(By.ID, 'btnLogin').click()
    wait=WebDriverWait(driver,10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/div/div[1]/h1'),'Dashboard')) #wait for dashboard title to be presented
    adminEle=driver.find_element(By.ID, 'menu_admin_viewAdminModule')
    userMgmtEle=driver.find_element(By.ID, 'menu_admin_UserManagement')
    usersEle=driver.find_element(By.ID, 'menu_admin_viewSystemUsers')
    action=ActionChains(driver)
    action.move_to_element(adminEle).move_to_element(userMgmtEle).click(usersEle).perform()  #navigate to Users section after hover
    driver.find_element(By.ID, 'ohrmList_chkSelectRecord_50').click()
    driver.find_element(By.CLASS_NAME, 'delete').click()
    assert driver.find_element(By.XPATH, '//*[@id="deleteConfModal"]/div[2]').text== 'Delete records?'

@pytest.mark.sanity
def test_alerts(setup):
    print('starting alerts test!')
    driver.get('https://testautomationpractice.blogspot.com/')
    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    assert driver.switch_to.alert.text == 'Press a button!'