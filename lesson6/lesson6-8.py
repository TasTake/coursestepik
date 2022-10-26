from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()