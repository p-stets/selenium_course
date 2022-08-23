# from selenium.webdriver.support.ui import Select
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
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    fname = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    lname = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    email = browser.find_element(By.XPATH, '//input[@name="email"]')
    file = browser.find_element(By.XPATH, '//input[@type="file"]')
    submit = browser.find_element(By.XPATH, '//button[@type="submit"]')

    fname.send_keys("John")
    lname.send_keys("Doe")
    email.send_keys("some@email.com")


    file.send_keys(os.path.join(os.path.dirname(__file__), 'requirements.txt'))
    submit.click()



















finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()












