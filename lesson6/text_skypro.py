
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.maximize_window()

waiter = WebDriverWait(driver, 10)

try:
    driver.get("http://uitestingplayground.com/textinput")

    entering_text = driver.find_element(By.ID, "newButtonName")
    entering_text.send_keys("SkyPro")
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()
    waiter.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    print(blue_button.text)

except Exception as ex:
    print(ex)

finally:
    driver.quit()
