import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def setup(request):
    if request.params == "chrome":
        service = Service('C://Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        driver.get('https://google.com')



