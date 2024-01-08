from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
radio1 = driver.find_element(By.CSS_SELECTOR, 'input[value=\'radio1\']')
radio1.click()
print(radio1.is_selected())

checkbox2 = driver.find_element(By.CSS_SELECTOR, 'input[name=\'checkBoxOption2\']')
print(checkbox2.is_selected())
checkbox2.click()
print(checkbox2.is_selected())

driver.close()
