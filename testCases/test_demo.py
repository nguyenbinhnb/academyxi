import time

import pytest
from selenium.webdriver import ActionChains

from wrapper.BasePage import BasePage
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_001_Demo:
    baseURL = ReadConfig.getApplicationURL("baseURL")
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    # @pytest.mark.regression
    @pytest.mark.smoke
    def test_001_enroll_course(self):
        self.logger.info("Test_001_enroll_course")
        self.logger.info("Started Enroll Course")
        self.driver.get(self.baseURL)
        self.homePage = HomePage(self.driver)
        self.basePage = BasePage(self.driver)
        self.homePage.click_enroll_a_course_button()
        ActionChains(self.driver).move_by_offset(20, 20).click().perform()
        time.sleep(20)
        self.homePage.click_enroll_first_course()
        time.sleep(20)
        self.basePage.verify_text_element_should_be_displayed('h2', 'Enrol With Us')
        self.checkoutPage = CheckoutPage(self.driver)
        self.checkoutPage.set_first_name('Sandbox')
        self.checkoutPage.set_last_name('Axi Testing')
        self.checkoutPage.set_street_address('hanoi 123')
        self.checkoutPage.set_phone('0355665555')
        self.checkoutPage.set_email_address('test@gmail.com')
        self.checkoutPage.set_date('11')
        self.checkoutPage.close_chat_box()
        self.checkoutPage.set_month('12')
        self.checkoutPage.set_year('1999')


