from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    transition_button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    transition_button.click()

    confirm = driver.switch_to.alert
    confirm.accept()

    value_element = driver.find_element(By.ID, 'input_value')
    x = int(value_element.text)
    result = calc(x)

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(result)

    button_submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button_submit.click()

finally:
    time.sleep(10)
    driver.quit()
