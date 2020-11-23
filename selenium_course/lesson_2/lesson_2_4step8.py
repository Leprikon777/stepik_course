from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    b = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button_book = browser.find_element_by_id("book")
    button_book.click()
    input_value = browser.find_element_by_id("input_value")
    y = str(math.log(abs(12*math.sin(int(input_value.text)))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    button_solve = browser.find_element_by_id("solve")
    button_solve.click()
finally:
    time.sleep(10)
    browser.quit()