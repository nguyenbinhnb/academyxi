import time
from telnetlib import EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePage):

    enroll_a_course_button_xpath = "//div[@data-element_type='widget'][5]//span[text()='Enrol in a course' and contains(@class,'text-empty')]"
    enroll_first_course_css_selector = "a[data-discipline*='Data Analytics Pro']"
    close_chat_box_button_css_selector = "//button[@aria-label='Minimize window']"
    download_iframe_xpath = "//iframe[contains(@src, 'is_show_course_price=1')]"
    page_number_xpath = "//a[text()='{}']"
    enroll_course_xpath = "//div[@data-name-courses='{}']/div[@class='right-content']//a[text()='Enrol now']"
    download_course_guide_xpath = "//div[@data-name-courses='Customer Experience']/div[@class='right-content']//a[text()='Download course guide']"
    firstname_xpath = "//input[@placeholder='First Name *']"
    lastname_xpath = "//input[@placeholder='Last Name *']"
    phone_number_id = "number-phone"
    email_xpath = "//p[contains(@class, 'form_phone')]//following-sibling::p//input[@placeholder='Email *']"
    dropdown_xpath = "//select[@class = 'select']//option[text()='{}']"
    i_am_over_18_xpath = "//label[text()='I am over 18']//preceding-sibling::input"
    download_button_xpath = "//input[@value='Download']"
    software_engineer_transform_course_xpath ="//img[contains(@srcset, 'https://academyxi.com/wp-content/uploads/2020/12/Screen-Shot-2020-12-23-at-2.23.54-pm-338x480.png')]"
    courses_for_individual = "//a[text()='{}']//parent::div//img"


    def __init__(self, driver):
        self.driver = driver
        self.element_by_finder = ElementByLocator()

    def click_enroll_a_course_button(self):
         self.click_element(self.enroll_a_course_button_xpath)

    def click_enroll_first_course(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.enroll_first_course_css_selector)
        self.driver.execute_script("arguments[0].click();", element)

    def clickPageNumber(self, num):
        self.click_element(self.page_number_xpath.format(num))

    def enrollASpecificCourse(self, name):
        self.driver.execute_script("window.scrollTo(0, -(document.body.scrollHeight));")
        element = self.driver.find_element(By.XPATH, "//h3[text()='Filter by:']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element_by_js(self.enroll_course_xpath.format(name))

    def download_course_guide(self, firstname, lastname, phone, email, discipline, reason):
        element = self.driver.find_element(By.XPATH, "//a[text()='3']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH,self.download_iframe_xpath)))
        self.input_text(self.firstname_xpath, firstname)
        self.input_text(self.lastname_xpath, lastname)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.phone_number_id))).send_keys(phone)
        self.input_text(self.email_xpath, email)
        self.click_element(self.dropdown_xpath.format('Discipline *'))
        self.click_element(self.dropdown_xpath.format(discipline))
        self.click_element(self.dropdown_xpath.format('Why are you looking to study?'))
        self.click_element(self.dropdown_xpath.format(reason))
        self.click_element_by_js(self.i_am_over_18_xpath)
        self.click_element_by_js(self.download_button_xpath)

    def verify_locator_css_value(self, property, expected_value):
        self.verify_css_property(self.software_engineer_transform_course_xpath, property, expected_value)

    def verify_images_are_not_broken_on_home_page(self):
        self.verify_image_is_not_broken(self.courses_for_individual.format("Courses for individuals"))
        self.verify_image_is_not_broken(self.courses_for_individual.format("Training for teams"))
        self.verify_image_is_not_broken(self.courses_for_individual.format("Talent & recruitment "))






