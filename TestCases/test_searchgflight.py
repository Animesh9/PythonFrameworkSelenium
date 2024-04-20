import pytest
import softest
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack, file_data
from pages.LaunchPage import launchPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchFlight(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = launchPage(self.driver)
        self.ut = Utils()

    # @data(("03/06/2024", "1"), ("05/05/2024", "2"))
    # @unpack
    # @file_data("..//TestData//testyml.yaml")
    # @data(*Utils.read_data_from_excel("..\\TestData\\testExcel.xlsx", "Sheet1"))
    # run this command to get report of tests pytest -v --html=./reports/report.html --self-contained-html
    @data(*Utils.read_data_from_csv("D:\\Help\\Selenium\\PythonFrameworkSelenium\\TestData\\testDataCSV.csv"))
    @unpack
    def testLaunch(self, date, name):
        print(name, '\n')
        self.lp.launch(date)
        self.lp.filter()
        self.lp.scrollWindow()
        all_stops = self.lp.wait_for_locators(By.XPATH, "//span[@class='dotted-borderbtm'][normalize-space()='2 Stop(s)']")
        print(len(all_stops))

        self.ut.assertListItemText(all_stops, "2 Stop(s)")

        self.driver.get("https://www.yatra.com/")
