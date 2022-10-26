from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "div[class='container'] span:nth-child(2)")
    x = x_element.text
    y = calc(x)

    element1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    element1.send_keys(y)

    
    option1 = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    option1.click() 
    

    option2 = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    option2.click() 

    option3 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    option3.click() 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()