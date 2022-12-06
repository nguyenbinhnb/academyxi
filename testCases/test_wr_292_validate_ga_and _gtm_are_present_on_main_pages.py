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
    logger = LogGen.loggen()
    customerExperienceDisciplineURL = ReadConfig.getApplicationURL("Customer Experience Discipline Page")
    uxdThankYouURL = ReadConfig.getApplicationURL("UXD Thank You Page")
    checkoutURL = ReadConfig.getApplicationURL("Checkout Page")
    lpSoftwareEngineerOnlineURL = ReadConfig.getApplicationURL("LP Software Engineer Online Page")

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
        self.driver.get(self.checkoutURL)
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
        self.driver.get(self.uxdThankYouURL)
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
        self.driver.get(self.lpSoftwareEngineerOnlineURL)
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
        self.driver.get(self.customerExperienceDisciplineURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        time.sleep(2)
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_ga_and_gtm_are_present()
