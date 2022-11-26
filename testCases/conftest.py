import datetime
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    global driver
    options = Options()
    options.headless = True
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--user-agent=Chrome/77")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-shm-using")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu") 
    options.add_argument("--remote-debugging-port=9222")
    options.set_capability("loggingPrefs", {'performance': 'ALL'})
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #driver = webdriver.Chrome(executable_path="/var/lib/jenkins/axi_website_tests/chromedriver", options=options, desired_capabilities=capabilities)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Academyxi Web'
    config._metadata['Module Name'] = 'Verify Academyxi Web'
    config._metadata['Tester'] = 'Binh'

# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# It is hook for take screenshot and add to HTML Report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        link = driver.current_url
        extra.append(pytest_html.extras.url(link))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:350px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra
