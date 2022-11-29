import time

import pytest
from selenium.webdriver import ActionChains
from wrapper.BasePage import BasePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class TestValidateGaAndGtmArePresentOnMainPages:
    baseURL = ReadConfig.getApplicationURL("baseURL")
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    # @pytest.mark.regression
    @pytest.mark.smoke
    def test_001_validate_ga_and_gtm_are_present_on_home_page(self):
        self.logger.info("Test_001_validate_ga_and_gtm_are_present_on_home_page")
        self.driver.get(self.baseURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        time.sleep(2)
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_ga_and_gtm_are_present()

    # @pytest.mark.regression
    @pytest.mark.smoke
    def test_002_validate_ga_and_gtm_are_present_on_checkout_page(self):
        self.logger.info("Test_001_validate_ga_and_gtm_are_present_on_checkout_page")
        self.driver.get(self.baseURL+"checkout/")
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        time.sleep(2)
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_ga_and_gtm_are_present()

    # @pytest.mark.regression
    @pytest.mark.smoke
    def test_003_validate_ga_and_gtm_are_present_on_thank_you_page(self):
        self.logger.info("Test_001_validate_ga_and_gtm_are_present_on_thank_you_page")
        self.driver.get(self.baseURL+"/online-courses/user-experience-design/course-guide/thank-you/")
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        time.sleep(2)
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_ga_and_gtm_are_present()

    # @pytest.mark.regression
    @pytest.mark.smoke
    def test_004_validate_ga_and_gtm_are_present_on_landing_page(self):
        self.logger.info("Test_001_validate_ga_and_gtm_are_present_on_landing_page")
        self.driver.get(self.baseURL + "lp/software-engineering-online/")
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        time.sleep(2)
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_ga_and_gtm_are_present()

    # @pytest.mark.regression
    @pytest.mark.smoke
    def test_005_validate_ga_and_gtm_are_present_on_course_page(self):
        self.logger.info("Test_001_validate_ga_and_gtm_are_present_on_course_page")
        self.driver.get(self.baseURL+"online-courses/customer-experience/")
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        time.sleep(2)
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_ga_and_gtm_are_present()
