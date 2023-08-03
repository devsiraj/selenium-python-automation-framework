import pytest
import softest
from pages.yatra_launch_page import YatraLaunchPage
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchFlights(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = YatraLaunchPage(driver=self.driver)
        self.ut = Utils()

    @pytest.mark.ddtdata
    @data(("New Delhi", "New York", "30/10/2023", "1 Stop"), ("Mumbai", "New York", "30/08/2023", "2 Stop"))
    @unpack
    def test_search_flights_for_one_stop(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.search_flight(goingfrom, goingto, date)
        search_flight_result.filter_by_stops(stops)
        self.lp.scroll_page()
        number_of_stops = search_flight_result.getsearchflightresults()
        print(len(number_of_stops))
        self.ut.assertlistitemtext(number_of_stops, stops)
        self.driver.quit()

    @pytest.mark.jsondata
    @file_data("../TestData/testdata.json")
    def test_search_flights_for_one_stop(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.search_flight(goingfrom, goingto, date)
        search_flight_result.filter_by_stops(stops)
        self.lp.scroll_page()
        number_of_stops = search_flight_result.getsearchflightresults()
        print(len(number_of_stops))
        self.ut.assertlistitemtext(number_of_stops, stops)
        self.driver.quit()

    @pytest.mark.yamldata
    @file_data("../TestData/testdata.yaml")
    def test_search_flights_for_one_stop(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.search_flight(goingfrom, goingto, date)
        search_flight_result.filter_by_stops(stops)
        self.lp.scroll_page()
        number_of_stops = search_flight_result.getsearchflightresults()
        print(len(number_of_stops))
        self.ut.assertlistitemtext(number_of_stops, stops)
        self.driver.quit()


    @pytest.mark.exceldata
    @data(*Utils.read_data_from_excel("C:\\Users\\Siraj\\PycharmProjects\\TestFrameworkDemo\\TestData\\testdata.xlsx", "Sheet1"))
    @unpack
    def test_search_flights_for_one_stop(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.search_flight(goingfrom, goingto, date)
        search_flight_result.filter_by_stops(stops)
        self.lp.scroll_page()
        number_of_stops = search_flight_result.getsearchflightresults()
        print(len(number_of_stops))
        self.ut.assertlistitemtext(number_of_stops, stops)
        self.driver.quit()

    @pytest.mark.csvdata
    @data(*Utils.read_data_from_csv("C:\\Users\\Siraj\\PycharmProjects\\TestFrameworkDemo\\TestData\\testdata.csv"))
    @unpack
    def test_search_flights_for_one_stop(self, goingfrom, goingto, date, stops):
        search_flight_result = self.lp.search_flight(goingfrom, goingto, date)
        search_flight_result.filter_by_stops(stops)
        self.lp.scroll_page()
        number_of_stops = search_flight_result.getsearchflightresults()
        print(len(number_of_stops))
        self.ut.assertlistitemtext(number_of_stops, stops)
        self.driver.quit()


# to generate html report pass  pytest --html=report.html --self-contained-html along with pytest command in cmd
