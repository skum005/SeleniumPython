from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
driver.get_screenshot_as_png()
driver.get_screenshot_as_file('test.png')
driver.close()
