import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Alex")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Gricenko")
    email = browser.find_element_by_name("email")
    email.send_keys("a@a.ru")


    file_button = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    file_button.send_keys(file_path)

    submit_button = browser.find_element_by_css_selector(".btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()