from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj = Service()
#driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
driver.quit()


