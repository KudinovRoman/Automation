from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.maximize_window()

try:
    driver.get("http://uitestingplayground.com/ajax")

    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    driver.implicitly_wait(17)

    print(driver.find_element(By.CLASS_NAME, "bg-success").text)
    sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.quit()