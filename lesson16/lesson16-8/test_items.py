from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_should_be_present(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "btn btn-lg btn-primary btn-add-to-basket")
    assert button != NULL