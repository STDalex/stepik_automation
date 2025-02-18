from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_fname = browser.find_element(By.CSS_SELECTOR, ".first_class > input")
    assert input_fname.get_attribute("required"), "first name is not required"
    assert input_fname.get_attribute('placeholder') == 'Input your first name', 'first name input has an invalid placeholder'
    input_fname.send_keys('first_name')

    input_lname = browser.find_element(By.CSS_SELECTOR, ".second_class > input")
    assert input_lname.get_attribute("required"), "last name is not required"
    assert input_lname.get_attribute('placeholder') == 'Input your last name', 'last name input has an invalid placeholder'
    input_lname.send_keys('last_name')
    
    input_email = browser.find_element(By.CSS_SELECTOR, ".third_class > input")
    assert input_email.get_attribute("required"), "email name is not required"
    assert input_email.get_attribute('placeholder') == 'Input your email', 'email input has an invalid placeholder'
    input_email.send_keys('email@gmail.com')
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, "error"
    time.sleep(3)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    
    # закрываем браузер после всех манипуляций
    browser.quit()