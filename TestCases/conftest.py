from time import sleep

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(autouse=True)
def setup(request, browser):
    # global driver
    if browser == "chrome":
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(
            executable_path="C:/Users/Siraj/PycharmProjects/chromedriver-win64/chromedriver-win64/chromedriver.exe",
            options=options)
    elif browser == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    elif browser == None:
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(
            executable_path="C:/Users/Siraj/PycharmProjects/chromedriver-win64/chromedriver-win64/chromedriver.exe",
            options=options)
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras
