import allure
import pytest

from PageObjects.Login_page import Login_page as Login_page
from Testcases.conftest import driver_setup
from Utilities import read_config
from Utilities.read_config import ReadConfig
from Utilities.logger import Logger_class

@pytest.mark.usefixtures("driver_setup")

class Test_login_page_001:
    driver = None
    # email = ReadConfig.get_email()
    # password = ReadConfig.get_password()
    url = ReadConfig.get_login_url()
    log = Logger_class.get_logger()

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, rerun_delay=1)
    @pytest.mark.order(1)
    @allure.title("test_verify_login_url_001")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.epic("Epic: Verify Login")
    @allure.description("This testcases is to validate login url")
    @allure.story("AutomationExercise:Verify_login_url")
    def test_verify_login_url_001(self):
        self.driver.get(self.url)
        self.log.info("Started test_verify_login_url verification")
        if self.driver.title == "Automation Exercise - Signup / Login":
           self.driver.save_screenshot("Screenshots\\test_verify_url_pass.png")
           self.log.info("driver title fetched successfully")
        else:
            self.driver.save_screenshot("Screenshots\\test_verify_url_fail.png")
            self.log.info("driver title is not correct")

    @pytest.mark.parametrize("email,password,expected", [
        ("gilbilesharmila93@gmail.com", "s966507.", "login_pass"),  # Positive
        ("gilbilesharmila93@gmail.com", "s966507", "login_fail"),  # Negative
        ("gilbilesharmila@gmail.com", "s966507.", "login_fail"),  # Negative
        ("gilbilesharmila@gmail.com", "s966507", "login_fail"),  # Negative
    ])

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, rerun_delay=1)
    @pytest.mark.order(2)
    @pytest.mark.dependency(name="test_verify_login_url_001")
    def test_verify_login_002(self,email,password,expected):
        self.driver.get(self.url)
        lp=Login_page(self.driver)
        lp.enter_email_address(email)
        lp.enter_password(password)
        self.log.info("Clicking Login Button")
        lp.click_login()
        self.log.info("verifying login")
        actual_result = lp.verify_login()
        if lp.verify_login()=="login_pass":
            self.log.info("logged in successfully")
            self.driver.save_screenshot("Screenshots\\test_verify_login_successfully.png")
            lp.click_logout()
            # assert True

        else:
            self.log.error("login failed ")
            self.driver.save_screenshot("Screenshots\\test_verify_login_failure.png")
            # assert False,"User login failed"


        if actual_result == expected:
            self.log.error("Test case passed ")
        else:
            self.log.error("Test case failed ")

        assert actual_result==expected,f"Login test failed for {email}{password}"

    # def test_verify_registeration(self):



