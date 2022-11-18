import time

import pytest

from pageObjects.OnlineCoursesNewPage import OnlineCoursesNewPage
from pageObjects.UXUIDesignNewPage import UXUIDesignNewPage
from wrapper.BasePage import BasePage
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from wrapper.elementfinder import ElementByLocator


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class Test_001_validate_online_enrolment_flow:
    baseURL = ReadConfig.getApplicationURL("baseURL")
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_001_validate_online_enrolment_flow(self):
        self.logger.info("Test_001_validate_online_enrolment_flow")
        self.logger.info("Started Enrol Course")
        self.driver.get("https://uat.academyxi.com/")
        self.homePage = HomePage(self.driver)
        self.basePage = BasePage(self.driver)
        self.homePage.click_view_all_courses("https://uat.academyxi.com/online-courses-new/")
        self.onlineCoursesNewPage = OnlineCoursesNewPage(self.driver)
        self.onlineCoursesNewPage.click_learn_more_button("/online-courses/software-engineering-new/")
        time.sleep(3)
        self.uxuiDesignNewPage = UXUIDesignNewPage(self.driver)
        self.uxuiDesignNewPage.click_enrol_now_button("2")
        time.sleep(3)
        self.checkoutPage = CheckoutPage(self.driver)
        self.checkoutPage.fill_in_details_for_checkout()
        self.checkoutPage.verify_payment_options()
        self.checkoutPage.choose_payment_option("1")
        self.checkoutPage.verify_payment_summary()
        self.checkoutPage.fill_in_details_for_payment_and_submit()
        self.checkoutPage.verify_that_enrolment_is_confirmed()




