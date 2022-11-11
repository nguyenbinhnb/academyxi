import time

from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class LandingPage(BasePage):

    download_course_guide_button = "//a[text()='Download free course guide']"

    def __init__(self,driver):
        self.driver=driver
        self.element_by_finder = ElementByLocator()

    def verify_presence_of_ctas_on_landing_page(self):
        self.element_should_be_present(self.download_course_guide_button)

    def verify_color_of_ctas_on_landing_page(self):
        time.sleep(3)
        self.verify_css_property(self.download_course_guide_button, "background-color", "rgba(54, 115, 252, 1)")
        self.verify_css_property(self.download_course_guide_button, "color", "rgba(255, 255, 255, 1)")

    def verify_working_link_of_ctas_on_landing_page(self):
        self.verify_working_link(self.download_course_guide_button)

