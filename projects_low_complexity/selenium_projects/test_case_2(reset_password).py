import json
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://rahulshettyacademy.com/client/'
current_file_name = os.path.basename(__file__)

with open('consolidated_data.json',"r") as file:
    test_cases_data = json.load(file)

for test_case in test_cases_data["test_cases"]:
    if test_case['test_case_name'] == f'{current_file_name[:-3]}':
        input_data = test_case["input_data"]
        email = input_data["email"]
        password = input_data["password"]


try:
    driver = webdriver.Edge()
    driver.get(URL)
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Forgot password?").click()
    driver.find_element(By.XPATH, "//form/div[1]/input").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys(password)
    driver.find_element(By.XPATH, "//button[text() = 'Save New Password']").click()

    time.sleep(10)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()