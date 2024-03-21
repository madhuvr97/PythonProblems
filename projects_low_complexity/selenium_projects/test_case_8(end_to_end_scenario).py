from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://rahulshettyacademy.com/angularpractice"
input_data = {
    "country": "Ind"
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

# Initialize web driver
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(url)
    driver.find_element(By.LINK_TEXT, "Shop").click()
    products = driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
    for product in products:
        product_name = product.find_element(By.XPATH, "div/h4/a").text
        if product_name == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.CSS_SELECTOR, "a[class*= 'btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.XPATH, "//input[@id='country']").send_keys(input_data["country"])
    selected_country = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "India"))
    )
    selected_country.click()
    driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    success_message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    assert "Success" in success_message, "Assertion error: Mismatch in expected and Actual message"

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()