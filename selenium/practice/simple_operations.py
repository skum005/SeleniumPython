from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
print(driver.title)

label_text = driver.find_element(By.CSS_SELECTOR, 'label.form-check-label').text

driver.find_element(By.NAME, 'name').send_keys('Santosh')
driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']').click()

driver.maximize_window()
print(label_text)
driver.close()

