from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = 'http://suninjuly.github.io/file_input.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    first_name_element = driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    first_name_element.send_keys('test')

    first_name_element = driver.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    first_name_element.send_keys('test')

    first_name_element = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    first_name_element.send_keys('test')

    file_upload_element = driver.find_element(By.ID, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    file_upload_element.send_keys(file_path)

    button_submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button_submit.click()

finally:
    time.sleep(10)
    driver.quit()
