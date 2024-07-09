
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    field_number_location = 'input'

    field_number = driver.find_element(By.TAG_NAME, field_number_location)

    field_number.send_keys("1000")
    sleep(2)

    field_number.clear()
    sleep(2)

    field_number.send_keys("999")
    sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.quit()

