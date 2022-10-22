from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    browser.execute_script("prompt('Hello!');")
    """
    browser.execute_script("alert('Hello!');")
    browser.execute_script("confirm('Hello!');")
    browser.execute_script("prompt('Hello!');")
    alert = browser.switch_to.alert
    alert.accept()
    alert_text = alert.text
    print(alert_text)
    
    confirm = browser.switch_to.alert
    confirm.accept()
    confirm.dismiss()
    
    prompt = browser.switch_to.alert
    time.sleep(2)
    prompt.send_keys("My answer")
    time.sleep(2)
    prompt.accept()
    """

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()