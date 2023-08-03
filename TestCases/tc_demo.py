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
        # launching the browser
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(
            executable_path="C:/Users/Siraj/PycharmProjects/chromedriver-win64/chromedriver-win64/chromedriver.exe",
            options=options)
        ex_wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get("https://www.yatra.com")
        flight_origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        flight_origin.click()
        flight_origin.send_keys("New Delhi")
        flight_origin.send_keys(Keys.ENTER)
        flight_destination = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        sleep(1)
        flight_destination.send_keys("New York")
        suggestion_list = ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))
            # . \
            # find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")

        for item in suggestion_list:
            if "New York (JFK)" in item.text:
                item.click()
                break

        origin_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin_date.click()

        select_date = ex_wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))). \
            find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in select_date:
            # print(date.get_attribute("data-date"))
            x = date.get_attribute("data-date")
            if "30/10/2023" in x:
                date.click()
                break

        search_btn = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']")
        search_btn.click()
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']"))).click()

        # page scroller code
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
        # end of page scroller code

        number_of_stops = ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")))
            # .\
            # find_elements(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")

        print(len(number_of_stops))
        for stops in number_of_stops:
            print(stops.text)
            assert stops.text == "1 Stop"
            print("assert pass")
            # if stops.text == "":
            #     continue
            # elif "1 Stop" in stops.text:
            #     assert stops.text == "1 Stop"
            #     print("assert pass")
            # else:
            #     assert stops.text != "1 Stop"
            #     print("assert pass")

        sleep(5)
        driver.close()

tfd = TestFrameworkDemo()
tfd.automation_test_framework_demo()
