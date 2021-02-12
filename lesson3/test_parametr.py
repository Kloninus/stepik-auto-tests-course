import pytest
from selenium import webdriver
import time
import math

exepted_text = "Correct!"

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()

def calc():
    return str(math.log(int(time.time())))

@pytest.mark.parametrize('link_num', ["895", "896","897","898","899","903","904","905"])
class TestParametr:
    def test_guest_should_see_login_link(self, browser, link_num):
        link = f"https://stepik.org/lesson/236{link_num}/step/1/"
        browser.get(link)
        textarea = browser.find_element_by_class_name("textarea")
        textarea.send_keys(calc())
        button = browser.find_element_by_class_name("submit-submission")
        button.click()
        answ_elem = browser.find_element_by_class_name("smart-hints__hint")
        assert answ_elem.text == exepted_text, f"exepted {exepted_text}, but -- {answ_elem.text}"



