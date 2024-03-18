from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://rahulshettyacademy.com/seleniumPractise"
input_data = {
    "search": "ber",
    "promocode": "rahulshettyacademy",
    "success_message": "Code applied ..!"
}

# Initialize web driver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get(url)

    # search for the product
    driver.find_element(By.XPATH, "//input[@type='search']").send_keys(input_data["search"])

    # Add the products to cart and checkout
    products = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='products']/div"))
    )
    for product in products:
        # chaining of web elements
        product.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
    driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

    # Apply promocode
    select_promocode = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoCode"))
    )
    select_promocode.send_keys(input_data["promocode"])
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

    success_message = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "promoInfo"),input_data["success_message"])
    )

    assert success_message, "Success message not found or doesn't match expected message"

    # sum validation
    prices = driver.find_elements(By.XPATH, "//tbody/tr/td[5]/p")
    total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
    sum = 0
    for price in prices:
        sum = sum + int(price.text)

    assert sum == total_amount, "Total amount mismatch"

    # discount validation
    discount_percentage = float(driver.find_element(By.CSS_SELECTOR, ".discountPerc").text[:-1])
    total_after_discount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
    calculated_amount = total_amount - ((discount_percentage/100)*total_amount)
    assert total_after_discount == calculated_amount

    print("Test passed: All validations successful!")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
