from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.chrome.options import Options
chrome_options = Options()

webdriver.ChromeOptions().add_argument("--browser.chrome.path=F:/chrome-win64/chrome.exe")

webdriver.ChromeOptions().add_argument("--browser.chrome.driver=C:/chromedriver/chromedriver.exe")

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("123")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Переключаем контекст WebDriver на всплывающее окно
    alert = browser.switch_to.alert
    print(alert.text)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла