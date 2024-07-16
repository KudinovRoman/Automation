from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()


# Клик по кнопке без ID


try:
    # Счетчик кликов
    count = 0
    driver.get("http://uitestingplayground.com/dynamicid")
    

    # Определение переменной кнопки
    blue_button_location = '//button[text()="Button with Dynamic ID"]'
    
    # Кликнуть по синей кнопке
    blue_button = driver.find_element(By.XPATH, blue_button_location).click()

    # Кликните на синюю кнопку 3 раза
    for _ in range(3):
        blue_button = driver.find_element(By.XPATH, blue_button_location).click()
        count += 1
        sleep(5)
        print(count)

except Exception as ex:
    print(ex)

finally:
    driver.quit()