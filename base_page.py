from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы для работы с веб-элементами.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, by, value):
        """ элемент с ожиданием"""
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    def find_clickable_element(self, by, value):
        """ кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable((by, value)))
    
    def is_element_visible(self, by, value, timeout=10):
        """роверить видимость элемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False
    
    def get_element_text(self, by, value):
        """ текст элемента"""
        element = self.find_element(by, value)
        return element.text
    
    def input_text(self, by, value, text):
        """Ввести текст """
        element = self.find_clickable_element(by, value)
        element.clear()
        element.send_keys(text)
    
    def click_element(self, by, value):
        """Клик по элементу"""
        element = self.find_clickable_element(by, value)
        element.click()
    
    def wait_for_element_has_text(self, by, value, timeout=10):
        """Ожидание пока элемент получит любой текст"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.find_element(by, value).text.strip() != ''
            )
            return True
        except TimeoutException:
            return False
    
    def wait_for_specific_text(self, by, value, expected_text, timeout=10):
        """Ожидание появления текста в элементе"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: expected_text in driver.find_element(by, value).text
            )
            return True
        except TimeoutException:
            return False
    
    def execute_script(self, script, *args):
        """Выполнить код"""
        return self.driver.execute_script(script, *args)