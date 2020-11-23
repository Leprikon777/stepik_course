import os
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    submit_button = browser.find_element_by_css_selector(".btn")
    submit_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input_value = browser.find_element_by_id("input_value")
    y = str(math.log(abs(12*math.sin(int(input_value.text)))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    submit_button = browser.find_element_by_css_selector(".btn")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()