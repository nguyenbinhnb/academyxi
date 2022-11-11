from selenium.webdriver.common.by import By


class ElementFinder(object):

    def __init__(self):
        strategies = {
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'link': self._find_by_link_text,
            'partial link': self._find_by_partial_link_text,
            'css': self._find_by_css_selector,
            'tag_name': self._find_by_tag_name,
            'class_name': self._find_by_class_name,
            'default': self._find_by_default
        }
        self._strategies = strategies
        self._default_strategies = list(strategies.keys())

    def find(self, driver, locator):
        assert driver is not None
        assert locator is not None and len(locator) > 0

        (prefix, criteria) = self._parse_locator(locator)
        prefix = 'default' if prefix is None else prefix
        strategy = self._strategies.get(prefix)
        if strategy is None:
            raise ValueError("Element locator with prefix '" + prefix + "' is not supported")
        return strategy(driver, criteria)

    def _parse_locator(self, locator):
        prefix = None
        criteria = locator
        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0]
                criteria = locator_parts[2].strip()
        return prefix, criteria

    def _find_by_id(self, driver, criteria):
        return driver.find_element(by=By.ID, value=criteria)

    def _find_by_name(self, driver, criteria):
        return driver.find_element(by=By.NAME, value=criteria)

    def _find_by_xpath(self, driver, criteria):
        return driver.find_element(by=By.XPATH, value=criteria)

    def _find_by_link_text(self, driver, criteria):
        return driver.find_element(by=By.LINK_TEXT, value=criteria)

    def _find_by_partial_link_text(self, driver, criteria):
        return driver.find_element(by=By.PARTIAL_LINK_TEXT, value=criteria)

    def _find_by_css_selector(self, driver, criteria):
        return driver.find_element(by=By.CSS_SELECTOR, value=criteria)

    def _find_by_tag_name(self, driver, criteria):
        return driver.find_element(by=By.TAG_NAME, value=criteria)

    def _find_by_class_name(self, driver, criteria):
        return driver.find_element(by=By.CLASS_NAME, value=criteria)

    def _find_by_default(self, driver, criteria):
        if criteria.startswith('//'):
            return driver.find_element(by=By.XPATH, value=criteria)


class ElementsFinder(object):

    def __init__(self):
        strategies = {
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'link': self._find_by_link_text,
            'partial link': self._find_by_partial_link_text,
            'css': self._find_by_css_selector,
            'tag_name': self._find_by_tag_name,
            'class_name': self._find_by_class_name,
            'default': self._find_by_default
        }
        self._strategies = strategies
        self._default_strategies = list(strategies.keys())

    def find(self, driver, locator):
        assert driver is not None
        assert locator is not None and len(locator) > 0

        (prefix, criteria) = self._parse_locator(locator)
        prefix = 'default' if prefix is None else prefix
        strategy = self._strategies.get(prefix)
        if strategy is None:
            raise ValueError("Element locator with prefix '" + prefix + "' is not supported")
        return strategy(driver, criteria)

    def _parse_locator(self, locator):
        prefix = None
        criteria = locator
        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0]
                criteria = locator_parts[2].strip()
        return prefix, criteria

    def _find_by_id(self, driver, criteria):
        return driver.find_elements(by=By.ID, value=criteria)

    def _find_by_name(self, driver, criteria):
        return driver.find_elements(by=By.NAME, value=criteria)

    def _find_by_xpath(self, driver, criteria):
        return driver.find_elements(by=By.XPATH, value=criteria)

    def _find_by_link_text(self, driver, criteria):
        return driver.find_elements(by=By.LINK_TEXT, value=criteria)

    def _find_by_partial_link_text(self, driver, criteria):
        return driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=criteria)

    def _find_by_css_selector(self, driver, criteria):
        return driver.find_elements(by=By.CSS_SELECTOR, value=criteria)

    def _find_by_tag_name(self, driver, criteria):
        return driver.find_elements(by=By.TAG_NAME, value=criteria)

    def _find_by_class_name(self, driver, criteria):
        return driver.find_elements(by=By.CLASS_NAME, value=criteria)

    def _find_by_default(self, driver, criteria):
        if criteria.startswith('//'):
            return driver.find_elements(by=By.XPATH, value=criteria)


class ElementByLocator(object):

    def __init__(self):
        strategies = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'link': By.LINK_TEXT,
            'partial link': By.PARTIAL_LINK_TEXT,
            'css': By.CSS_SELECTOR,
            'tag_name': By.TAG_NAME,
            'class_name': By.CLASS_NAME,
            'default': By.XPATH
        }
        self._strategies = strategies
        self._default_strategies = list(strategies.keys())

    def by_locator(self, locator):
        assert locator is not None and len(locator) > 0

        (prefix, criteria) = self._parse_locator(locator)
        prefix = 'default' if prefix is None else prefix
        strategy = self._strategies.get(prefix)
        if strategy is None:
            raise ValueError("Element locator with prefix '" + prefix + "' is not supported")
        return strategy, criteria

    def _parse_locator(self, locator):
        prefix = None
        criteria = locator
        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0]
                criteria = locator_parts[2].strip()
        return prefix, criteria
