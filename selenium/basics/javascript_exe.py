from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
driver.close()
