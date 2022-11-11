import time

import requests
from selenium.webdriver.common.by import By

from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class ThankYouPage(BasePage):
    pdf_files = "//a[contains(@href, '.pdf')]"

    def __init__(self,driver):
        self.driver=driver
        self.element_by_finder = ElementByLocator()

    def verify_course_guide_pdf_files(self):
        try:
           pdf_list = self.driver.find_elements(By.XPATH, self.pdf_files)
           response_code_list = []
           for pdf in pdf_list:
               time.sleep(2)
               response = requests.get(pdf.get_attribute('href'), stream=True)
               response_code = response.status_code
               response_code_list.append(response_code)
               if response_code == 404:
                   self.logger.info(pdf.get_attribute('href') + " is broken")
               else:
                   self.logger.info(pdf.get_attribute('href') + " is not broken")
           assert 404 not in response_code_list
        except requests.exceptions.MissingSchema:
           print("Encountered MissingSchema Exception")
        except requests.exceptions.InvalidSchema:
            print("Encountered InvalidSchema Exception")

    download_pdf_button_xpath = "//a[contains(@href, 'SE-OT-Course-Guide.pdf')]//span[text()= 'Course guide']"