import time

from selenium.webdriver import ActionChains

from wrapper.BasePage import BasePage


class UXUIDesignNewPage(BasePage):
    enrol_button = "(//a[text()='Enrol today'])[{}]"

    def __init__(self, driver):
        self.driver = driver

    def click_enrol_now_button(self, num):
        self.double_click(self.enrol_button.format(num))
        if self.is_present(self.enrol_button.format(num)):
           self.double_click(self.enrol_button.format(num))


