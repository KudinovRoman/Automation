
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    fast_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    address = driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    zip_code = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
    city = driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    country = driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    phone = driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    job_position = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    company = driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")

    sleep(2)

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    sleep(3)

    background_color_zip = zip_code.value_of_css_property("background-color")
    assert background_color_zip == ["#f8d7da"]


    c1 = fast_name.value_of_css_property("background-color")
    c2 = last_name.value_of_css_property("background-color")
    c3 = address.value_of_css_property("background-color")
    c4 = zip_code.value_of_css_property("background-color")
    c5 = city.value_of_css_property("background-color")
    c6 = country.value_of_css_property("background-color")
    c7 = email.value_of_css_property("background-color")
    c8 = phone.value_of_css_property("background-color")
    c9 = job_position.value_of_css_property("background-color")
    c10 = company.value_of_css_property("background-color")

    color_lenght = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
    background_color_all = "#d1e7dd" * 10

    assert color_lenght == background_color_all

except Exception as ex:
    print(ex)

finally:
    driver.quit()
