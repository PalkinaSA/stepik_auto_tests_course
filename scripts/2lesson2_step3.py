from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    result = int(num1) + int(num2)

    selects = Select(browser.find_element(By.TAG_NAME, "select"))
    selects.select_by_value(str(result))
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
finally:
    time.sleep(30)
    browser.quit()
