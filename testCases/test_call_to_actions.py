import time

import pytest

from pageObjects.BuyNowPage import BuyNowPage
from pageObjects.HomePage import HomePage
from pageObjects.LandingPage import LandingPage
from pageObjects.OnlineCoursesPage import OnlineCoursesPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from wrapper.BasePage import BasePage


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class Test_001_Call_To_Actions:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL("baseURL")

    # @pytest.mark.smoke
    def test_001_call_to_actions_on_home_page(self):
        self.logger.info("Test_001_call_to_actions_on_home_page")
        self.logger.info("Started Go To Home page")
        self.driver.get(self.baseURL)
        self.homePage = HomePage(self.driver)
        self.homePage.verify_presence_of_ctas_on_home_page()
        self.homePage.verify_color_of_ctas_on_home_page()
        self.homePage.verify_working_link_of_ctas_on_home_page()

    # @pytest.mark.smoke
    def test_002_call_to_actions_on_online_courses_page(self):
        self.logger.info("Test_001_call_to_actions_on_online_courses_page")
        self.logger.info("Started Go To Online Course Page")
        self.driver.get("https://academyxi.com/online-courses/")
        self.onlineCoursesPage = OnlineCoursesPage(self.driver)
        time.sleep(30)
        self.onlineCoursesPage.verify_presence_of_ctas_on_online_courses_page()
        self.onlineCoursesPage.verify_color_of_ctas_on_online_courses_page()
        self.onlineCoursesPage.verify_working_link_of_ctas_on_online_courses_page()

    # @pytest.mark.smoke
    def test_003_call_to_actions_on_buy_now_page(self):
        self.logger.info("Test_001_call_to_actions_on_buy_now_page")
        self.logger.info("Started Go To Buy Now Page")
        self.driver.get("https://academyxi.com/buy-now/")
        self.buyNowPage = BuyNowPage(self.driver)
        self.buyNowPage.verify_presence_of_ctas_on_buy_now_page()
        self.buyNowPage.verify_color_of_ctas_on_buy_now_page()
        self.buyNowPage.verify_working_link_of_ctas_on_buy_now_page()

    # @pytest.mark.smoke
    def test_004_call_to_actions_on_landing_page(self):
        self.logger.info("Test_001_call_to_actions_on_landing_page")
        self.logger.info("Started Go To Landing Page")
        self.driver.get("https://academyxi.com/lp/software-engineering-online/")
        self.basePage = BasePage(self.driver)
        self.landingPage = LandingPage(self.driver)
        self.basePage.scroll_down_to_bottom()
        self.landingPage.verify_presence_of_ctas_on_landing_page()
        self.landingPage.verify_color_of_ctas_on_landing_page()
        self.landingPage.verify_working_link_of_ctas_on_landing_page()