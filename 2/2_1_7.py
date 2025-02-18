from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import math

url = 'https://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x_value = int(browser.find_element(By.ID, 'treasure').get_attribute('valuex'))
    y = str(math.log(abs(12*math.sin(int(x_value)))))
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
   # browser.find_element(By.ID, 'robotsRule').find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

    alert = Alert(browser)
    alert_text = alert.text
    print(f"Текст алерта: {alert_text}")
    alert.accept()


finally:
    browser.quit()