from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class BuyNowPage(BasePage):

    download_course_guide_button = "(//div[@class='wrapper-button'])[1]//a[text()='Download course guide']"
    enrol_now_button = "(//div[@class='wrapper-button'])[1]//a[text()='Enrol now']"

    def __init__(self,driver):
        self.driver=driver
        self.element_by_finder = ElementByLocator()

    def verify_presence_of_ctas_on_buy_now_page(self):
        self.element_should_be_present(self.download_course_guide_button)
        self.element_should_be_present(self.enrol_now_button)

    def verify_color_of_ctas_on_buy_now_page(self):
        try:
            self.driver.find_elements(By.XPATH, self.download_course_guide_button)
            self.verify_css_property(self.download_course_guide_button, "background-color", "rgba(255, 255, 255, 1)")
            self.verify_css_property(self.download_course_guide_button, "color", "rgba(18, 30, 77, 1)")
        except StaleElementReferenceException:
            pass
        self.verify_css_property(self.enrol_now_button, "background-color", "rgba(18, 30, 77, 1)")
        self.verify_css_property(self.enrol_now_button, "color", "rgba(255, 255, 255, 1)")

    def verify_working_link_of_ctas_on_buy_now_page(self):
        self.verify_working_link(self.download_course_guide_button)
        self.verify_working_link(self.enrol_now_button)

    def click_on_download_button_of_any_course(self):
        self.click_element_by_js(self.download_course_guide_button)
