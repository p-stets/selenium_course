from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time

try:
    link_1 = "http://suninjuly.github.io/registration1.html"
    link_2 = "http://suninjuly.github.io/registration2.html"
    links_list = [link_1, link_2]
    for link in links_list:
        browser = webdriver.Chrome(service=Service(executable_path='.wdm/drivers/chromedriver/linux64/104.0.5112.79/chromedriver'))
        browser.get(link)
        input1 = browser.find_element_by_css_selector('[class="form-control first"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("Smolensk@mymail.au")
        time.sleep(5)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        print('-' * 50)
finally:
    time.sleep(5)
    browser.quit()
