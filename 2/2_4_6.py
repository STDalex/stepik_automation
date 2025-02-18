from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://suninjuly.github.io/cats.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element(By.ID, "button")

finally:
    browser.quit()