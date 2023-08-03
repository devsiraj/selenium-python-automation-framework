from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def scroll_page(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while match == False:
            lastCount = pageLength
            sleep(1)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
        sleep(4)

    def wait_until_presence_of_all_elements_located(self, locatortype, locator):
        wait = WebDriverWait(self.driver, 50)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locatortype, locator)))
        return list_of_elements


    def wait_until_element_to_be_clickable(self, locatortype, locator):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.element_to_be_clickable((locatortype, locator)))
        return element

    def wait_until_presence_of_element_located(self,locatortype, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_element_located((locatortype, locator)))
        return element
