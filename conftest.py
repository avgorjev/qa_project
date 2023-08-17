import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    print('\nstart browser for test..')
    page_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': page_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    # этот код выполнится после завершения теста
    print('\nquit browser..')
    browser.quit()
