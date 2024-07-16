from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Клик по кнопке



driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_element_locator = 'button[onclick="addElement()"]'
delete_id = "button.added-manually"


add_button = driver.find_element(By.CSS_SELECTOR, add_element_locator)

# Пять раз кликните на кнопку Add Element
for new_element in range(0, 5):
    add_button.click()

# Соберите со страницы список кнопок Delete

all_delete = driver.find_elements(By.CSS_SELECTOR, delete_id)

# Выведите на экран размер списка
print(len(all_delete))

sleep(5)

