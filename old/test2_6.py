from selenium.webdriver.support.ui import Select
import os
import time
import requests

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Следующие импорты отвечают за скачивание самой последней и подходящей версии драйвера браузера `Google crome`
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import utils as manager_utils

# Тут мы переписываем RegEx для того чтобы брать номер мастер-версию для Google Chrome
manager_utils.PATTERN[manager_utils.ChromeType.GOOGLE] = r'(?<=\s)\d+'
google_chrome_version_base = manager_utils.get_browser_version_from_os(manager_utils.ChromeType.GOOGLE)
# Тут мы находим последнюю версию вебдрайвера для нашего Chrome
supported_webdriver_version_latest = requests.get(f'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{google_chrome_version_base}').content.decode()

# Устанавливаем последний подходящий webdriver, он появится в папке `.wdm` в текущей директории
driver_path = ChromeDriverManager(path=os.curdir, version=supported_webdriver_version_latest ).install()
# Инициализируем браузер при помощи вебдрайвера и разворачиваем во весь экран
browser = webdriver.Chrome(service=Service(executable_path=driver_path))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    value_x = browser.find_element(By.ID, 'input_value').text

    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(value_x)
    answer_input = browser.find_element(By.XPATH, "//input[@id='answer']")
    answer_input.send_keys(y)
    robot_checkbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    robot_checkbox.click()


    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robot_rule_radio = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    robot_rule_radio.click()



    button.click()

    __file__



# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()












