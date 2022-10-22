from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
driver.implicitly_wait(3)

text_box = driver.find_element('xpath', '//*[@id="my-text-id"]')
text_box.send_keys('Selenium')