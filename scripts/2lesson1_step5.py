from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    
finally:
    time.sleep(30)
    browser.quit()
