
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
