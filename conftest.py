import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920x1080")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store_true', help='Run driver in headless mode.')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    headless = request.config.getoption('headless')
    if browser_name == 'chrome':
        if not headless:
            browser = webdriver.Chrome()
        else:
            browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == 'firefox':
        if not headless:
            browser = webdriver.Firefox()
        else:
            browser = webdriver.Firefox(options=chrome_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
# pytest -v --tb=line --browser_name=chrome --headless .\test_change_password_page.py
