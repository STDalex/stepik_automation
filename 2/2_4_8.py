from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import math
import time

url = 'https://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), text_="100"))
    browser.find_element(By.ID, 'book').click()
    browser.implicitly_wait(5)
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, 'answer').send_keys(y)
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    browser.find_element(By.ID, 'solve').click()

    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = Alert(browser)
    alert_text = alert.text
    print(f"Текст алерта: {alert_text}")
    alert.accept()

finally:
    browser.quit()