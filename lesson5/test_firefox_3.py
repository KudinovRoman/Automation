from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()


# Клик по кнопке с CSS-классом

try:
    driver.get("http://uitestingplayground.com/classattr")

    # Кликнуть на синюю кнопку 3 раза

    atr_blue_button_location = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"

    for _ in range(3):
        atr_blue_button = driver.find_element(By.XPATH, atr_blue_button_location).click()
        sleep(5)
        driver.switch_to.alert.accept()
except Exception as ex:
    print(ex)

finally:
    driver.quit()