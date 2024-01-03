from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
# to maximize the window use maximize_window() method
driver.maximize_window()
print(driver.title)

# refresh method for refreshing the current page
driver.refresh()

# current_url property fetches current URL
print('Current URL is ', driver.current_url)

# forward and back methods for forwarding and going back to previous page
driver.get('https://rahulshettyacademy.com/')
print('New website:', driver.title)
driver.back()
print('Back to previous:', driver.title)
driver.forward()
print('After forward:', driver.title);

# close for closing single window and quit method is for closing all windows
driver.close()
