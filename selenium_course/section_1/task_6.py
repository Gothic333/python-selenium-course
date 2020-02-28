import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ссылка на тестируемую страницу
link = 'http://suninjuly.github.io/registration1.html'

# Блок теста
try:
    # Открытие браузера и переход по ссылке
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных (required) полей формы
    selectors = ['first', 'second', 'third']
    for selector in selectors:
        req_field = browser.find_element(By.CSS_SELECTOR, 'input[required].' + selector)
        req_field.send_keys('test')

    # Отправка формы. Клик по кнопке Submit
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    # Поиск заголовка и запись его текста в переменную welcome_text
    # На поиск элемента выделено 10 сек.
    welcome_text_elt = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    )
    welcome_text = welcome_text_elt.text

    # Проверка текста с сайта с ожидаемым текстом
    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    # Задержка для оценки результата
    time.sleep(10)
    # Закрыть браузер
    browser.quit()
