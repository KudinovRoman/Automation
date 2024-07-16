
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username_location = 'input[name="username"]'

    username = driver.find_element(By.CSS_SELECTOR, username_location)

    username.send_keys("tomsmith")
    sleep(2)

    login_location = 'input[name="password"]'

    login = driver.find_element(By.CSS_SELECTOR, login_location)

    login.send_keys("SuperSecretPassword!")
    sleep(2)

    login_button_location = "fa.fa-2x.fa-sign-in"
    login_button = driver.find_element(By.CLASS_NAME, login_button_location).click()
    sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.quit()