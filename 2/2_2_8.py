from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import math
import os

url = 'https://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element(By.NAME, 'firstname').send_keys('firstname')
    browser.find_element(By.NAME, 'lastname').send_keys('lastname')
    browser.find_element(By.NAME, 'email').send_keys('email@gmail.com')
    browser.find_element(By.NAME, 'file').send_keys(os.path.abspath('2_2_8.txt'))
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = Alert(browser)
    alert_text = alert.text
    print(f"Текст алерта: {alert_text}")
    alert.accept()

finally:
    browser.quit()