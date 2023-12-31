from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    # Нажать на кнопку "Book"
    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

button = browser.find_element(By.ID, "button")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button.click()

time.sleep(10)
browser.quit()