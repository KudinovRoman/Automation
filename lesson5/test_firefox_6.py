
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username_location = 'username'

    username = driver.find_element(By.ID, username_location)

    username.send_keys("tomsmith")
    sleep(2)

    login_location = 'password'

    login = driver.find_element(By.ID, login_location)

    login.send_keys("SuperSecretPassword!")
    sleep(2)

    login_button_location = '//i[text()=" Login"]'
    login_button = driver.find_element(By.XPATH, login_button_location).click()
    sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.quit()