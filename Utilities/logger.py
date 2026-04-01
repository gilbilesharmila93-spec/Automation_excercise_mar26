import inspect
import logging


class Logger_class:
    @staticmethod
    def get_logger():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(funcName)s : %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('.\\Logs\\Automation_practice.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger