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


browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")

browser.find_element(By.ID, "button")