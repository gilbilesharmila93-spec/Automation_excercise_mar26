import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_email():
        return config.get("login", "email")

    @staticmethod
    def get_password():
        return config.get("login","password")

    @staticmethod
    def get_login_url():
        return config.get("urls", "login_url")