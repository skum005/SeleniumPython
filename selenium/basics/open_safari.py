from selenium import webdriver

driver = webdriver.Safari()
driver.maximize_window()
driver.get('https://www.google.com')
print(driver.title)
driver.close()
