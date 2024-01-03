from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element(By.CSS_SELECTOR, 'input[name=\'name\']').send_keys('Santosh')
email_box = driver.find_element(By.XPATH, '//input[@name=\'email\']')
email_box.send_keys('santosh.sri54@gmail.com')

password = driver.find_element(By.ID, 'exampleInputPassword1')
password.send_keys('Testing@1234')

checkbox = driver.find_element(By.ID, 'exampleCheck1')
checkbox.click()

submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\']')
submit_button.click()

message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)

print(driver.title)
driver.close()

'''
name : input[name='name']
email : //input[@name='email']

'''
