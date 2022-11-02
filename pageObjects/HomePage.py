import time
from telnetlib import EC

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class HomePage(BasePage):

    enroll_a_course_button_xpath = "//div[@data-element_type='widget'][5]//span[text()='Enrol in a course' and contains(@class,'text-empty')]"
    enroll_first_course = "//a[@data-courseid='2463']"
    close_chat_box_button_css_selector = "//button[@aria-label='Minimize window']"
    download_iframe= "//iframe[contains(@src, 'is_show_course_price=1')]"
    a_with_text = "//a[text()='{}']"
    enroll_course_xpath = "//div[@data-name-courses='{}']/div[@class='right-content']//a[text()='Enrol now']"
    download_course_guide_xpath = "//div[@data-name-courses='Customer Experience']/div[@class='right-content']//a[text()='Download course guide']"
    firstname_xpath = "//input[@placeholder='First Name *']"
    lastname_xpath = "//input[@placeholder='Last Name *']"
    phone_number_id = "number-phone"
    email_xpath = "//p[contains(@class, 'form_phone')]//following-sibling::p//input[@placeholder='Email *']"
    i_am_over_18_xpath = "//label[text()='I am over 18']//preceding-sibling::input"
    download_button_xpath = "//input[@value='Download course guide']"
    software_engineer_transform_course_xpath ="//img[contains(@srcset, 'https://academyxi.com/wp-content/uploads/2020/12/Screen-Shot-2020-12-23-at-2.23.54-pm-338x480.png')]"
    courses_for_individual = "//a[text()='{}']//parent::div//img"
    images_in_for_individuals_tab = "//img[@alt='{}']"
    span_with_text = "//span[text()='{}']"
    link_video_images = "//a[@class= 'link-video']//img"
    academyxi_logo = "//a[@aria-label='Logo']"
    h2_with_text = "//h2[text()='{}']"
    h3_with_text = "//h3[text()='{}']"
    p_contains_class = "//p[contains(@class, '{}')]//select"
    options_in_dropdown = "//p[contains(@class, '{}')]//option[text()='{}']"


    def __init__(self, driver):
        self.driver = driver
        self.element_by_finder = ElementByLocator()

    def click_enroll_a_course_button(self):
         self.click_element(self.enroll_a_course_button_xpath)

    def click_enroll_first_course(self):
        self.wait_element_presence(self.enroll_first_course)
        self.click_element(self.enroll_first_course)

    def click_page_number(self, num):
        self.wait_element_presence(self.a_with_text.format(num))
        self.click_element_by_js(self.a_with_text.format(num))

    def enroll_a_specific_course(self, name):
        self.driver.execute_script("window.scrollTo(0, -(document.body.scrollHeight));")
        element = self.driver.find_element(By.XPATH, "//h3[text()='Filter by:']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element_by_js(self.enroll_course_xpath.format(name))

    def download_course_guide(self, firstname, lastname, phone, email, discipline, reason):
        self.scroll_into_locator("//a[text()='3']")
        self.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(20, 20).click().perform()
        self.switch_to_iframe(self.download_iframe)
        self.input_text(self.firstname_xpath, firstname)
        self.input_text(self.lastname_xpath, lastname)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.phone_number_id))).send_keys(phone)
        self.scroll_into_locator("//p[contains(@class,'Study_Motivation')]")
        self.click_element(self.options_in_dropdown.format('Discipline', discipline))
        self.click_element(self.options_in_dropdown.format('Study_Motivation', reason))
        self.input_text(self.email_xpath, email)
        self.click_element_by_js(self.i_am_over_18_xpath)
        self.wait_for_page_load()
        self.click_element_by_js(self.download_button_xpath)
        time.sleep(10)

    def verify_locator_css_value(self, property, expected_value):
        self.verify_css_property(self.software_engineer_transform_course_xpath, property, expected_value)

    def verify_presence_of_ctas_on_home_page(self):
        self.element_should_be_present(self.enroll_a_course_button_xpath)
        self.element_should_be_present(self.a_with_text.format("Courses for individuals"))
        self.element_should_be_present(self.a_with_text.format("Training for teams"))
        self.element_should_be_present(self.a_with_text.format("Talent & recruitment "))

    def verify_color_of_ctas_on_home_page(self):
        time.sleep(3)
        self.verify_css_property(self.enroll_a_course_button_xpath, "background-color", "rgba(0, 0, 0, 0)")
        self.verify_css_property(self.enroll_a_course_button_xpath, "color", "rgba(255, 255, 255, 1)")
        self.verify_css_property(self.a_with_text.format("Courses for individuals"), "background-color", "rgba(0, 0, 0, 0)")
        self.verify_css_property(self.a_with_text.format("Courses for individuals"), "color", "rgba(18, 30, 77, 1)")
        self.verify_css_property(self.a_with_text.format("Training for teams"), "background-color", "rgba(0, 0, 0, 0)")
        self.verify_css_property(self.a_with_text.format("Training for teams"), "color", "rgba(18, 30, 77, 1)")
        self.verify_css_property(self.a_with_text.format("Talent & recruitment "), "background-color", "rgba(0, 0, 0, 0)")
        self.verify_css_property(self.a_with_text.format("Talent & recruitment "), "color", "rgba(18, 30, 77, 1)")
    def verify_working_link_of_ctas_on_home_page(self):
        self.verify_working_link("//a[@href = 'https://academyxi.com/buy-now/']")
        self.verify_working_link(self.a_with_text.format("Courses for individuals"))
        self.verify_working_link(self.a_with_text.format("Training for teams"))
        self.verify_working_link(self.a_with_text.format("Courses for individuals"))








