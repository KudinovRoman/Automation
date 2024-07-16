from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()


# Модальное окно

try:
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    wait = WebDriverWait(driver, 10)
    close_button_location = '//p[text()="Close"]'
    
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, close_button_location))).click()
    sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.quit()