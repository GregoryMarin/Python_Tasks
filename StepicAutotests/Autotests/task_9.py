import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


br = webdriver.Chrome()
br.get(link)

but1 = br.find_element(By.XPATH, '//button').click()

confirm = br.switch_to.alert
confirm.accept()

x = br.find_element(By.ID, "input_value").text
res = calc(x)

answer = br.find_element(By.ID, "answer").send_keys(res)

button = br.find_element(By.XPATH, '//button').click()

time.sleep(20)
br.quit()