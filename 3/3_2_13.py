import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/registration2.html"

class TestRegistration(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.fields_config = {
            "first_name": {
                "selector_type": By.XPATH,
                "selector": "/html/body/div/form/div[1]/div[1]/input",
                "test_data": "firstname",
                "placeholder": "Input your first name",
                "required": True
            }
            ,
            "last_name": {
                "selector_type": By.XPATH,
                "selector": "/html/body/div/form/div[1]/div[2]/input",
                "test_data": "lastname",
                "placeholder": "Input your last name",
                "required": True
            },
            "email": {
                "selector_type": By.XPATH,
                "selector": "/html/body/div/form/div[1]/div[3]/input",
                "test_data": "email@gmail.com",
                "placeholder": "Input your email",
                "required": True
            },
            "phone": {
                "selector_type": By.XPATH,
                "selector": "/html/body/div/form/div[2]/div[1]/input",
                "test_data": "89555555555",
                "placeholder": "Input your phone:",
                "required": None
            },
            "submit_button": {
                "selector_type": By.XPATH,
                "selector": "/html/body/div/form/button",
                "test_data": None,
                "placeholder": None,
                "required": None
            }
        }

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(url)

    def test_form_elements_present(self):
        try:
            for field, config in self.fields_config.items():
                with self.subTest(field=field):
                    element = self.driver.find_element(config["selector_type"], config["selector"])
                    if not element:
                        self.fail(f"Элемент '{field}' не найден на странице.")
                    self.assertTrue(element.is_displayed(), f"Поле {field} отсутствует на форме.")
        finally:
            print('test_form_elements_present is complite')

    def test_placeholder(self):
        try:
            for field, config in self.fields_config.items():
                with self.subTest(field=field):
                    if config["placeholder"] is not None:
                        element = self.driver.find_element(config["selector_type"], config["selector"])
                        current_placeholder = element.get_attribute("placeholder")
                        self.assertEqual(config["placeholder"], current_placeholder)
        finally:
            print('test_placeholder is complite')

    def test_required(self):
        try:
            for field, config in self.fields_config.items():
                with self.subTest(field=field):
                    if config["required"] is not None:
                        element = self.driver.find_element(config["selector_type"], config["selector"])
                        required_attribute = element.get_attribute("required")
                        self.assertIsNotNone(required_attribute, "Attribute required is lost")
        finally:
            print('test_placeholder is complite')

    def test_positive_registration(self):
        try:
            for field, config in self.fields_config.items():
                if field != "submit_button":
                    element = self.driver.find_element(config["selector_type"], config["selector"])
                    element.send_keys(config["test_data"])
                else:
                    element = self.driver.find_element(config["selector_type"], config["selector"])
                    element.click()
            welcome_text_elt = self.driver.find_element(By.TAG_NAME, "h1").text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt)
        finally:
            print('test_positive_registration is complite')
    

if __name__ == "__main__":
    unittest.main()  
