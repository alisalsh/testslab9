import unittest
from selenium import webdriver
from contact_page import ContactPage
import os
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
    
    def test_successful_form_submission_with_all_fields(self):
        # Тестовые данные
        test_data = {
            'name': 'Иван Иванов',
            'email': 'ivan@example.com',
            'phone': '1234567890',
            'message': 'Это тестовое сообщение для проверки формы.'
        }
        
        # Заполняем форму
        self.contact_page.fill_form(
            name=test_data['name'],
            email=test_data['email'],
            phone=test_data['phone'],
            message=test_data['message']
        )
        
        # Отправляем форму
        self.contact_page.submit_form()
        
        # Проверяем результат
        self.assertTrue(
            self.contact_page.is_success_message_displayed(),
            "Сообщение об успехе не отображается после отправки формы с валидными данными"
        )
        
        success_text = self.contact_page.get_success_message_text()
        expected_text = "Спасибо! Ваше сообщение отправлено."
        
        self.assertEqual(
            success_text, 
            expected_text,
            f"Текст успешного сообщения не совпадает. Ожидалось: '{expected_text}', Получено: '{success_text}'"
        )
    

if __name__ == "__main__":
    unittest.main()