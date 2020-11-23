from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

try:
    x = browser.find_element_by_id("input_value")
    y = math.log(abs(12*math.sin(int(x.text))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    #time.sleep(5)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    #time.sleep(5)

    radio_scroll = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_scroll)
    radio_scroll.click()
    button = browser.find_element_by_tag_name("button")
    button.click()
    assert True
    time.sleep(10)
finally:
    browser.quit()