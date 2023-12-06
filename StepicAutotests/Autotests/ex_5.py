from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link2)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text("Python")

time.sleep(20)
browser.quit()