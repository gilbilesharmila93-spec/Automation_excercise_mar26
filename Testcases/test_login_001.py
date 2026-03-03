import pytest
from PageObjects.Login_page import Login_page as Login_page
from Utilities import read_config
from Utilities.read_config import ReadConfig

@pytest.mark.usefixtures("driver_setup")
class Test_login_page_001:
    driver = None
    def test_verify_login_url(self):
        email = ReadConfig.get_email()
        password = ReadConfig.get_password()
        url = ReadConfig.get_login_url()
        self.driver.get(url)
        if self.driver.title == "Automation Exercise - Signup / Login":
           self.driver.save_screenshot("Screenshots\\test_verify_url_pass.png")
        else:
            self.driver.save_screenshot("Screenshots\\test_verify_url_fail.png")


