from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import math

url = 'https://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, 'answer').send_keys(y)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    button.click()
    
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = Alert(browser)
    alert_text = alert.text
    print(f"Текст алерта: {alert_text}")
    alert.accept()

finally:
    browser.quit()