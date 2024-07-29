
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
def test_market(): 
    driver.get(
        "https://www.saucedemo.com/"
        )

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("МихалПалыч")
    driver.find_element(By.ID, "last-name").send_keys("Терентьев")
    driver.find_element(By.ID, "postal-code").send_keys("666555")
    driver.find_element(By.ID, "continue").click()

    total = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_summa = total.text.strip().replace("Total: ", "")
    print(total_summa)

    assert total_summa == "$58.29"
    driver.quit()

