import unittest
from selenium import webdriver
from contact_page import ContactPage
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from contact_page import ContactPage
import os

class TestContactFormPositive(unittest.TestCase):
    
    def setUp(self):
        # Настройки для CI/CD
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Без графического интерфейса
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        
        # Автоматическая установка ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        self.contact_page = ContactPage(self.driver)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = f"file://{os.path.join(current_dir, 'contact_form.html')}"
        
        self.contact_page.load(html_file_path)
    
    def tearDown(self):
        if self.driver:
            self.driver.quit()
    
    def test_empty_required_name_field(self):
        self.contact_page.clear_form()
        
        # Заполняем все поля кроме имени
        self.contact_page.fill_form(
            email='test@example.com',
            phone='1234567890',
            message='Тестовое сообщение'
        )
        self.contact_page.submit_form()
        time.sleep(1)
        
        name_error = self.contact_page.get_name_error()
        expected_error = 'Имя обязательно для заполнения.'
        
        self.assertIn(
            expected_error, 
            name_error,
            f"Неверное сообщение об ошибке для пустого имени. Ожидалось: '{expected_error}', Получено: '{name_error}'"
        )
    
    def test_invalid_email_format(self):
        self.contact_page.clear_form()
        
        # Заполняем форму с невалидным email
        self.contact_page.fill_form(
            name='Иван Иванов',
            email='invalid-email',
            message='Тестовое сообщение'
        )
        self.contact_page.submit_form()
        time.sleep(1)
        
        # Проверяем сообщение об ошибке
        email_error = self.contact_page.get_email_error()
        expected_error = 'Введите корректный email.'
        
        self.assertIn(
            expected_error, 
            email_error,
            f"Неверное сообщение об ошибке для невалидного email. Ожидалось: '{expected_error}', Получено: '{email_error}'"
        )
    
    def test_invalid_phone_format(self):
        self.contact_page.clear_form()
        
        # Заполняем форму с невалидным телефоном
        self.contact_page.fill_form(
            name='Иван Иванов',
            email='ivan@example.com',
            phone='12345',
            message='Тестовое сообщение'
        )
        self.contact_page.submit_form()
        time.sleep(1)
        phone_error = self.contact_page.get_phone_error()
        expected_error = 'Телефон должен содержать 10 цифр.'
        
        self.assertIn(
            expected_error, 
            phone_error,
            f"Неверное сообщение об ошибке. Ожидалось: '{expected_error}', Получено: '{phone_error}'"
        )
    
    def test_empty_message_field(self):
        self.contact_page.clear_form()
        
        # Заполняем все поля кроме сообщения
        self.contact_page.fill_form(
            name='Иван Иванов',
            email='ivan@example.com',
            phone='1234567890'
        )
        self.contact_page.submit_form()
        time.sleep(1)
        
        message_error = self.contact_page.get_message_error()
        expected_error = 'Сообщение обязательно для заполнения.'
        
        self.assertIn(
            expected_error, 
            message_error,
            f"Неверное сообщение об ошибке для пустого сообщения. Ожидалось: '{expected_error}', Получено: '{message_error}'"
        )

if __name__ == "__main__":
    unittest.main()