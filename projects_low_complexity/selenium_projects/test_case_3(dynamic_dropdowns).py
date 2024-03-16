import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# constants
url = "https://rahulshettyacademy.com/dropdownsPractise/"
input_data = {
    "country_short_form": "Ind",
    "country": "India"
}

# Initialize web driver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open URL
    driver.get(url)

    # Enter country short form
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "autosuggest"))
    )
    input_field.send_keys(input_data["country_short_form"])

    # Select the country from the dropdown
    country_options = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[class = "ui-menu-item"] a'))
    )
    for country in country_options:
        if country.text == input_data["country"]:
            country.click()
            break

    # Wait for the selected country to appear in the input field
    selected_country = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_value((By.ID, "autosuggest"), input_data["country"])
    )

    assert selected_country

    # using get attribute method
    #assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == input_data["country"]

except Exception as e:
    print("An error occurred:", e)