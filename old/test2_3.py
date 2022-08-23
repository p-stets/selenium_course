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
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    number_1 = browser.find_element(By.ID, 'num1').text
    number_2 = browser.find_element(By.ID, 'num2').text

    result = sum([int(number_1), int(number_2)])
    options = Select(webelement=browser.find_element(By.XPATH, '//select[@id="dropdown"]'))
    options.select_by_value(str(result))
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

    input


# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

