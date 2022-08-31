from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
##############################################################
service=Service('C://Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()
DDL= driver.find_element(By.ID, 'RESULT_RadioButton-9')
Select(DDL).select_by_index(1) #SELECT BY INDEX -->"MORNING"
time.sleep(2)
Select(DDL).select_by_value('Radio-1') #select by value ->afternoon
time.sleep(2)
Select(DDL).select_by_visible_text('Evening') #select by visible text -->Evening
time.sleep(2)
#Count ALL the DDP options
print("The ddl has {} options ".format(len(Select(DDL).options)))
#Print all option from the ddl
all_options= Select(DDL).options
for option in all_options :
    print(option.text)
driver.quit()