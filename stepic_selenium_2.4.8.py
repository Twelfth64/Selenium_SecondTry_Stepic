from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


from selenium.webdriver.chrome.options import Options
chrome_options = Options()



webdriver.ChromeOptions().add_argument("--browser.chrome.path=F:/chrome-win64/chrome.exe")

webdriver.ChromeOptions().add_argument("--browser.chrome.driver=C:/chromedriver/chromedriver.exe")


try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    Money = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    input1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    answer_button = browser.find_element(By.CSS_SELECTOR, "#answer")
    x_value = input1.text
    answer = calc(x_value)
    answer_button.send_keys(answer)

    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    button2.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()


finally:
    time.sleep(3)
    browser.quit()