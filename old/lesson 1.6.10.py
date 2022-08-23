from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    driver = webdriver.Chrome(service=Service(executable_path='.wdm/drivers/chromedriver/linux64/104.0.5112.79/chromedriver'))
    driver.get(link)

    first = driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    first.send_keys("first")

    second = driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    second.send_keys("second")

    third = driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    third.send_keys("third")

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    time.sleep(1)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    driver.quit()
