
from telnetlib import EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class ThankYouPage(BasePage):

    def __init__(self,driver):
        self.driver=driver
        self.element_by_finder = ElementByLocator()

    def verify_course_guide_pdf_file(self,course_name, pdf_file, expected_pdf):
         self.scroll_into_locator("//strong[text()='{}']".format(course_name))
         element = WebDriverWait(self.driver, 20).until(
             EC.presence_of_element_located(self.element_by_finder.by_locator(f"//a[contains(@href, '{pdf_file}')]")))
         actual_pdf = element.get_attribute('href')
         self.assert_two_values_equal(actual_pdf, expected_pdf, 'yes')

    download_pdf_button_xpath = "//a[contains(@href, 'SE-OT-Course-Guide.pdf')]//span[text()= 'Course guide']"