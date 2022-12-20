import time

import pytest
from selenium.webdriver import ActionChains
from wrapper.BasePage import BasePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class TestValidatePricesOnMainPages:
    baseURL = ReadConfig.getApplicationURL("baseURL")
    logger = LogGen.loggen()
    daTransformPartTimeURL = ReadConfig.getApplicationURL("DA Transform Part Time Page")
    daTransformFullTimeURL = ReadConfig.getApplicationURL("DA Transform Full Time Page")

    @pytest.mark.sanity
    # @pytest.mark.regression
    @pytest.mark.smoke
    def test_001_validate_prices_on_da_transform_part_time_page(self):
        self.logger.info("Test_001_validate_prices_on_da_transform_part_time_page")
        self.driver.get(self.daTransformPartTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_prices()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_002_validate_prices_on_da_transform_full_time_page(self):
        self.logger.info("Test_002_validate_prices_on_da_transform_full_time_page")
        self.driver.get(self.daTransformFullTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_prices()
