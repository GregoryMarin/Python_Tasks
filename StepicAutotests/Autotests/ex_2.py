from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'name')]").send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]").send_keys("Ilon_Mask@gmail.com")
    input3 = browser.find_element(By.XPATH, '//input[contains(@placeholder, "last")]').send_keys("Petrov")
    input4 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'pho')]").send_keys("9634853045")
    input5 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'add')]").send_keys("Mars")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    #Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    #Проверяем, что смогли зарегестрироваться
    #Ждем загрузки страницы
    time.sleep(1)

    #находим элемент, содержащий текст
    welcome_text_el = browser.find_element(By.TAG_NAME, 'h1')
    #записываем в переменную welcome_text текст из элемента welcome_text_el
    welcome_text = welcome_text_el

    # с помощью assert проверяем, что ождаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()