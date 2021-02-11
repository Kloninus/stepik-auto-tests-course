from selenium import webdriver
import os
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("12@gm.r")

    file1 = browser.find_element_by_id("file")
    file1.send_keys(file_path)

    button1 = browser.find_element_by_css_selector(".btn")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()