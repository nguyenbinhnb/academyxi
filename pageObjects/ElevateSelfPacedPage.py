import json

from wrapper.BasePage import BasePage
from wrapper.elementfinder import ElementByLocator


class ElevateSelfPacedPage(BasePage):

    a_with_text = "//a[text() =\"{}\"]"
    div_with_id = "//div[@id='panel-header-6572']"
    p_span_contains_text = "//p//span[contains(text(),\"{}\")]"
    li_span_contains_text = "//li//span[contains(text(),\"{}\")]"
    expand_collapse_icon = "//a[contains(text(),\"{}\")]//preceding-sibling::span[@class ='panel-icon']"

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


