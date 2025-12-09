from base_page import BasePage
from selenium.webdriver.common.by import By
import time

class ContactPage(BasePage):
    """
    Класс для работы со страницей контактной формы.
    """ 
    # элементы формы
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    PHONE_INPUT = (By.ID, "phone")
    MESSAGE_TEXTAREA = (By.ID, "message")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    # сообщения об ошибках
    NAME_ERROR = (By.ID, "nameError")
    EMAIL_ERROR = (By.ID, "emailError")
    PHONE_ERROR = (By.ID, "phoneError")
    MESSAGE_ERROR = (By.ID, "messageError")
    
    SUCCESS_MESSAGE = (By.ID, "successMessage")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def load(self, url):
        self.driver.get(url)
        self.find_element(*self.NAME_INPUT)
    
    def fill_name(self, name):
        """Заполнить поле имени"""
        self.input_text(*self.NAME_INPUT, name)
    
    def fill_email(self, email):
        """Заполнить поле email"""
        self.input_text(*self.EMAIL_INPUT, email)
    
    def fill_phone(self, phone):
        """Заполнить поле телефона"""
        self.input_text(*self.PHONE_INPUT, phone)
    
    def fill_message(self, message):
        """Заполнить поле сообщения"""
        self.input_text(*self.MESSAGE_TEXTAREA, message)
    
    def submit_form(self):
        """Отправить форму"""
        self.click_element(*self.SUBMIT_BUTTON)
        time.sleep(2)
    
    def get_name_error(self):
        """текст ошибки имени"""
        if self.wait_for_element_has_text(*self.NAME_ERROR, timeout=5):
            return self.get_element_text(*self.NAME_ERROR)
        return ""
    
    def get_email_error(self):
        """текст ошибки для email """
        if self.wait_for_element_has_text(*self.EMAIL_ERROR, timeout=5):
            return self.get_element_text(*self.EMAIL_ERROR)
        return ""
    
    def get_phone_error(self):
        """текст ошибки телефона"""
        if self.wait_for_element_has_text(*self.PHONE_ERROR, timeout=5):
            return self.get_element_text(*self.PHONE_ERROR)
        return ""
    
    def get_message_error(self):
        """текст ошибки сообщения"""
        if self.wait_for_element_has_text(*self.MESSAGE_ERROR, timeout=5):
            return self.get_element_text(*self.MESSAGE_ERROR)
        return ""
    # Ожидание появления ошибки 
    def wait_for_name_error(self, expected_text=None):
        
        if expected_text:
            return self.wait_for_specific_text(*self.NAME_ERROR, expected_text)
        else:
            return self.wait_for_element_has_text(*self.NAME_ERROR)
    
    def wait_for_email_error(self, expected_text=None):
       
        if expected_text:
            return self.wait_for_specific_text(*self.EMAIL_ERROR, expected_text)
        else:
            return self.wait_for_element_has_text(*self.EMAIL_ERROR)
    
    def wait_for_phone_error(self, expected_text=None):
       
        if expected_text:
            return self.wait_for_specific_text(*self.PHONE_ERROR, expected_text)
        else:
            return self.wait_for_element_has_text(*self.PHONE_ERROR)
    
    def wait_for_message_error(self, expected_text=None):
        if expected_text:
            return self.wait_for_specific_text(*self.MESSAGE_ERROR, expected_text)
        else:
            return self.wait_for_element_has_text(*self.MESSAGE_ERROR)
    
    def is_success_message_displayed(self):
        return self.is_element_visible(*self.SUCCESS_MESSAGE)
    
    def get_success_message_text(self):
        if self.is_success_message_displayed():
            return self.get_element_text(*self.SUCCESS_MESSAGE)
        return ""
    
    def fill_form(self, name="", email="", phone="", message=""):
        """
        Заполнить всю форму данными
        """
        if name:
            self.fill_name(name)
        if email:
            self.fill_email(email)
        if phone:
            self.fill_phone(phone)
        if message:
            self.fill_message(message)
    
    def clear_form(self):
        """Очистить"""
        self.find_element(*self.NAME_INPUT).clear()
        self.find_element(*self.EMAIL_INPUT).clear()
        self.find_element(*self.PHONE_INPUT).clear()
        self.find_element(*self.MESSAGE_TEXTAREA).clear()
    
    def get_field_value(self, field_locator):
        return self.find_element(*field_locator).get_attribute('value')