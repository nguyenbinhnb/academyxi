import time

from selenium.webdriver import ActionChains
from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class CoursePage(BasePage):

    download_course_guide_button = "//div[@id='axi-navmenu-aside-global']//a[text()= 'Download course guide']"
    enrol_now_button = "//div[@id='axi-navmenu-aside-global']//a[text()='Enrol now']"
    learn_more_button = "//div[@data-page ='1'][1]//a[text()='Learn More']"
    h1_with_text = "//h1[text()='{}']"

    def __init__(self,driver):
        self.driver=driver
        self.element_by_finder = ElementByLocator()

    def verify_images_are_not_broken_on_course_page(self):
        self.scroll_into_locator("//p[text()='Academy Xi has a 5 score out of 5, rated by 0 students.']")
        self.verify_images_are_not_broken("//div[@class='elementor-image']//img")
        self.scroll_into_locator("//h2[text()='Meet your mentors']")
        self.verify_images_are_not_broken("//div[@class='entry-image']//img")
        self.scroll_down_to_bottom()
        self.verify_images_are_not_broken("//a[@aria-label='Flag']//img")