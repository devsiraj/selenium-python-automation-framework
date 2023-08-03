from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


class TestFrameworkDemo:
    def automation_test_framework_demo(self):
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(
            executable_path="C:/Users/Siraj/PycharmProjects/chromedriver-win64/chromedriver-win64/chromedriver.exe",
            options=options)
        ex_wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get("https://www.firewatchgame.com/")
        sleep(10)
        pageLength = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while match == False:
            lastCount = pageLength
            sleep(1)
            pageLength = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
        sleep(4)


tfd = TestFrameworkDemo()
tfd.automation_test_framework_demo()