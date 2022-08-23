import os
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Adding manager for managing chromedriver versions and installations
from webdriver_manager.chrome import ChromeDriverManager
import webdriver_manager.core.utils as manager_utils

# Owerwrite regex pattern to get full Google Chrome browser version
manager_utils.PATTERN[manager_utils.ChromeType.GOOGLE] = r'[\d.]+'
google_chrome_version = manager_utils.get_browser_version_from_os(manager_utils.ChromeType.GOOGLE)

# Installing required driver and saving location as variable
driver_path = ChromeDriverManager(path=os.curdir, version=google_chrome_version).install()

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome(service=Service(driver_path))
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("UA")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
