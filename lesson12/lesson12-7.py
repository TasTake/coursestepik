from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def finders(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element(By.CLASS_NAME, "first_block .form-control.first")
    element1.send_keys("Name")

    element2 = browser.find_element(By.CLASS_NAME, "first_block .form-control.second")
    element2.send_keys("Surname")

    element3 = browser.find_element(By.CLASS_NAME, "first_block .form-control.third")
    element3.send_keys("email")

    element4 = browser.find_element(By.CLASS_NAME, "second_block .form-control.first")
    element4.send_keys("phone")

    element5 = browser.find_element(By.CLASS_NAME, "second_block .form-control.second")
    element5.send_keys("address")

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
    return welcome_text

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(finders("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "Should be the same text")
        
    def test_abs2(self):
        self.assertEqual(finders("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "Should be the same text")
        
if __name__ == "__main__":
    unittest.main()