from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import pytest, time

#########################################################
#setting pytest setup module
def setup_module():
    print('setup module is running...')
    service=Service('C://Drivers/chromedriver.exe')
    global driver
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
def teardown_module():
    print('teardown module is running...')
    driver.quit()
def test_login():
    print('test login is running...')
    driver.find_element(By.CSS_SELECTOR, 'input[name=username').send_keys('Admin')
    driver.find_element(By.CSS_SELECTOR, 'input[name=password').send_keys('admin123')
    driver.find_element(By.CSS_SELECTOR, 'button.oxd-button').click()
    wait =WebDriverWait(driver, 10)
    textEle=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/p')
    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/p'), 'Time at Work'
        )
    )
    # select from the ddl
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
    time.sleep(5)
    ele=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div[1]')
    ele.click()
    time.sleep(1)
    ele.send_keys('m')
    time.sleep(3)
    # take a screen shoot
    driver.save_screenshot('./AfterLogin.png')
    #Logging Out!
    # driver.find_element(By.CSS_SELECTOR, 'oxd-userdropdown-name').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
    driver.find_element(By.LINK_TEXT, 'Logout').click()

@pytest.mark.skip('Irelevant test so I am skipping it')
def test2():
    print('test 2 is running...')

@pytest.mark.skip('because I said so!')
def test3():
    print('running test 3...')

@pytest.mark.skip('just because')
@pytest.mark.parametrize("username", ["Admin"])
@pytest.mark.parametrize("password", ["admin", "admin123"])
def test_negativeLogin(username, password):
    print('test negative login to console...')
    driver.find_element(By.CSS_SELECTOR, 'input[name=username').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name=password').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name=username').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, 'input[name=password').send_keys(password)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'button.oxd-button').click()
    ele= driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')
    if ele.text == 'Invalid credentials':
        print('Test pass... Login ended successfully')
        assert True
    else:
        print('Test failed! user should NOT be able to login!!!')

def test_doubleClick():
    print('running double click test')
    driver.get('https://testautomationpractice.blogspot.com/%22')
    driver.find_element(By.ID, 'field1').clear()
    driver.find_element(By.ID, 'field1').send_keys('Idan')
    button=driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
    action=ActionChains(driver)
    action.double_click(button).perform()
    field2= driver.find_element(By.ID, 'field2')
    if field2.get_attribute('value')== 'Idan':
        print('test pass...')
        assert True
    else:
        print('Test failed!!!')
        assert False
def test_alert():
    print('test switch to alert..')
    driver.get('https://testautomationpractice.blogspot.com/%22')
    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    if driver.switch_to.alert.text == 'Press a button!':
        print('alert test passed...')
        assert True
        driver.switch_to.alert.accept()
        print('alert was accepted...')
        assert (driver.find_element(By.CSS_SELECTOR, 'p#demo').text) == 'You pressed OK!'
        driver.save_screenshot('./alertAccepted.png')
    else:
        print('alert test failed!!!')
        assert False

    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    driver.switch_to.alert.dismiss()
    assert (driver.find_element(By.CSS_SELECTOR, 'p#demo').text) == 'You pressed Cancel!'
    driver.save_screenshot('./alertDismissed.png')

def test_ddl():
    driver.get('https://testautomationpractice.blogspot.com/%22')
    print('test ddl...')
    ele = driver.find_element(By.ID, 'speed')
    select = Select(ele)
    select.select_by_visible_text('Fast')
    driver.save_screenshot('./ddlFast.png')

def test_hover():
    driver.get('https://testautomationpractice.blogspot.com/%22')
    print('test hover')
    tooltipEle=driver.find_element(By.LINK_TEXT, 'Tooltips')
    driver.execute_script("arguments[0].scrollIntoView();", tooltipEle)
    actions=ActionChains(driver)
    actions.move_to_element(tooltipEle).perform()
    textele= driver.find_element(By.XPATH, '/html/body/div[6]/div')
    # assert (driver.find_element(By.CSS_SELECTOR, 'div#ui-id-18')).text == 'That\'s what this widget is'
    assert textele.text == 'That\'s what this widget is'
    driver.save_screenshot('./testHover.png')

def test_rightClick():
    print('test right click...')
    driver.get('https://demo.guru99.com/test/simple_context_menu.html')
    ele= driver.find_element(By.CSS_SELECTOR, 'span.context-menu-one')
    copyEle= driver.find_element(By.XPATH, '//*[@id="authentication"]/ul/li[3]')
    action= ActionChains(driver)
    action.context_click(ele).click(copyEle).perform()
    # copyEle.click()
    driver.switch_to.alert.text == 'clicked: copy'
    time.sleep(3)
    driver.switch_to.alert.accept()

def test_scroll2element():
    print('test scroll to element...')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    ele=driver.find_element(By.LINK_TEXT, 'Software Testing Tutorials')
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    assert ele.text == 'Software Testing Tutorials'
    time.sleep(2)

def test_checkbox():
    print('test checkbox')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    driver.find_element(By.CSS_SELECTOR, 'label[for=RESULT_CheckBox-8_1]').click()
    time.sleep(2)
    driver.save_screenshot('./checkboxIdan.png')

def test_drag():
    print('test drag and drop...')
    driver.get('https://testautomationpractice.blogspot.com/%22')
    sorceEle=driver.find_element(By.XPATH, '//*[@id="gallery"]/li[1]/img')
    destEle=driver.find_element(By.ID, 'trash')
    action=ActionChains(driver)
    action.drag_and_drop(sorceEle, destEle).perform()
    time.sleep(3)
    driver.save_screenshot('./dragNovember2.png')
