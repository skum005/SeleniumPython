from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://rahulshettyacademy.com/angularpractice/')
checkbox = browser.find_element(By.ID, 'exampleCheck1')
print(checkbox.get_attribute('type')) # this should print the value of the attribute 'type'
browser.close()
