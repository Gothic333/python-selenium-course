from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_registration(link):
    welcome_text = ''
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        selectors = ['first', 'second', 'third']
        for selector in selectors:
            req_field = browser.find_element(By.CSS_SELECTOR, 'input[required].' + selector)
            req_field.send_keys('test')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        welcome_text_elt = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h1'))
        )
        welcome_text = welcome_text_elt.text

    finally:
        browser.quit()
        return welcome_text
