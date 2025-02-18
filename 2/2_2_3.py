from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time

url = 'https://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    x1 = browser.find_element(By.ID, 'num1').text
    print(x1)
    x2 = browser.find_element(By.ID, 'num2').text
    print(x2)
    ans = int(x1) + int(x2)
    Select(browser.find_element(By.ID, 'dropdown')).select_by_value(str(ans))
    print(f"answer is :{ans}")
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click() 
    
    alert = Alert(browser)
    alert_text = alert.text
    print(f"Текст алерта: {alert_text}")
    alert.accept()
    
finally:
    browser.quit()
