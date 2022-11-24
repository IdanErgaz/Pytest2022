from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pytest, time


###################################################
@pytest.fixture()
def setup():
    print('####   setup  ######')
    global driver
    service = Service('C://Drivers/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get('http://google.com')
    yield
    print('###### Teardown    ########')
    driver.quit()


def test_countLinks(setup):
    print('running counting links...')
    driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
    linkElement= driver.find_elements(By.TAG_NAME, 'a')
    print('Links number:' + str(len(linkElement)))
    for l in linkElement:
        print(l.text)
        if 'ASIA' == l.text:
            print('ASIA was found!...')
        else:
            print('ASIA failed to be found!!!!!')