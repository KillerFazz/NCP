from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    # driver = webdriver.Chrome()
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome -------------------")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox --------------------")
    else:
        driver = webdriver.Chrome()
        print('Default Browser')

    return driver

def pytest_addOption(parser):  # This will get the value from CLI/hooks
        parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return  the browser value to set up method
    return request.config.getoption("--browser")






# "*********It is hook for adding Environment info to HTMl Report***********"

def pytest_configure(config):
    config._metadata["Project name"] = "Nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = 'Shaikh'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
