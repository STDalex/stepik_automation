from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

url = 'https://suninjuly.github.io/find_link_text'
text_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    link = browser.find_element(By.LINK_TEXT, text_link)
    link.click()
    browser.find_element(By.NAME, 'first_name').send_keys('Alexander')
    browser.find_element(By.NAME, 'last_name').send_keys('Smith')
    browser.find_element(By.NAME, 'firstname').send_keys('Moscow')
    browser.find_element(By.ID, 'country').send_keys('Russia')
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    time.sleep(10)
    browser.quit()