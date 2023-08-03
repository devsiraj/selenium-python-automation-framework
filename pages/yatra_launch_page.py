from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Base.base_driver import BaseDriver
from pages.search_flights_page import SearchFlightResult
from utilities.utils import Utils

class YatraLaunchPage(BaseDriver):

    log = Utils().custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    FLIGHT_ORIGIN = "//input[@id='BE_flight_origin_city']"
    FLIGHT_DESTINATION = "//input[@id='BE_flight_arrival_city']"
    ORIGIN_DATE = "//input[@id='BE_flight_origin_date']"
    SELECT_DATE = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_FLIGHT_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"
    SUGGESTIONS_LIST = "//div[@class='viewport']//div[1]/li"
    AD_POP_UP = "//a[@id='webklipper-publisher-widget-container-notification-close-div']"
    AD_FRAME = "//iframe[@id='webklipper-publisher-widget-container-notification-frame']"
    # LOCATION PROVIND METHOD'S
    def getflightoriginlocation(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.FLIGHT_ORIGIN)

    def getflightdestinationlocation(self):
        return self.driver.find_element(By.XPATH, self.FLIGHT_DESTINATION)

    def getorigindatelocation(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.ORIGIN_DATE)

    def getselectdatelocation(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.SELECT_DATE)

    def getsearchflightlocation(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_FLIGHT_BUTTON)

    def getsuggestionslistlocation(self):
        return self.wait_until_presence_of_all_elements_located(By.XPATH, self.SUGGESTIONS_LIST)

    def getpopupadclosebtnlocation(self):
        return self.wait_until_presence_of_element_located(By.XPATH, self.AD_POP_UP)

    def getpopupframelocation(self):
        return self.wait_until_presence_of_element_located(By.XPATH, self.AD_FRAME)
    # END OF LOCATION PROVIDING METHOD'S

    # ELEMENT ACTIONS PROVIDING METHODS
    def switch_to_ad_frame(self):
        sleep(3)
        frame = self.getpopupframelocation()
        self.driver.switch_to.frame(frame)

    def close_ad_pop_up(self):
        sleep(3)
        self.getpopupadclosebtnlocation().click()
        self.log.info("Close button of pop ad is clicked !")

    def enter_flight_origin(self, departfrom):
        flight_origin = self.getflightoriginlocation()
        flight_origin.click()
        self.log.info("Flight origin text field clicked")
        sleep(1)
        flight_origin.send_keys(departfrom)
        sleep(1)
        self.log.info("Typed :" + departfrom)
        flight_origin.send_keys(Keys.ENTER)
        self.log.info("ENTER Key pressed")

    def enter_flight_destination(self, goingto):
        flight_destination = self.getflightdestinationlocation()
        sleep(1)
        flight_destination.click()
        sleep(1)
        flight_destination.send_keys(goingto)
        # sleep(1)
        suggestion_list = self.getsuggestionslistlocation()
        for item in suggestion_list:
            if goingto in item.text:
                item.click()
                break

    def select_date(self, departuredate):
        origin_date = self.getorigindatelocation()
        origin_date.click()
        select_date = self.getselectdatelocation().find_elements(By.XPATH, self.SELECT_DATE)
        for date in select_date:
            x = date.get_attribute("data-date")
            if departuredate in x:
                date.click()
                break

    def click_search(self):
        search_btn = self.getsearchflightlocation()
        search_btn.click()

    def search_flight(self, departfrom, goingto, departuredate):
        self.switch_to_ad_frame()
        self.close_ad_pop_up()
        self.enter_flight_origin(departfrom)
        self.enter_flight_destination(goingto)
        self.select_date(departuredate)
        self.click_search()
        search_flight_results = SearchFlightResult(driver=self.driver)
        return search_flight_results

    def open_home_page(self):
        sleep(5)
