from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.chrome.options import Options
chrome_options = Options()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


webdriver.ChromeOptions().add_argument("--browser.chrome.path=F:/chrome-win64/chrome.exe")

webdriver.ChromeOptions().add_argument("--browser.chrome.driver=C:/chromedriver/chromedriver.exe")

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input2 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    input3 = browser.find_element(By.CSS_SELECTOR, "#answer")
    x_value = int(input2.text)
    answer = calc(x_value)
    input3.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # Переключаем контекст WebDriver на всплывающее окно
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла