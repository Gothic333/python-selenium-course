from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = 'http://suninjuly.github.io/selects1.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    num1_element = driver.find_element(By.ID, 'num1')
    num2_element = driver.find_element(By.ID, 'num2')

    num1 = num1_element.text
    num2 = num2_element.text
    result = str(int(num1) + int(num2))

    dropdown_select = Select(driver.find_element(By.ID, 'dropdown'))
    dropdown_select.select_by_value(result)

    button_submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button_submit.click()

finally:
    time.sleep(10)
    driver.quit()
