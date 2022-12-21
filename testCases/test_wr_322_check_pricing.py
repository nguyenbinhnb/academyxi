import time

import pytest
from selenium.webdriver import ActionChains
from wrapper.BasePage import BasePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class TestValidatePricesOnMainPages:
    baseURL = ReadConfig.getApplicationURL("baseURL")
    logger = LogGen.loggen()
    daTransformPartTimeURL = ReadConfig.getApplicationURL("DA Transform Part Time Page")
    uudTransformFullTimeURL = ReadConfig.getApplicationURL("UUD Transform Full Time Page")
    uudTransformPartTimeURL = ReadConfig.getApplicationURL("UUD Transform Part Time Page")
    uudElevateSelfPacedURL = ReadConfig.getApplicationURL("UUD Elevate Self Paced Page")
    daDataAnalyticsSelfPacedElevateURL = ReadConfig.getApplicationURL("DA Analytics Self Paced Elevate Page")
    fewdTransformPartTimeURL = ReadConfig.getApplicationURL("FEWD Transform Part Time Page")
    seTransformFullTimeURL = ReadConfig.getApplicationURL("SE Transform Full Time Page")
    seTransforPartTimeURL = ReadConfig.getApplicationURL("SE Transform Part Time Page")
    gdTransformPartTimeURL = ReadConfig.getApplicationURL("GD Transform Part Time Page")
    gdElevateSelfPacedURL = ReadConfig.getApplicationURL("GD Elevate Self Paced Page")
    csTransforPartTimeURL = ReadConfig.getApplicationURL("CS Transform Part Time Page")
    pmTransformPartTimeURL = ReadConfig.getApplicationURL("PM Transform Part Time Page")
    pmElevateSelfPacedURL = ReadConfig.getApplicationURL("PM Elevate Self Paced Page")
    sdElevateSelfPacedURL = ReadConfig.getApplicationURL("SD Elevate Self Paced Page")
    dtElevateSelfPacedURL = ReadConfig.getApplicationURL("DT Elevate Self Paced Page")
    ceElevateSelfPacedURL = ReadConfig.getApplicationURL("CE Elevate Self Paced Page")
    smmElevateSelfPacedURL = ReadConfig.getApplicationURL("SMM Elevate Self Paced Page")
    dmTransformPartTimeURL = ReadConfig.getApplicationURL("DM Transform Part Time Page")
    dmElevateSelfPacedURL = ReadConfig.getApplicationURL("DM Elevate Self Paced Page")
    dpmElevateSelfPacedURL = ReadConfig.getApplicationURL("DPM Elevate Self Paced Page")


    @pytest.mark.smoke
    def test_001_validate_prices_on_data_analytics_transform_part_time_page(self):
        self.logger.info("Test_001_validate_prices_on_data_analytics_transform_part_time_page")
        self.driver.get(self.daTransformPartTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_002_validate_prices_on_ux_ui_design_transform_full_time_page(self):
        self.logger.info("Test_002_validate_prices_on_ux_ui_design_transform_full_time_page")
        self.driver.get(self.uudTransformFullTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_003_validate_prices_on_ux_ui_design_transform_part_time_page(self):
        self.logger.info("Test_003_validate_prices_on_ux_ui_design_transform_part_time_page")
        self.driver.get(self.uudTransformPartTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_004_validate_prices_on_ux_ui_design_elevate_self_paced_page(self):
        self.logger.info("Test_004_validate_prices_on_ux_ui_design_elevate_self_paced_page")
        self.driver.get(self.uudElevateSelfPacedURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_005_validate_prices_on_data_analytics_self_paced_elevate_page(self):
        self.logger.info("Test_005_validate_prices_on_data_analytics_self_paced_elevate_page")
        self.driver.get(self.daDataAnalyticsSelfPacedElevateURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_006_validate_prices_on_front_end_web_development_transform_part_time_page(self):
        self.logger.info("Test_006_validate_prices_on_front_end_web_development_transform_part_time_page")
        self.driver.get(self.fewdTransformPartTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_007_validate_prices_on_software_engineering_transform_full_time_page(self):
        self.logger.info("Test_007_validate_prices_on_software_engineering_transform_full_time_page")
        self.driver.get(self.seTransformFullTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_008_validate_prices_on_software_engineering_transform_part_time_page(self):
        self.logger.info("Test_008_validate_prices_on_software_engineering_transform_part_time_page")
        self.driver.get(self.seTransforPartTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_009_validate_prices_on_graphic_design_transform_part_time_page(self):
        self.logger.info("Test_009_validate_prices_on_graphic_design_transform_part_time_page")
        self.driver.get(self.gdTransformPartTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_010_validate_prices_on_graphic_design_elevate_self_paced_page(self):
        self.logger.info("Test_010_validate_prices_on_graphic_design_elevate_self_paced_page")
        self.driver.get(self.gdElevateSelfPacedURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_011_validate_prices_on_cyber_security_transform_part_time_page(self):
        self.logger.info("Test_011_validate_prices_on_cyber_security_transform_part_time_page")
        self.driver.get(self.csTransforPartTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_012_validate_prices_on_product_management_transform_part_time_page(self):
        self.logger.info("Test_012_validate_prices_on_product_management_transform_part_time_page")
        self.driver.get(self.pmTransformPartTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_013_validate_prices_on_product_management_elevate_self_paced_page(self):
        self.logger.info("Test_013_validate_prices_on_product_management_elevate_self_paced_page")
        self.driver.get(self.pmElevateSelfPacedURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_014_validate_prices_on_service_design_elevate_self_paced_page(self):
        self.logger.info("Test_014_validate_prices_on_service_design_elevate_self_paced_page")
        self.driver.get(self.sdElevateSelfPacedURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_015_validate_prices_on_design_thinking_elevate_self_paced_page(self):
        self.logger.info("Test_015_validate_prices_on_design_thinking_elevate_self_paced_page")
        self.driver.get(self.dtElevateSelfPacedURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_016_validate_prices_on_customer_experience_elevate_self_paced_page(self):
        self.logger.info("Test_016_validate_prices_on_customer_experience_elevate_self_paced_page")
        self.driver.get(self.ceElevateSelfPacedURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_017_validate_prices_on_social_media_marketing_elevate_self_paced_page(self):
        self.logger.info("Test_017_validate_prices_on_social_media_marketing_elevate_self_paced_page")
        self.driver.get(self.smmElevateSelfPacedURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_018_validate_prices_on_digital_marketing_transform_part_time_page(self):
        self.logger.info("Test_018_validate_prices_on_digital_marketing_transform_part_time_page")
        self.driver.get(self.dmTransformPartTimeURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_019_validate_prices_on_digital_marketing_elevate_self_paced_page(self):
        self.logger.info("Test_019_validate_prices_on_digital_marketing_elevate_self_paced_page")
        self.driver.get(self.dmElevateSelfPacedURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

    @pytest.mark.smoke
    def test_020_validate_prices_on_digital_project_management_elevate_self_paced_page(self):
        self.logger.info("Test_020_validate_prices_on_digital_project_management_elevate_self_paced_page")
        self.driver.get(self.dpmElevateSelfPacedURL)
        self.basePage = BasePage(self.driver)
        self.basePage.wait_for_page_load()
        ActionChains(self.driver).move_by_offset(5, 5).click().perform()
        self.basePage.verify_original_price_and_discounted_price()

