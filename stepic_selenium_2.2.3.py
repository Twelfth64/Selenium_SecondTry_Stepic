from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import math

def calc(x, y):
  return str(int(x) + int(y))


chrome_options = Options()

webdriver.ChromeOptions().add_argument("--browser.chrome.path=F:/chrome-win64/chrome.exe")

webdriver.ChromeOptions().add_argument("--browser.chrome.driver=C:/chromedriver/chromedriver.exe")

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x_element = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y_element = y_element.text
    sum = calc(x_element, y_element)

    # Ваш код, который заполняет обязательные поля
    selector_answer = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    selector_answer.select_by_visible_text(sum)

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()