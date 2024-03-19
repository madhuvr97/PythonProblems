from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com"
input_data = {
    "text": "Hello madhu"
}
# Initialize web driver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get(url)
    driver.find_element(By.LINK_TEXT, "Multiple Windows").click()
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    tabs_opened = driver.window_handles

    driver.switch_to.window(tabs_opened[1])
    print(driver.find_element(By.TAG_NAME, "h3").text)
    driver.close()

    driver.switch_to.window(tabs_opened[0])
    assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
    driver.back()

    driver.find_element(By.LINK_TEXT, "Frames").click()
    driver.find_element(By.LINK_TEXT, "iFrame").click()
    driver.switch_to.frame("mce_0_ifr")
    driver.find_element(By.ID, "tinymce").clear()
    driver.find_element(By.ID, "tinymce").send_keys(input_data["text"])

    driver.switch_to.default_content()
    print(driver.find_element(By.TAG_NAME, "h3").text)

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()