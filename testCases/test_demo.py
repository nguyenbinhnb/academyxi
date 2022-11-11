import pytest

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
        self.homePage.click_enroll_first_course()
        self.basePage.wait_for_page_load()
        self.basePage.verify_text_element_should_be_displayed('h2', 'Enrol With Us')
        self.checkoutPage = CheckoutPage(self.driver)
        self.checkoutPage.set_first_name('Binh')
        self.checkoutPage.set_last_name('Nguyen')
        self.checkoutPage.set_street_address('hanoi 123')
        self.checkoutPage.set_phone('0355665555')
        self.checkoutPage.set_email_address('test@gmail.com')
        self.checkoutPage.set_date('11')
        self.checkoutPage.set_month('12')
        self.checkoutPage.set_year('1999')


