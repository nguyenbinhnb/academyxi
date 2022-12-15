import time

import pytest
from selenium.webdriver import ActionChains

from pageObjects.BuyNowPage import BuyNowPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from pageObjects.ThankYouPage import ThankYouPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from wrapper.BasePage import BasePage


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class Test_001_Main_Flow:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL("baseURL")

    @pytest.mark.sanity
    # @pytest.mark.regression
    @pytest.mark.smoke
    def test_001_download_course_guide(self):
        self.logger.info("Test_001_main_flow")
        self.logger.info("Started Go To Home page")
        self.driver.get(self.baseURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(20, 20).click().perform()
        self.basePage.verify_text_element_should_be_displayed('a','Discover your  learning path')
        self.basePage.verify_text_element_should_be_displayed('a', 'Upskill your organisation')
        self.homePage = HomePage(self.driver)
        self.homePage.click_enroll_a_course_button()
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()
        self.basePage.verify_course_item_should_be_displayed()
        self.homePage.click_page_number('2')
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()
        self.buyNowPage = BuyNowPage(self.driver)
        self.buyNowPage.click_on_download_button_of_any_course()
        self.checkoutPage = CheckoutPage(self.driver)
        self.homePage.download_course_guide('sandbox', 'sandbox', '082934290', 'testing@gmail.com', 'Change or start a new career')
        self.thankYouPage = ThankYouPage(self.driver)
        self.basePage.wait_for_page_load()
        self.basePage.wait_for_loading_icon_disappear()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_user_redirect_to_correct_location('https://academyxi.com/online-courses/data-analytics/course-guide/thank-you')
        self.thankYouPage.verify_course_guide_pdf_files()



