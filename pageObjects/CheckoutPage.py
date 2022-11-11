from telnetlib import EC

from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen


class CheckoutPage:

    logger = LogGen.loggen()
    textbox_firstname_id = "billing_first_name"
    textbox_lastname_id = "billing_last_name"
    street_address_css_selector = "input[name*='billing_address']"
    phone_id = "billing_phone"
    email_address_id = "billing_email"
    dob_date_css_selector = "span[aria-labelledby*='select2-billing_day-container']"
    dob_month_id ="billing_month_field"
    dob_year_css_selector = "span[aria-labelledby*='select2-billing_year-container']"
    input_textbox_class_name = "select2-search__field"
    h2_text_xpath = "//h2[text()='{}']"
    li_text_xpath ="//li[text()='{}']"
    next_button_id = "continue"


    def __init__(self,driver):
        self.driver=driver

    def set_first_name(self, firstname):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.ID,self.textbox_firstname_id))).clear()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, self.textbox_firstname_id))).send_keys(firstname)

    def set_last_name(self, lastname):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.textbox_lastname_id))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.textbox_lastname_id))).send_keys(lastname)

    def set_street_address(self, address):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.street_address_css_selector))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.street_address_css_selector))).send_keys(address)

    def set_phone(self, phone):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.phone_id))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.phone_id))).send_keys(phone)

    def set_email_address(self, email):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.email_address_id))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.email_address_id))).send_keys(email)

    def set_date(self, date):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.dob_date_css_selector))).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.input_textbox_class_name))).send_keys(date)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.li_text_xpath.format(date)))).click()


    def set_month(self, month):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.dob_month_id))).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.input_textbox_class_name))).send_keys(month)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.li_text_xpath.format(month)))).click()

    def set_year(self, year):
        element = self.driver.find_element(By.ID,'billing_phone')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.dob_year_css_selector))).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.input_textbox_class_name))).send_keys(year)
        WebDriverWait(self.driver, 20) .until(
            EC.visibility_of_element_located((By.XPATH, self.li_text_xpath.format(year)))).click()




