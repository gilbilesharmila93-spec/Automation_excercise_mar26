class Login_page:
    login_button = "//a[normalize-space()='Signup / Login']"
    email_address="//input[@data-qa='login-email']"
    password="//input[@placeholder='Password']"
    login_click="//button[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def login_button(self):
        self.driver.get(self.login_button).click()

    def enter_email_address(self, Email):
        self.driver.get(self.email_address).send_keys(Email)

    def enter_password(self, Password):
        self.driver.get(self.password).send_keys(Password)

    def click_login(self):
        self.driver.get(self.login_button).click()














