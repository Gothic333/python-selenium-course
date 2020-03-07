import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# link - тестируемая страница
# wait_time - задержка для наглядности
# search_wait_time - время на поиск кнопки
# add_to_basket_btn_selector - селектор кнопки "Добавить в корзину"
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
wait_time = 30
search_wait_time = 15
add_to_basket_btn_selector = 'button.btn-add-to-basket'


# Тестовая функция проверки наличия на странице кнопки "Добавить в корзину"
def test_page_contains_add_to_basket_button(browser):
    browser.get(link)
    # Опциональная задержка, замедляет тест, можно закомментировать
    time.sleep(wait_time)

    try:
        _ = WebDriverWait(browser, search_wait_time).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, add_to_basket_btn_selector)))
    except Exception as e:
        assert 0, 'Test failure. Search timeout ({}s), exception - {}'.format(search_wait_time, str(e))
