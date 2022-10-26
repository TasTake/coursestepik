from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    element1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    element1.send_keys("Name")

    element2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    element2.send_keys("Surname")

    element3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    element3.send_keys("E-mail")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'emptytext.txt')           # добавляем к этому пути имя файла 
    element4 = browser.find_element(By.CSS_SELECTOR, "#file")
    element4.send_keys(file_path)
    time.sleep(0.1)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()