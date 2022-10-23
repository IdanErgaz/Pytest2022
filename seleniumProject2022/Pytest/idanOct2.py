from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pytest, time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
#####################################################
def setup_module(module):
    print("#### Start runing th etest #########################")
    service = Service("C://Drivers/chromedriver.exe")
    global driver
    driver= webdriver.Chrome(service=service)
    driver.get('https://demo.automationtesting.in/Alerts.html')
    driver.maximize_window()
    driver.implicitly_wait(7)
def teardown_module(module):
    print('################# Finish running the tests ##############')
    driver.quit()

@pytest.mark.skip('just skip once.')
def test1():
    print('test1 is running')
    driver.find_element(By.CSS_SELECTOR, '#OKTab.active').click()
    assert driver.switch_to.alert.text == 'I am an alert box!'
    time.sleep(2)
    driver.switch_to.alert.accept()
@pytest.mark.skip('just skip once.')
def test_form():
    driver.get('https://demo.automationtesting.in/Register.html')
    driver.find_element(By.CSS_SELECTOR, 'input[ng-model=FirstName]').send_keys('Idan')
    driver.find_element(By.CSS_SELECTOR, 'input[ng-model=LastName]').send_keys('Ben')
    driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[2]/div/textarea').send_keys('bla bla bla23')
    driver.find_element(By.CSS_SELECTOR, 'input[type=email2]').send_keys('Ben@walla.com')
    driver.find_element(By.CSS_SELECTOR, 'input[ng-model=Phone]').send_keys('0525333181')
    driver.find_element(By.CSS_SELECTOR, 'input[value=Male]').click()
    driver.find_element(By.CSS_SELECTOR, 'input#checkbox3').click()
    # ddl = Select(driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul'))
    # ddl.select_by_visible_text('Bulgarian') #select Bulgarian
    # driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[2]/a').click()
    ddlSkils=Select(driver.find_element(By.ID, 'Skills'))
    ddlSkils.select_by_index('1') #select adobIn design option
    ddlCountries= Select(driver.find_element(By.ID, 'country'))
    ddlCountries.select_by_value("Netherlands")
    time.sleep(5)

@pytest.mark.skip('just skip once.')
def test_ckeditor():
    driver.get('https://demo.automationtesting.in/CKEditor.html')
    driver.switch_to.frame(0)
    driver.find_element(By.CSS_SELECTOR, 'body.cke_editable').send_keys('this is my text')

@pytest.mark.skip('just skip once.')
def test_drag():
    driver.get('https://testautomationpractice.blogspot.com/%22')
    # driver.switch_to.frame('result')
    # dropArea=driver.find_element(By.ID, 'droparea')
    sorceEle=driver.find_element(By.ID,'draggable')
    destEle= driver.find_element(By.CSS_SELECTOR, '#droppable')
    # driver.execute_script("arguments[0].scrollIntoView();", destEle)
    time.sleep(2)
    action=ActionChains(driver)
    action.drag_and_drop(sorceEle,destEle).perform()
    driver.save_screenshot('./drag009.png')

@pytest.mark.skip('just skip once.')
def test_style():
    driver.get('https://testautomationpractice.blogspot.com/%22')
    print('test the text font and style')
    ele=driver.find_element(By.XPATH, '//*[@id="1"]/name')
    print(ele.text)
    print(ele.value_of_css_property('color'))
    if ele.value_of_css_property('color') == 'rgba(255, 0, 0, 1)':
        print('The color test Passed!')
        assert True
    else:
        print('The color is wrong!!! test FAILED!')
        driver.execute_script("arguments[0].scrollIntoView();", ele)
        driver.get_screenshot_as_file('.\\textColor.png')
        assert False
@pytest.mark.skip('just because2')
def test_fileUpload():
    driver.get('https://demo.automationtesting.in/FileUpload.html')
    driver.find_element(By.CSS_SELECTOR, 'input#input-4').send_keys('C:\\Users\\user\\PycharmProjects\\seleniumProject2022\\Pytest\\txt.png')
    driver.save_screenshot('./uploadFile1.png')
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div[1]/button[1]/span').click()
    driver.save_screenshot('./afterRemove.png')

@pytest.mark.skip('just because2')
def test_hover():
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    ele=driver.find_element(By.CSS_SELECTOR, 'button#mousehover')
    topEle=driver.find_element(By.XPATH, '/html/body/div[4]/div/fieldset/div/div/a[1]')
    action=ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    action.move_to_element(ele).move_to_element(topEle).click().perform()
    time.sleep(3)
@pytest.mark.skip('just3')
def test_doubleClick():
    driver.get('https://testautomationpractice.blogspot.com/%22')
    ele=driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
    action=ActionChains(driver)
    action.double_click(ele).perform()
    if driver.find_element(By.CSS_SELECTOR, 'input#field2').get_attribute('value') == 'Hello World!':
        print('text is ok...')
        assert True
    else:
        print('The text is wrong!!!')
        assert False
    time.sleep(3)

@pytest.mark.skip('just3')
def test_dismissAlert():
    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    driver.switch_to.alert.text == 'Press a button!'
    driver.switch_to.alert.dismiss() #dismiss the alert
    time.sleep(2)

@pytest.mark.skip('just3')
def test_search4Text():
    driver.get('https://testautomationpractice.blogspot.com/%22')
    driver.find_element(By.CSS_SELECTOR,' input#Wikipedia1_wikipedia-search-input').send_keys('Idan')
    driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()
    wait=WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.LINK_TEXT, 'Idan Raichel'), 'Idan Raichel'
        )
    )
@pytest.mark.skip('just3')
def test_count_links():
    driver.get('https://testautomationpractice.blogspot.com/%22')
    ancors=driver.find_elements(By.TAG_NAME, 'a')
    print(len(ancors))
    for a in ancors:
        print(a.text)

def test_rightClick():
    driver.get('http://demo.guru99.com/test/simple_context_menu.html')
    ele=driver.find_element(By.XPATH, '//*[@id="authentication"]/span')
    action=ActionChains(driver)
    action.context_click(ele).perform()
    driver.find_element(By.XPATH, '//*[@id="authentication"]/ul/li[3]/span').click()
    time.sleep(3)
    assert driver.switch_to.alert.text == 'clicked: copy'
    driver.switch_to.alert.accept()
    time.sleep(2)