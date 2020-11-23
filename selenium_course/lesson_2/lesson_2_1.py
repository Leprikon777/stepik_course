from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Найдем lable чтобы взять значение для x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # Находим текстовое поле и вписываем туда ответ
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    input_checkbox = browser.find_element_by_id("robotCheckbox")
    input_checkbox.click()

    input_radio = browser.find_element_by_id("robotsRule")
    input_radio.click()

    input_btn = browser.find_element_by_css_selector(".btn")
    input_btn.click()


    time.sleep(10)
finally:
    browser.quit()