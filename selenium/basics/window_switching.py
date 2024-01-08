import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.implicitly_wait(30)

parentWindow = driver.current_window_handle
element = driver.find_element(By.ID, 'openwindow')
element.click()
time.sleep(5)
windowSet = driver.window_handles
childWindowId = None
if len(windowSet) == 2:
    print('2 active windows')
    for windowId in windowSet:
        if windowId != parentWindow:
            childWindowId = windowId
            break
else:
    print('Error')

if childWindowId is None:
    print('Error')

driver.switch_to.window(childWindowId)
print('child window title:', driver.title)
print('child window', childWindowId)
print('print window', parentWindow)
driver.switch_to.window(parentWindow)
print('parent window title:', driver.title)
driver.quit()
