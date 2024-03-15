import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://rahulshettyacademy.com/angularpractice/"

# Load input data from JSON file
with open("input_data.json", "r") as file:
    INPUT_DATA = json.load(file)

try:
    # Initialize Microsoft Edge WebDriver, launch the URL and maximize the window
    driver = webdriver.Edge()
    driver.get(URL)
    driver.maximize_window()

    print("Title: ", driver.title)
    print("current_url: ", driver.current_url)

    # CSS Selector syntax: tagname[attribute = 'value']   or #id  or .classname
    # XPATH syntax: //tagname[@attribute = 'value']

    # Fill out the form
    driver.find_element(By.CSS_SELECTOR, 'input[name = "name"]').send_keys(INPUT_DATA['name'])
    driver.find_element(By.NAME, 'email').send_keys(INPUT_DATA['email'])
    driver.find_element(By.ID, 'exampleInputPassword1').send_keys(INPUT_DATA['password'])
    if INPUT_DATA['checkbox']:
        driver.find_element(By.ID, 'exampleCheck1').click()
    driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()

    # Static dropdown
    dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
    dropdown.select_by_visible_text(INPUT_DATA['gender'])

    # Submit the form
    driver.find_element(By.XPATH, '//input[@type = "submit"]').click()

    # Verify success message
    success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
    print(success_message)
    assert "Success" in success_message

    # clear and update text fields
    text_field = driver.find_element(By.XPATH, '(//input[@type = "text"])[3]')
    text_field.clear()
    text_field.send_keys(INPUT_DATA['text_update'])

    time.sleep(10)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()