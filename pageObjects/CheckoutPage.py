import time
from telnetlib import EC

from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen
from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class CheckoutPage(BasePage):
    logger = LogGen.loggen()
    textbox_firstname_id = "billing_first_name"
    textbox_lastname_id = "billing_last_name"
    street_address_css_selector = "input[name*='billing_address']"
    phone_id = "billing_phone"
    email_address_id = "billing_email"
    dob_date_css_selector = "span[aria-labelledby*='select2-billing_day-container']"
    dob_month_id = "billing_month_field"
    dob_year_css_selector = "span[aria-labelledby*='select2-billing_year-container']"
    input_textbox_class_name = "select2-search__field"
    h2_text_xpath = "//h2[text()='{}']"
    li_text_xpath = "//li[text()='{}']"
    next_button = "//input[@id= 'continue']"
    chat_box_iframe = "//iframe[@id='chat-widget']"
    minimize_icon = "//button[@aria-label='Minimize window']"
    term_check_box = "//input[@id= 'chk_term']"
    a_with_class = "//a[@class='{}']"
    span_with_text = "//span[text()='{}']"
    payment_options = "//div[@class='item-product']"
    add_to_cart_button = "(//a[@class='btn-addtocart'])[{}]"
    h3_with_text = "//h3[text()='{}']"
    p_with_text = "//p[text()='{}']"
    td_with_text = "//td[text()='{}']"
    price = "(//td//span[contains(@class,'woocommerce-Price-amount')])[{}]"

    def __init__(self, driver):
        self.driver = driver
        self.element_by_finder = ElementByLocator()

    def set_first_name(self, firstname):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.ID, self.textbox_firstname_id))).clear()
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
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.ID, self.dob_month_id))).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.input_textbox_class_name))).send_keys(month)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.li_text_xpath.format(month)))).click()

    def set_year(self, year):
        element = self.driver.find_element(By.ID, 'billing_phone')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.dob_year_css_selector))).click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.input_textbox_class_name))).send_keys(year)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.li_text_xpath.format(year)))).click()

    def fill_in_details_for_checkout(self):
        self.set_first_name('Sandbox')
        self.set_last_name("Axi Testing")
        self.set_street_address("123 hanoi")
        self.set_phone("923265233")
        self.set_email_address("binh.n@academyxi.com")
        self.set_date("19")
        self.close_chat_box()
        self.scroll_into_locator("//input[@id= 'billing_phone']")
        self.set_month("3")
        self.set_year("1988")
        self.click_element(self.term_check_box)
        drag = self.driver.find_element(By.XPATH, "(//p/span)[26]")
        drop = self.driver.find_element(By.XPATH, "//span[text()='Email: change@academyxi.com']")
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        time.sleep(2)
        self.click_element(self.a_with_class.format('btn_accept'))
        self.click_element(self.next_button)

    def close_chat_box(self):
        if self.is_visible(self.chat_box_iframe, 5):
            self.switch_to_iframe(self.chat_box_iframe)
            self.click_element_by_js(self.minimize_icon)
            self.driver.switch_to.default_content()

    def verify_payment_options(self):
        payment_list = self.driver.find_elements(By.XPATH, self.payment_options)
        assert len(payment_list) >= 2
        self.logger.info("There are {} payment options on Checkout Page".format(len(payment_list)))

    def choose_payment_option(self, num):
        self.click_element_by_js(self.add_to_cart_button.format(num))
        self.click_element_by_js(self.a_with_class.format('btn-review'))

    def verify_payment_summary(self):
        self.element_should_be_present(self.h3_with_text.format("Payment Summary"))
        self.element_should_be_present(self.p_with_text.format('Course total'))
        self.element_should_be_present(self.p_with_text.format('Discount (Pay in full discount)'))
        self.element_should_be_present(self.td_with_text.format('Total AUD (inc. tax)'))
        self.element_should_be_present(self.price.format('1'))
        self.element_should_be_present(self.price.format('2'))
        self.element_should_be_present(self.price.format('3'))
