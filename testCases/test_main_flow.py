import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.ThankYouPage import ThankYouPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from wrapper.BasePage import BasePage


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class Test_001_Demo:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.smoke
    def test_001_download_course_guide(self):
        self.logger.info("Test_001_main_flow")
        self.logger.info("Started Go To Home page")
        self.driver.get(self.baseURL)
        self.basePage = BasePage(self.driver)
        self.basePage.verify_text_element_should_be_displayed('a','Discover your  learning path')
        self.basePage.verify_text_element_should_be_displayed('a', 'Upskill your organisation')
        self.homePage = HomePage(self.driver)
        self.homePage.click_enroll_a_course_button()
        self.basePage.verify_text_element_should_be_displayed('span', 'Academy Xi’s expert-led courses and workshops are designed to help you learn, practice and embed new knowledge, preparing you to shape your career and change the world.')
        self.basePage.verify_course_item_should_be_displayed('Data Analytics Pro')
        self.homePage.clickPageNumber('2')
        self.homePage.download_course_guide('aXi Tes', 'Sanest', '355664455', 'testing@gmail.com','React', 'Change or start a new career')
        self.basePage.verify_user_redirect_to_correct_location('https://academyxi.com/online-courses/software-engineering/course-guide/thank-you/')
        self.thankYouPage = ThankYouPage(self.driver)
        self.thankYouPage.verify_course_guide_pdf_file("Software Engineering Transform",
                                                       "SE-OT-Course-Guide.pdf",
                                                       "https://academyxi.com/wp-content/uploads/2022/02/SE-OT-Course-Guide.pdf")
        self.thankYouPage.verify_course_guide_pdf_file("Front-End Web Development Transform",
                                                       "React-Course-Guide.pdf",
                                                       "https://academyxi.com/wp-content/uploads/2022/09/React-Course-Guide.pdf")
        self.thankYouPage.verify_course_guide_pdf_file("Front-End Web Development Elevate",
                                                  "FE-Course-Guide.pdf",
                                                  "https://courseguides.academyxi.com/2021/04/07172345/FE-Course-Guide.pdf")
        self.thankYouPage.verify_course_guide_pdf_file("React Elevate",
                                                       "React-Course-Guide.pdf",
                                                       "https://academyxi.com/wp-content/uploads/2022/09/React-Course-Guide.pdf")
        # self.driver.close()


