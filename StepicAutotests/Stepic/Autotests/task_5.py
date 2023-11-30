from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "img[valuex]")
x = x_element.get_attribute('valuex')
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
check1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
check2 = browser.find_element(By.CSS_SELECTOR, "#robotsrule").click()
button = browser.find_element(By.CSS_SELECTOR, "button").click()


time.sleep(30)
browser.quit()