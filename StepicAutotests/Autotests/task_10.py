import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

br = webdriver.Chrome()
br.get(link)

buttom1 = br.find_element(By.TAG_NAME, "button").click()


new_window = br.window_handles[1]
first_window = br.window_handles[0]
br.switch_to.window(new_window)

x = br.find_element(By.ID, "input_value").text
res = calc(x)

answer = br.find_element(By.ID, "answer").send_keys(res)
button = br.find_element(By.XPATH, '//button').click()

time.sleep(20)
br.quit()