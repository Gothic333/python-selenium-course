import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    value_element = driver.find_element(By.ID, 'input_value')
    x = int(value_element.text)
    result = calc(x)

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(result)

    robot_checkbox = driver.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robots_rule = driver.find_element(By.ID, 'robotsRule')
    robots_rule.click()

    button_submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button_submit.click()

finally:
    time.sleep(10)
    driver.quit()
