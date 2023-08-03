from time import sleep

from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchFlightResult(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

    # LOCATORS
    ONE_STOP_FILTER_BTN = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    TWO_STOP_FILTER_BTN = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    NON_STOP_FILTER_BTN = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    ALL_STOPS = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"

    def getonestopfilterbtnlocation(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.ONE_STOP_FILTER_BTN)

    def gettwostopfilterbtnlocation(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.TWO_STOP_FILTER_BTN)

    def getnonstopfilterbtnlocation(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.NON_STOP_FILTER_BTN)

    def getsearchflightresults(self):
        return self.wait_until_presence_of_all_elements_located(By.XPATH, self.ALL_STOPS)

    def filter_by_stops(self, by_stop):
        if by_stop == "1 Stop":
            sleep(1)
            self.getonestopfilterbtnlocation().click()
            print("Selected flights with 1 stop")
            sleep(2)
        elif by_stop == "2 Stop":
            sleep(1)
            self.gettwostopfilterbtnlocation().click()
            print("Selected flights with 2 stop")
            sleep(2)
        elif by_stop == "Non Stop":
            sleep(1)
            self.getnonstopfilterbtnlocation().click()
            print("Selected flights with 0 stop")
            sleep(2)
        else:
            print("please provide valid filter options")