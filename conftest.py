import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--headless')
    options.add_argument('--start_maximized')
    options.add_argument('--window-size = 1400, 700')
    return options


@pytest.fixture(scope='function')
def get_webdriver(get_chrome_options):
    options = get_chrome_options()
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='class')
def welcome(request):
    # driver = get_webdriver
    driver = webdriver.Chrome()
    driver.set_window_size(1400, 700)
    url = 'https://www.labirint.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
