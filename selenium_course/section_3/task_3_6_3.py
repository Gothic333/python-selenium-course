import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def browser():
    print('\nOpen browser for test')
    browser = webdriver.Chrome()
    yield browser
    print('\nClose browser')
    browser.quit()


@pytest.mark.parametrize('page_code', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_feedback_is_correct(browser, page_code):
    link = 'https://stepik.org/lesson/{}/step/1'.format(page_code)
    browser.get(link)

    text_field = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'textarea')))
    answer = math.log(int(time.time()))
    text_field.send_keys(str(answer))

    button_submit = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
    button_submit.click()

    feedback_element = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'pre')))
    feedback_text = feedback_element.text

    assert feedback_text == 'Correct!', 'Test fails, code - {}, message - {}'.format(page_code, feedback_text)

