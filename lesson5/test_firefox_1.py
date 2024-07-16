from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# Клик по кнопке


try: 
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    add_element_locator = '//button[text()="Add Element"]'
    delete_id = '//button[text()="Delete"]'


    add_button = driver.find_element(By.XPATH, add_element_locator)

    # Пять раз кликните на кнопку Add Element
    for new_element in range(0, 5):
        add_button.click()

    # Соберите со страницы список кнопок Delete

    all_delete = driver.find_elements(By.XPATH, delete_id)

    # Выведите на экран размер списка
    print(len(all_delete))

    sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.quit()