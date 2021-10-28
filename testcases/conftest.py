from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.options import Options

# fixtures are function which us used to before testcase is calling

@pytest.fixture(scope="session")
def setup(browser):
    global driver

    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager.install())
        driver.maximize_window()
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
    return driver

def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")




