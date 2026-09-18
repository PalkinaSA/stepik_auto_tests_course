from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    first_name = browser.find_element(By.NAME, "firstname")
    last_name = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    bio_text_file = browser.find_element(By.NAME, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    first_name.send_keys("Palkina")
    last_name.send_keys("Sofia")
    email.send_keys("my_email@gmail.ru")
    bio_text_file.send_keys(file_path)

    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

finally:
    time.sleep(30)
    browser.quit()
    
