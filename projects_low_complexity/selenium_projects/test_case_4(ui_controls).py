from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

url = "https://rahulshettyacademy.com/AutomationPractice/"
input_data = {
    "option": "option2",
    "radio_button": "radio2",
    "name": "madhu"
}

# headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

# Initialize web driver
driver = webdriver.Chrome(options= chrome_options)
driver.maximize_window()

try:
    driver.get(url)

    # checkboxes
    options = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for option in options:
        if option.get_attribute("value") == input_data["option"]:
            option.click()
            assert option.is_selected()
            break

    # Radio buttons
    radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
    for radio_button in radio_buttons:
        if radio_button.get_attribute("value")  == input_data["radio_button"]:
            radio_button.click()
            assert radio_button.is_selected()
            break

    assert driver.find_element(By.ID, "displayed-text").is_displayed()
    driver.find_element(By.ID, "hide-textbox").click()
    assert not driver.find_element(By.ID, "displayed-text").is_displayed()

    # alerts
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(input_data["name"])
    driver.find_element(By.ID, "alertbtn").click()
    alert = driver.switch_to.alert
    assert input_data["name"] in alert.text
    alert.accept()

    # actions like hovering, double click etc
    actions = ActionChains(driver)
    actions.scroll_to_element(driver.find_element(By.ID, "mousehover")).perform()
    actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
    actions.click(driver.find_element(By.LINK_TEXT, "Top")).perform()

    # scrolling to the bottom of the webpage and taking screenshots
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    driver.save_screenshot("screen.png")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()