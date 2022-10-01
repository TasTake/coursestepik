import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

link = "http://suninjuly.github.io/registration2.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    time.sleep(3)
    input1 = driver.find_element(By.NAME, "first_name")
    input1.send_keys("Danya")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Sukhoparov")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Pskov")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys('Russia')
    button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    time.sleep(10)
    driver.quit()