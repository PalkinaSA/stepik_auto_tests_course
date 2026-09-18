from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    browser.implicitly_wait(1)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button_submit = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    button_submit.click()

finally:
    time.sleep(30)
    browser.quit()
    
