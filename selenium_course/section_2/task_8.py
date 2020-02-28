import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    book_button = driver.find_element(By.ID, 'book')
    book_button.click()

    value_element = driver.find_element(By.ID, 'input_value')
    x = int(value_element.text)
    result = calc(x)

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(result)

    button_submit = driver.find_element(By.ID, 'solve')
    button_submit.click()

finally:
    time.sleep(10)
    driver.quit()
