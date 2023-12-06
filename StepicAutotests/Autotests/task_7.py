from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import math
import time

link = "https://SunInJuly.github.io/execute_script.html"

br = webdriver.Chrome()
br.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = br.find_element(By.CSS_SELECTOR, "label>span:nth-child(2)").text
res = calc(x_element)

answer = br.find_element(By.ID, "answer").send_keys(res)
checkbox = br.find_element(By.ID, "robotCheckbox").click()
radiobutton = br.find_element(By.ID, "robotsRule")
br.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()

button = br.find_element(By.TAG_NAME, "button")
br.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(20)
br.quit()
