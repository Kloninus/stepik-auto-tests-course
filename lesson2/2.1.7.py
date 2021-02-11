from selenium import webdriver
import time
import  math

#from selenium.webdriver.support.ui import Select
#select = Select(browser.find_element_by_tag_name("select"))
#select.select_by_value("1") # ищем элемент с текстом "Python"


def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest_img = browser.find_element_by_id("treasure")
    chest_atr = chest_img.get_attribute("valuex")
    y = calc(chest_atr)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    checkbox1 = browser.find_element_by_id("robotCheckbox")
    checkbox1.click()

    radiobtn1 = browser.find_element_by_id("robotsRule")
    radiobtn1.click()

    button1 = browser.find_element_by_css_selector(".btn")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()