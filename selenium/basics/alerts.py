from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
name = 'Santosh Balaga'
driver.find_element(By.ID, 'name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()



driver.close()
