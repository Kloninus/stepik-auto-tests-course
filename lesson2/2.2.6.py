from selenium import webdriver
import time
import  math

def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element_by_id("input_value")
    x = x_el.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    checkbox1 = browser.find_element_by_id("robotCheckbox")
    checkbox1.click()

    radiobtn1 = browser.find_element_by_id("robotsRule")
    radiobtn1.click()

    button1 = browser.find_element_by_css_selector(".btn")
    button1.click()

    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()