
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.maximize_window()

waiter = WebDriverWait(driver, 40)

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        )

    waiter.until(
        EC.presence_of_element_located((By.ID, "landscape"))
    )

    award = driver.find_element(By.ID, "award")
    src = award.get_attribute('src')

    print(src)

except Exception as ex:
    print(ex)

finally:
    driver.quit()
