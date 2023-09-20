from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.chrome.options import Options
chrome_options = Options()

webdriver.ChromeOptions().add_argument("--browser.chrome.path=F:/chrome-win64/chrome.exe")

webdriver.ChromeOptions().add_argument("--browser.chrome.driver=C:/chromedriver/chromedriver.exe")

link = "https://testpages.herokuapp.com/styled/alerts/alert-test.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Кликаем на кнопку, вызывающую alert
    button = browser.find_element(By.ID, "alertexamples")
    button.click()

    #Переключаем контекст WebDriver на всплывающее окно
    #driver.switchTo().alert();

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла