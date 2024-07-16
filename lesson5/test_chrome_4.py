from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Модальное окно

try:
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    wait = WebDriverWait(driver, 10)
    close_button_location = "modal-footer"
    
    close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, close_button_location))).click()
    sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.quit()