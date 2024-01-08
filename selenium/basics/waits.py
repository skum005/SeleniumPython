from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('')

# implicit wait setting - waits for 30 seconds
driver.implicitly_wait(30)

def explictWait(element, timeout):
    wait = WebDriverWait(driver, timeout)
    wait.until(expected_conditions.presence_of_element_located(By.ID, ''))
