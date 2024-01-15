from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button = browser.find_element(By.ID, "book").click()
browser.implicitly_wait(2)

x = browser.find_element(By.ID, "input_value").text
res = calc(x)

answer = browser.find_element(By.ID, "answer").send_keys(res)
buton2 = browser.find_element(By.ID, "solve").click()

time.sleep(10)
browser.quit()