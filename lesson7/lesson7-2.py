from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_chest = browser.find_element(By.ID, "treasure")

    x = treasure_chest.get_attribute("valuex")
    y = calc(x)

    element1 = browser.find_element(By.CSS_SELECTOR, "input[type='text']")
    element1.send_keys(y)

    
    option1 = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    option1.click() 
    

    option2 = browser.find_element(By.CSS_SELECTOR, ".check-input[value='robots']")
    option2.click() 

    option3 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    option3.click() 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()