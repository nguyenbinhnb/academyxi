import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.ThankYouPage import ThankYouPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from wrapper.BasePage import BasePage


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class Test_001_Frequent_Failures:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_001_frequent_failures(self):
        self.logger.info("Test_001_main_flow")
        self.logger.info("Started Go To Home page")
        self.driver.get(self.baseURL)
        self.homePage= HomePage(self.driver)
        self.homePage.verify_images_are_not_broken_on_home_page()
        # self.driver.get("https://the-internet.herokuapp.com/broken_images")
        # self.basePage = BasePage(self.driver)
        # self.basePage.verify_image_is_not_broken2()

