from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')


# method 1 - using Select class
dropdownElement = driver.find_element(By.ID, 'exampleFormControlSelect1')
gender_dropdown = Select(dropdownElement)
gender_dropdown.select_by_visible_text('Male')

# method 2 - by iterating through all elements of the dropdown values
dropdown_elements = driver.find_elements(By.CSS_SELECTOR, 'select#exampleFormControlSelect1 option')
dropdownElement.click()
for element in dropdown_elements:
    if(element.text == 'Female'):
        element.click()
        break

driver.close()
