from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

mouseHoverElement = driver.find_element(By.ID, 'mousehover')

actions = ActionChains(driver)
actions.move_to_element(mouseHoverElement).click(driver.find_element(By.XPATH, '//div[@class=\'mouse-hover-content\']/a[2]')).perform()

driver.maximize_window()
driver.close()
