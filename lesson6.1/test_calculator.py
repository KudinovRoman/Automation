
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
waiter = WebDriverWait(driver, 50)
def test_calculator():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
    
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys('5')
    
    number1 = "7"
    number2 = "8"
    sign = "+"
    equal_to = "="

    num1 = int(number1)
    num2 = int(number2)

    if sign == "+":
        result = num1 + num2
    elif sign == "-":
        result = num1 - num2
    elif sign == "x":
        result = num1 * num2
    elif sign == "÷":
        result = num1 / num2   
    else:
        result = "может какой-то знак хочешь поставить между цифрами?"

    driver.find_element(By.XPATH, f'//span[text()="{number1}"]').click()
    driver.find_element(By.XPATH, f'//span[text()="{sign}"]').click()
    driver.find_element(By.XPATH, f'//span[text()="{number2}"]').click()
    driver.find_element(By.XPATH, f'//span[text()="{equal_to}"]').click()

    waiter.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), str(result))
    )

    screen_text = driver.find_element(By.CLASS_NAME, "screen").text

    assert screen_text == str(result)
    driver.quit()

