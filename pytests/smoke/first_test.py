from selenium import webdriver

def test_title():
    driver = webdriver.Chrome()
    driver.get('https://www.lambdatest.com/automation-demos')
    assert driver.title == 'Selenium Playground | LambdaTest', 'Title doesn\'t match'

def test_login():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    assert driver.title == 'Googlee', 'title doesn\'t match'
