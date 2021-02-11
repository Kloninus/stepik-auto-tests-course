from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x,y):

    return str(int(x)+int(y))

try:

    link = " http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_el = browser.find_element_by_id("num1")
    x1 = x1_el.text
    x2_el = browser.find_element_by_id("num2")
    x2 = x2_el.text
    y = calc(x1, x2)

    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(y)

    button1 = browser.find_element_by_css_selector(".btn")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()