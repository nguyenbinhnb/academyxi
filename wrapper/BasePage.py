import os
import time
from telnetlib import EC
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from packaging.requirements import URL
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from wrapper.elementfinder import ElementByLocator
from utilities.customLogger import LogGen


class BasePage:
    collect_failed_soft_validation_data = []
    col_soft_validation_lect_failed_data = []
    logger = LogGen.loggen()
    tag_with_text_xpath = "//{}[text()='{}']"
    course_name_xpath ="//div[@data-name-courses= '{}']"
    div_contains_class_xpath ="//div[contains(@class, 'pagination-content')]"


    def __init__(self, driver):
        self.driver = driver
        self.element_by_finder = ElementByLocator()
        self.timeout = 60
        self.implicitly_wait = 20

    def click_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.element_by_finder.by_locator(locator))).click()

    def click_element_by_js(self, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator)))
        if element:
            self.logger.info("Element: {} is present in {} sec.".format(locator, timeout))
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, value, timeout=20):
        """
        Input value to specified locator
        :param locator: String locator
        :param value: input value
        :return: self
        """
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.element_by_finder.by_locator(locator))).clear()
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.element_by_finder.by_locator(locator))).send_keys(value)
        return self

    def scroll_into_locator(self, locator):
        """
        this method scrolls into view of associated element located by the locator
        :param locator: Locator which is implemented to identify the element to scroll into view
        """
        self.wait_element_presence(locator)
        location = self.driver.find_element(By.XPATH, locator).location
        self.driver.execute_script("window.scrollTo({}, {});".format(location['x'], location['y']))

    def is_visible(self, locator, timeout=30):
        num = (time.strftime("%Y-%m-%d %H%M%S", time.gmtime()))
        try:
            self.driver.implicitly_wait(30)
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.element_by_finder.by_locator(locator))
            )
            if element:
                self.logger.info("Element '%s' is present." % locator)
                return True
            else:
                 self.driver.save_screenshot(".\\Screenshots\\" + f".test_elementDisplay_{num}.png")
                 print("element is not present")
                 self.logger.info("Element '%s' is not visible." % locator)
            return False
        except TimeoutException:
            self.driver.save_screenshot(".\\Screenshots\\" + f".test_elementDisplay_{num}.png")
            self.logger.warning("Fail to locate Element: {} in {} sec.".format(locator, 20))
            return False
        except WebDriverException as e:
            self.driver.save_screenshot(".\\Screenshots\\" + f".test_elementDisplay_{num}.png")
            self.logger.warning("Received WebDriver Exception for locator: {} in {} sec.".format(locator, 20))
            print(e)
            return False

    def element_should_be_visible(self, locator, message):
        self.logger.info("Verifying element '%s' is present." % locator)
        present = self.is_visible(locator)
        if not present:
            if not message:
                message = "The element '%s' should be present, " \
                          "but it is not present." % locator
            raise AssertionError(message)
        return self

    def verify_text_element_should_be_displayed(self, tag, text):
        self.wait_element_presence(self.tag_with_text_xpath.format(tag, text))
        self.element_should_be_visible(self.tag_with_text_xpath.format(tag, text), "Element is not present")
        return self

    def verify_course_item_should_be_displayed(self, course):
        self.element_should_be_visible(self.course_name_xpath.format(course), "Course is not present")
        return self

    def get_location(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def verify_user_redirect_to_correct_location(self, url):
        self.logger.info("Verify user redirect to correct location")
        time.sleep(20)
        txt_link = self.get_location()
        self.assert_two_values_equal(txt_link, url, 'yes')

    def assert_two_values_equal(self, actual_text, expected_text, hard_validation='no'):
        """
        Assert text value depending on validation condition
        :param actual_text:
        :param expected_text:
        :param hard_validation: Yes or No
        :return: either log or give assertion error
        """
        num = (time.strftime("%Y-%m-%d %H%M%S", time.gmtime()))
        actual_text = str(actual_text)
        expected_text = str(expected_text)
        if hard_validation.lower() == 'no':
            try:
                assert actual_text == expected_text
                self.logger.info("Soft Validation PASSED: Actual: {} and Expected: {}".format(actual_text,
                                                                                              expected_text))
            except AssertionError:
                self.logger.error("Soft Validation FAILED: Actual: {} and Expected: {}".format(actual_text, expected_text))
                self.driver.save_screenshot(".\\Screenshots\\" + f".test_assertTwoValues_{num}.png")
                self.col_soft_validation_lect_failed_data.append(
                    "Soft Validation FAILED: PAGE: {}, Actual: {} and Expected: {}".format(
                        self.get_title(), actual_text, expected_text)
                )

        else:
            assert actual_text == expected_text, \
                "Hard Validation FAILED: Actual: {} and Expected: {}".format(actual_text, expected_text)
            self.logger.info("Hard Validation PASSED: Actual: {} and Expected: {}".format(actual_text, expected_text))
        return actual_text == expected_text

    def verify_css_property(self, locator, property, expected_value):
        self.wait_for_page_load()
        self.scroll_into_locator(locator)
        actual_value = self.driver.find_element(By.XPATH, locator).value_of_css_property(property)
        assert actual_value == expected_value
        self.logger.info("Validation {} Property Passed: Actual: {} and Expected: {}".format(property, actual_value, expected_value))

    def verify_images_are_not_broken(self, locator):
        try:
           self.scroll_into_locator(locator)
           image_list = self.driver.find_elements(By.XPATH, locator)
           response_code_list = []
           for image in image_list:
               time.sleep(2)
               response = requests.get(image.get_attribute('src'), stream=True)
               response_code = response.status_code
               response_code_list.append(response_code)
               # print (response_code_list)
               if response_code == 404:
                   self.logger.info(image.get_attribute('src') + " is broken")
               else:
                   self.logger.info(image.get_attribute('src') + " is not broken")
           assert 404 not in response_code_list
        except requests.exceptions.MissingSchema:
           print("Encountered MissingSchema Exception")
        except requests.exceptions.InvalidSchema:
            print("Encountered InvalidSchema Exception")

    def wait_element_presence(self, locator):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, locator)))
        return self

    def switch_to_iframe(self, locator, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, locator)))

    def is_present(self, locator):
        element = self.driver.find_elements(By.XPATH, locator)
        if len(element):
            self.logger.info("Element {} is present.".format(locator))
            return True
        else:
            print("element is not present")
            self.logger.info("Element {} is not present.".format(locator))
            return False

    def wait_for_page_load(self, timeout=30):
        try:
            old_page = self.driver.find_element(By.XPATH, '//html')
            yield
            WebDriverWait(self, timeout).until(
                EC.staleness_of(old_page)
            )
        except TimeoutException:
            self.logger.info("got timeout exception on wait for page load!!")

    def verify_working_link(self, locator):
        try:
            working_link_list = self.driver.find_elements(By.XPATH, locator)
            response_code_list = []
            for link in working_link_list:
                time.sleep(2)
                response = requests.get(link.get_attribute('href'), stream=True)
                response_code = response.status_code
                response_code_list.append(response_code)
                if response_code == 200:
                    self.logger.info(link.get_attribute('href') + " is present")
                else:
                    self.logger.info(link.get_attribute('href') + " is not broken")
            assert 404 not in response_code_list
        except requests.exceptions.MissingSchema:
            print("Encountered MissingSchema Exception")
        except requests.exceptions.InvalidSchema:
            print("Encountered InvalidSchema Exception")
    def scroll_down_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_down_to_top(self):
        self.driver.execute_script("window.scrollTo(0, -(document.body.scrollHeight));")

    def verify_broken_images(self, url):
        global img
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        response_code_list = []
        imgs = bs.find_all('img')
        try:
            for img in imgs:
                if img.get('src').endswith(('.jpg', '.png', '.webp', 'svg')):
                    response = requests.get(img.get('src'), stream=True)
                    response_code = response.status_code
                    if (response_code == 200):
                       self.logger.info(img.get('src') + " is not broken")
                       response_code_list.append(response_code)
                    else:
                        self.logger.info(img.get('src') + " is broken")
                        response_code_list.append(response_code)
                assert 404 not in response_code_list
        except requests.exceptions.MissingSchema:
            print("Encountered MissingSchema Exception")
        except requests.exceptions.InvalidSchema:
            print("Encountered InvalidSchema Exception")

    def verify_broken_images_failed(self, url):
        global img
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        response_code_list = []
        imgs = bs.find_all('img')
        try:
            for img in imgs:
                if img.get('src').endswith(('.jpg', '.png', '.webp', 'svg')):
                    response = requests.get("https://the-internet.herokuapp.com"+img.get('src'), stream=True)
                    response_code = response.status_code
                    if (response_code == 200):
                       self.logger.info(img.get('src') + " is not broken")
                       response_code_list.append(response_code)
                    else:
                        self.logger.info(img.get('src') + " is broken")
                        response_code_list.append(response_code)
                assert 404 not in response_code_list
        except requests.exceptions.MissingSchema:
            print("Encountered MissingSchema Exception")
        except requests.exceptions.InvalidSchema:
            print("Encountered InvalidSchema Exception")

    def element_should_be_present(self, locator):
        present = self.is_present(locator)
        if not present:
            raise AssertionError()
        return self







