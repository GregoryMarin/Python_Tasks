from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

n1 = browser.find_element(By.ID, "num1").text
n2 = browser.find_element(By.ID, "num2").text

x = int(n1) + int(n2)

select = Select(browser.find_element(By.XPATH, "//select"))
select.select_by_visible_text(str(x))

button = browser.find_element(By.TAG_NAME, "button").click()


time.sleep(20)
browser.quit()
