from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    numLink1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    numLink2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num1 = numLink1.text
    num2 = numLink2.text

    y = int(num1) + int(num2)
    
    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    browser.find_element(By.CSS_SELECTOR, "[value='%s']" % y).click()
    
    option = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    option.click() 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()