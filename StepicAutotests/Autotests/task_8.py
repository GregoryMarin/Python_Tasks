from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element(By.XPATH, "//input[1]").send_keys("Gregory")
lastname = browser.find_element(By.XPATH, "//input[2]").send_keys("M")
email = browser.find_element(By.XPATH, "//input[3]").send_keys("jkljf@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'someFile.txt')           # добавляем к этому пути имя файла
fileAdd = browser.find_element(By.ID, "file").send_keys(file_path)

button = browser.find_element(By.TAG_NAME, "button").click()

time.sleep(15)
browser.quit()