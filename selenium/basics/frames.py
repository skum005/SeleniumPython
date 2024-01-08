from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

frame_element = driver.find_element(By.ID, 'courses-iframe')
driver.switch_to.frame(frame_element)

print('Getting text of an element inside a frame:', driver.find_element(By.CSS_SELECTOR, 'a[href=\'lifetime-access\']').text)
driver.switch_to.default_content()

mouseHoverElement = driver.find_element(By.ID, 'mousehover')
actions = ActionChains(driver)
actions.move_to_element(mouseHoverElement).click(driver.find_element(By.XPATH, '//div[@class=\'mouse-hover-content\']/a[2]')).perform()

driver.maximize_window()
driver.close()
