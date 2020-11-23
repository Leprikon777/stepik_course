from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    a = num1.text
    b = num2.text
    c = "[value='" + str(int(a) + int(b)) + "']"

    browser.find_element_by_id("dropdown").click()

    browser.find_element_by_css_selector(c).click()


    input_btn = browser.find_element_by_css_selector(".btn")
    input_btn.click()



finally:
    time.sleep(10)
    browser.quit()