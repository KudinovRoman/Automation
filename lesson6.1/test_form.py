
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
waiting = WebDriverWait(driver, 10)

def test_form():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")


    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


    waiting.until(EC.presence_of_element_located((By.ID, "zip-code")))

    background_color_zip = driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")
    assert background_color_zip == "rgba(248, 215, 218, 1)"


    c1 = driver.find_element(By.ID, "first-name").value_of_css_property("background-color")
    c2 = driver.find_element(By.ID, "last-name").value_of_css_property("background-color")
    c3 = driver.find_element(By.ID, "address").value_of_css_property("background-color")
    c4 = driver.find_element(By.ID, "city").value_of_css_property("background-color")
    c5 = driver.find_element(By.ID, "country").value_of_css_property("background-color")
    c6 = driver.find_element(By.ID, "e-mail").value_of_css_property("background-color")
    c7 = driver.find_element(By.ID, "phone").value_of_css_property("background-color")
    c8 = driver.find_element(By.ID, "job-position").value_of_css_property("background-color")
    c9 = driver.find_element(By.ID, "company").value_of_css_property("background-color")

    color_lenght = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
    background_color_all = ["rgba(209, 231, 221, 1)"] * 9 
    #d1e7dd

    assert color_lenght == background_color_all
    
    driver.quit()

