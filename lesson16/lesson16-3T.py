import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def get_answer():
    answer = math.log(int(time.time()))
    return answer

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", 
"https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1"
, "https://stepik.org/lesson/236905/step/1"])
def test_send_key_and_submit(browser, link):
    browser.get(link)
    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "textarea")))
    element.send_keys(get_answer())
    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()
    msg = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    msgT = msg.text
    assert msgT == "Correct!"