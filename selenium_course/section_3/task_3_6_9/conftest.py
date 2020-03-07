import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Встроенная функция для добавления опций.
# --browser_name - используемый браузер (сhrome или firefox)
# -- language - код языка (ru, en, es и тд.)
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     default='chrome',
                     help='Choose browser: chrome of firefox')
    parser.addoption('--language', action='store',
                     default='ru',
                     help='Choose language: ru, en etc.')


# Фикстура, управляющая открытием и закрытием браузера.
# scope=function - запуск для каждого теста
@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    lang_code = request.config.getoption('language')

    browser = None
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang_code})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('initl.accept.languages', lang_code)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('browser name should be chrome or firefox')

    print('\nBrowser {} with language code {} start..'.format(browser_name, lang_code))
    yield browser
    print('\nBrowser quit..')
    browser.quit()
