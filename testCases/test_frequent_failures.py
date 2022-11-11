import time

import pytest

from pageObjects.BlogPage import BlogPage
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
    # @pytest.mark.smoke
    def test_001_frequent_failures_on_home_page(self):
        self.logger.info("Test_001_frequent_failures_on_home_page")
        self.logger.info("Started Go To Home page")
        self.driver.get(self.baseURL)
        self.homePage = HomePage(self.driver)
        self.homePage.verify_academyxi_logo()
        # self.driver.get("https://the-internet.herokuapp.com/broken_images")
        self.homePage.verify_images_are_not_broken_on_home_page()
        # self.basePage = BasePage(self.driver)
        # self.basePage.verify_image_is_not_broken_in_failed_case()
        # self.basePage.verify_images_are_not_broken()

    @pytest.hookimpl(hookwrapper=True)
    @pytest.mark.smoke
    def test_002_frequent_failures_on_blog_page(self):
        self.logger.info("Test_002_frequent_failures_on_blog_page")
        self.logger.info("Started Go To Blog page")
        self.driver.get("https://academyxi.com/blogs/")
        self.blogPage = BlogPage(self.driver)
        self.blogPage.verify_articles_amount()
        self.driver.close()

