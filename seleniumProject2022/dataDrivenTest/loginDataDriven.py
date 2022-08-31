import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
service = Service('C://Drivers/chromedriver.exe')
driver= webdriver.Chrome(service=service)
driver.get('http://testphp.vulnweb.com/login.php')
driver.maximize_window()

path='C:/ExcelsFiles4Auto/loginData.xlsx'
rows= XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username= XLUtils.readData(path, 'Sheet1', r, 1)
    password= XLUtils.readData(path, 'Sheet1', r, 2)

    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/table/tbody/tr[1]/td[2]/input').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/table/tbody/tr[2]/td[2]/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/table/tbody/tr[3]/td/input').click()
    time.sleep(2)
    print('title:{}'.format(driver.title))
    if driver.title == 'user info':
        print('Login ended successfully ')
        XLUtils.writeData(path, 'Sheet1', r, 3, 'Pass')
        time.sleep(1)
        # driver.find_element(By.LINK_TEXT,'Logout').click()
        # time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="sectionLinks"]/ul/li[4]/a').click()  # logout for new login        XLUtils.writeData(path, 'Sheet1', r, 3, 'Fail')
        driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/table/tbody/tr[1]/td[2]/input').clear()
        driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/table/tbody/tr[2]/td[2]/input').clear()

    else:
        XLUtils.writeData(path, 'Sheet1', r, 3, 'Failed')
        print('Login Failed ')

    # else:
    #     print('Test failed!!!')



driver.quit()
