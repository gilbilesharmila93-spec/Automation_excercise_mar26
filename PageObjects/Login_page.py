from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_page:
    email_address="//input[@type='email']"
    password="//input[@type='password']"
    login_click="//button[@type='submit']"
    click_menu_xpath="//a[contains(text(),'Logged in as')]"
    click_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.wait = WebDriverWait(driver,10,0.5)
        self.driver = driver

    def enter_email_address(self, Email):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.email_address)))
        self.driver.find_element(By.XPATH,self.email_address).send_keys(Email)

    def enter_password(self, Password):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.password)))
        self.driver.find_element(By.XPATH,self.password).send_keys(Password)

    def click_login(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.login_click)))
        self.driver.find_element(By.XPATH,self.login_click).click()

    def click_menu(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.click_menu_xpath)))
        self.driver.find_element(By.XPATH, self.click_menu_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.click_logout_xpath).click()

    def verify_login(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.click_menu_xpath)))
            return "login_pass"
        except:
            return "login_fail"














