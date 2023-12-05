from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost:8000")

assert 'Django' in driver.title