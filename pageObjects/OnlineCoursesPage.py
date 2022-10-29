import time

from selenium.webdriver import ActionChains
from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class OnlineCoursesPage(BasePage):

    download_course_guide_button = "//div[@id='axi-navmenu-aside-global']//a[text()= 'Download course guide']"
    enrol_now_button = "//div[@id='axi-navmenu-aside-global']//a[text()='Enrol now']"
    learn_more_button = "//div[@data-page ='1'][1]//a[text()='Learn More']"
    h1_with_text = "//h1[text()='{}']"

    def __init__(self,driver):
        self.driver=driver
        self.element_by_finder = ElementByLocator()

    def verify_presence_of_ctas_on_online_courses_page(self):
        self.scroll_down_to_bottom()
        self.scroll_down_to_top()
        ActionChains(self.driver).move_by_offset(20, 20).click().perform()
        self.is_present(self.download_course_guide_button)
        self.is_present(self.enrol_now_button)
        self.is_present(self.learn_more_button)

    def verify_color_of_ctas_on_online_courses_page(self):
        time.sleep(3)
        self.verify_css_property(self.download_course_guide_button, "background-color", "rgba(54, 115, 252, 1)")
        self.verify_css_property(self.download_course_guide_button, "color", "rgba(255, 255, 255, 1)")
        self.verify_css_property(self.enrol_now_button, "background-color", "rgba(255, 255, 255, 1)")
        self.verify_css_property(self.enrol_now_button, "color", "rgba(54, 115, 252, 1)")
        self.verify_css_property(self.learn_more_button, "background-color", "rgba(0, 0, 0, 0)")
        self.verify_css_property(self.learn_more_button, "color", "rgba(54, 115, 252, 1)")


    def verify_working_link_of_ctas_on_online_courses_page(self):
        self.verify_working_link(self.download_course_guide_button)
        self.verify_working_link(self.enrol_now_button)
        self.verify_working_link(self.learn_more_button)
