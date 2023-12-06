from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


br = webdriver.Chrome()
br.get(link)

browser = br.find_element(By.ID, "input_value")
i = browser.text
res = calc(i)

input1 = br.find_element(By.ID, "answer").send_keys(res)
input2 = br.find_element(By.ID, "robotCheckbox").click()
input3 = br.find_element(By.ID, "robotsRule").click()

button = br.find_element(By.TAG_NAME, "button").click()

time.sleep(20)
br.quit()