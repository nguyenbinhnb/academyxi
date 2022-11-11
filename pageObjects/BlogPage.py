
from selenium.webdriver.common.by import By

from utilities.customLogger import LogGen
from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class BlogPage(BasePage):
    logger = LogGen.loggen()

    def __init__(self,driver):
        self.driver=driver
        self.element_by_finder = ElementByLocator()

    def verify_articles_amount(self):
         article_list = self.driver.find_elements(By.TAG_NAME, "article")
         assert len(article_list) >= 3
         self.logger.info("There are {} articles on Blog Page".format(len(article_list)))