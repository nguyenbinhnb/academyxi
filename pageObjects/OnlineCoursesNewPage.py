from selenium.webdriver import ActionChains

from wrapper.BasePage import BasePage


class OnlineCoursesNewPage(BasePage):

    learn_more_button = "//div[contains(@class, 'list-entry-col')]//div[contains(@class, 'content-bottom')]//a[@href='{}']"

    def __init__(self,driver):
        self.driver=driver


    def click_learn_more_button(self, course):
        self.scroll_into_locator(self.learn_more_button.format(course))
        self.click_element_by_js(self.learn_more_button.format(course))

