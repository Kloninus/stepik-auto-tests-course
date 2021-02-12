from selenium import webdriver
import time
import unittest

class Test_Registr(unittest.TestCase):

    def test_Reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Мой ответ")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Мой ответ")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # находим элемент, содержащий текст
        actual_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        actual_text = actual_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(actual_text, expected_text, f"Registration fail, expected {expected_text}, got {actual_text}" )
        browser.quit()

    def test_Reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Мой ответ")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Мой ответ")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # находим элемент, содержащий текст
        actual_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        actual_text = actual_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(actual_text, expected_text, f"Registration fail, expected {expected_text}, got {actual_text}")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
