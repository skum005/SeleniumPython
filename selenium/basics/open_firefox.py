from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.google.com')
browser.maximize_window()
print(browser.title)
browser.close()
