from selenium import webdriver
from selenium.webdriver.common.by import By
import time, pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains


##############################################################
def setup_module(module):
    print('once before ALL...')
    service = Service('C://Drivers/chromedriver.exe')
    global driver
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://testautomationpractice.blogspot.com/%22')
    driver.maximize_window()


def teardown_module(module):
    print('once AFTER all tests...')
    driver.quit()


@pytest.mark.skip('becauseIdanSaid')
def test_ddl():
    print('ddl test  is running...')
    ele = driver.find_element(By.CSS_SELECTOR, 'select#speed')
    select = Select(ele)
    select.select_by_index('1')  # select slow option


@pytest.mark.skip('becauseIdanSaid')
def test_search():
    print('search test  is running...')
    driver.find_element(By.CSS_SELECTOR, 'input.wikipedia-search-input').send_keys('Idan')
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()
    time.sleep(5)


@pytest.mark.skip('becauseIdanSaid')
def test_drag():
    print('test drag and drop...')
    source = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[1]/img')
    dest = driver.find_element(By.CSS_SELECTOR, 'div#trash')
    action = ActionChains(driver)
    action.drag_and_drop(source, dest).perform()
    time.sleep(2)
    driver.save_screenshot('./drag2.png')


@pytest.mark.skip('becauseIdanSaid')
def test_drag2():
    print('test drag2..')
    slider = driver.find_element(By.CSS_SELECTOR, 'span.ui-slider-handle')
    slider_location = slider.location
    print(slider_location)
    move = ActionChains(driver)
    move.drag_and_drop_by_offset(slider, 100, 0).perform()
    time.sleep(3)


@pytest.mark.skip('becauseIdanSaid')
def test_radio():
    print('test radio buttons...')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    femaleEle = driver.find_element(By.CSS_SELECTOR, 'input#RESULT_RadioButton-7_1')
    # driver.find_element(By.XPATH, '//*[@id="RESULT_RadioButton-7_1"]').click()
    driver.execute_script("arguments[0].click();", femaleEle)
    driver.save_screenshot('./radioButton1.png')


@pytest.mark.skip('becauseIdanSaid')
def test_uploadFile():
    print('uploadFile tes...')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    driver.find_element(By.XPATH, '//*[@id="RESULT_FileUpload-10"]').send_keys(
        'C://Users/user/PycharmProjects/seleniumProject2022/Pytest/doubleClick.png')
    time.sleep(3)


@pytest.mark.skip('becauseIdanSaid')
def test_form():
    print('test form...')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    driver.find_element(By.CSS_SELECTOR, 'input[name=RESULT_TextField-1]').send_keys('Idan')
    driver.find_element(By.CSS_SELECTOR, '#RESULT_TextField-2').send_keys('007')
    driver.find_element(By.CSS_SELECTOR, '#RESULT_TextField-3').send_keys('0525444181')
    driver.find_element(By.CSS_SELECTOR, '#RESULT_TextField-4').send_keys('iSRAEL')
    driver.find_element(By.CSS_SELECTOR, '#RESULT_TextField-5').send_keys('rISHON')
    driver.find_element(By.CSS_SELECTOR, '#RESULT_TextField-6').send_keys('aaa@gmail.com')
    time.sleep(4)


@pytest.mark.skip('becauseIdanSaid')
def test_rightClick():
    print('test right click...')
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys('Admin')
    driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys('admin123')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    wait = WebDriverWait(driver, 7)
    ele = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5')
    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5'), 'Employee Information')
    )
    driver.save_screenshot('./aftreLogin.png')


@pytest.mark.skip('becauseIdanSaid')
def test_rightClick():
    print('test rightClick....')
    driver.get('https://demo.guru99.com/test/simple_context_menu.html')
    ele = driver.find_element(By.XPATH, '//*[@id="authentication"]/span')
    action = ActionChains(driver)
    action.context_click(ele).perform()
    time.sleep(2)
    copyEle = driver.find_element(By.XPATH, '//*[@id="authentication"]/ul/li[3]')
    action.click(copyEle).perform()
    assert driver.switch_to.alert.text == 'clicked: copy'
    time.sleep(2)
    driver.switch_to.alert.accept()
    driver.save_screenshot('./acceptAlert.png')


@pytest.mark.skip('because2...')
def test_hover():
    print('test hover and click ...')
    driver.get('https://demo.guru99.com/test/tooltip.html')
    # driver.switch_to.frame('googlefcLoaded')
    downloadEle = driver.find_element(By.XPATH, '//*[@id="download_now"]')
    downloadEle.click()
    linkEle = driver.find_element(By.LINK_TEXT, "What's new in 3.2")
    action = ActionChains(driver)
    action.move_to_element(downloadEle).perform()
    action.move_to_element(downloadEle).click(linkEle).perform()
    # action.move_to_element(downloadEle).click(linkEle).perform()
    pageText = driver.find_element(By.XPATH, '/html/body/h1')
    wait = WebDriverWait(driver, 6)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '/html/body/h1'), 'Not Found'
        )
    )

@pytest.mark.skip('because 3 ...')
def test_countLinks():
    print('count links test')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    links = driver.find_elements(By.CLASS_NAME, 'link')
    print(len(links))
    for link in links:
        print(link.text)

    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type=checkbox]')
    print(len(checkboxes))
    for checkbox in checkboxes:
        print(checkbox.get_attribute("value"))

def test_scroll2element():
    print('test scroll to element..')
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    targetElement= driver.find_element(By.CSS_SELECTOR, 'input[type=submit]')
    driver.execute_script("arguments[0].scrollIntoView();", targetElement)
    print(targetElement.get_attribute("value"))
    assert targetElement.get_attribute("value") == 'Submit'
    time.sleep(4)

