from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select





service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()

#how many links there are?

links= driver.find_elements(By.TAG_NAME, 'a')

numberOfLinks= len(links)
print('the number of links is:{}'.format(numberOfLinks))


for link in links:
    print(link.text)
#capture a link
#clicking on the link

driver.find_element(By.LINK_TEXT, 'Software Testing Tutorials').click()
assert driver.title =='SDET QA Automation Techie'
print('the link redirec works fine!!!!')


#click on the link

