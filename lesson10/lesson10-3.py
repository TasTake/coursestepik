from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    """
    browser.switch_to.window(window_name)
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    """

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()