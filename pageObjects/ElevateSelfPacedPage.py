import json
import time

from selenium.webdriver.common.by import By

from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class ElevateSelfPacedPage(BasePage):

    a_with_text = "//a[text() =\"{}\"]"
    div_with_id = "//div[@id='panel-header-6572']"
    p_span_contains_text = "//p//span[contains(text(),\"{}\")]"
    li_span_contains_text = "//li//span[contains(text(),\"{}\")]"
    expand_collapse_icon = "(//a[contains(text(),'MODULE')]//preceding-sibling::span[@class ='panel-icon'])['{}']"
    accordion_content ="(//a[@class='panel-title']//parent::div//following-sibling::div//p)[{}]"
    panel_icon ="(//a[@class='panel-title']//following-sibling::div)[{}]"
    accordion_sub_content = "//p[contains(text(), '{}')]//following-sibling::ul//span"

    def __init__(self,driver):
        self.driver=driver
        self.element_by_finder = ElementByLocator()

    def verify_accordions(self):
        file = open("TestData/accordion.json", "r")
        data = file.read()
        file.close()
        obj = json.loads(data)
        self.scroll_into_locator(self.a_with_text.format(obj['accordion'][0]["module"]))
        self.logger.info("Verify accordions are displayed")
        for i in range(len(obj['accordion'])):
            self.click_element_by_js(self.expand_collapse_icon.format(obj['accordion'][i]["module"]))
            self.element_should_be_present(self.a_with_text.format(obj['accordion'][i]["module"]))
            self.element_should_be_present(self.p_span_contains_text.format(obj['accordion'][i]["title"]))
            self.element_should_be_present(self.li_span_contains_text.format(obj['accordion'][i]["item1"]))
            self.element_should_be_present(self.li_span_contains_text.format(obj['accordion'][i]["item2"]))
            self.element_should_be_present(self.li_span_contains_text.format(obj['accordion'][i]["item3"]))
            if obj['accordion'][i]["item4"] != "":
                self.element_should_be_present(self.li_span_contains_text.format(obj['accordion'][i]["item4"]))
            if obj['accordion'][i]["item5"] != "":
                    self.element_should_be_present(self.li_span_contains_text.format(obj['accordion'][i]["item5"]))

    def verify_accordions_2(self):
        self.logger.info("Verify accordions are present")
        self.scroll_into_locator(self.panel_icon.format("1"))
        time.sleep(2)
        module_list = self.driver.find_elements(By.XPATH, "//a[@class='panel-title']")
        content_value_list =[]
        sub_content_list=[]
        for module in module_list:
            module_number = module_list.index(module)+1
            module_value = module.text
            self.click_element_by_js(self.panel_icon.format(module_number))
            if module_value != "":
                self.logger.info("{} is present".format(module_value))
            else:
                self.logger.info("{} is not present".format(module_value))
            assert module_value != ""
            content_list = self.driver.find_elements(By.XPATH, self.accordion_content.format(module_number))
            for content in content_list:
                content_value = self.driver.execute_script('return arguments[0].firstChild.textContent;',content)
                if content_value != "":
                    self.logger.info("{} is present".format(content_value))
                else:
                    self.logger.info("{} is not present".format(content_value))
                assert content_value != ""
                content_value_list.append(content_value)
            self.scroll_into_locator(self.panel_icon.format(module_number))
            for content_value in content_value_list:
                sub_content_list = self.driver.find_elements(By.XPATH, self.accordion_sub_content.format(content_value))
            for sub_content in sub_content_list:
                sub_content_value = self.driver.execute_script('return arguments[0].firstChild.textContent;',sub_content)
                if sub_content_value != "":
                    self.logger.info("{} is present".format(sub_content_value))
                else:
                    self.logger.info("{} is not present".format(sub_content_value))





