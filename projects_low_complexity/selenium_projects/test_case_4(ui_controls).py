from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://rahulshettyacademy.com/AutomationPractice/"
input_data = {
    "option": "option2",
    "radio_button": "radio2",
    "name": "madhu"
}
# Initialize web driver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get(url)
    options = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for option in options:
        if option.get_attribute("value") == input_data["option"]:
            option.click()
            assert option.is_selected()
            break

    radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
    for radio_button in radio_buttons:
        if radio_button.get_attribute("value")  == input_data["radio_button"]:
            radio_button.click()
            assert radio_button.is_selected()
            break

    assert driver.find_element(By.ID, "displayed-text").is_displayed()
    driver.find_element(By.ID, "hide-textbox").click()
    assert not driver.find_element(By.ID, "displayed-text").is_displayed()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(input_data["name"])
    driver.find_element(By.ID, "alertbtn").click()
    time.sleep(5)
    alert = driver.switch_to.alert
    assert input_data["name"] in alert.text
    alert.accept()

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()