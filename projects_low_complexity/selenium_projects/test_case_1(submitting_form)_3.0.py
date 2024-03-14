import json
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://rahulshettyacademy.com/angularpractice/"
current_filename = os.path.basename(__file__)

# Load input data from JSON file
with open("consolidated_data.json", "r") as file:
    test_cases_data = json.load(file)

for test_case in test_cases_data['test_cases']:
    if test_case['test_case_name'] == f'{current_filename[:-3]}':
        # Found the desired test case
        input_data = test_case["input_data"]
        # Access input data for the test case
        name = input_data["name"]
        email = input_data["email"]
        password = input_data["password"]
        checkbox = input_data["checkbox"]
        text_update = input_data["text_update"]
        break
else:
    print(f"Test case {current_filename[:-3]} not found in the JSON file.")
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
    driver.find_element(By.CSS_SELECTOR, 'input[name = "name"]').send_keys(name)
    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.ID, 'exampleInputPassword1').send_keys(password)
    if checkbox:
        driver.find_element(By.ID, 'exampleCheck1').click()
    driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()

    # Submit the form
    driver.find_element(By.XPATH, '//input[@type = "submit"]').click()

    # Verify success message
    success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
    print(success_message)
    assert "Success" in success_message

    # clear and update text fields
    text_field = driver.find_element(By.XPATH, '(//input[@type = "text"])[3]')
    text_field.clear()
    text_field.send_keys(text_update)

    time.sleep(10)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()