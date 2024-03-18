from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class E2ETest:
    def __init__(self):
        self.url = "https://rahulshettyacademy.com/seleniumPractise"
        self.input_data = {
            "search": "ber",
            "promocode": "rahulshettyacademy",
            "success_message": "Code applied ..!"
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def search_for_product(self):
        self.driver.get(self.url)
        search_input = self.wait_for_element((By.XPATH, "//input[@type='search']"))
        search_input.send_keys(self.input_data["search"])
        self.wait_for_element((By.CSS_SELECTOR, ".product-name"))

    def add_products_to_cart(self):
        products = self.wait_for_elements((By.XPATH, "//div[@class='products']/div"))
        for product in products:
            product.find_element(By.XPATH, "div/button").click()
            self.wait_for_element((By.CSS_SELECTOR, ".added"))

    def proceed_to_checkout(self):
        cart_icon = self.driver.find_element(By.XPATH, "//img[@alt='Cart']")
        cart_icon.click()
        proceed_to_checkout_button = self.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
        proceed_to_checkout_button.click()

    def apply_promo_code(self):
        select_promocode = self.wait_for_element((By.CSS_SELECTOR, ".promoCode"))
        select_promocode.send_keys(self.input_data["promocode"])
        promo_btn = self.driver.find_element(By.CSS_SELECTOR, ".promoBtn")
        promo_btn.click()
        self.wait_for_element((By.CLASS_NAME, "promoInfo"))

    def validate_total_amount(self):
        prices = self.driver.find_elements(By.XPATH, "//tbody/tr/td[5]/p")
        total_amount = int(self.driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
        sum_prices = sum(int(price.text) for price in prices)
        assert sum_prices == total_amount, "Total amount mismatch"
        return total_amount

    def validate_discount_amount(self):
        discount_percentage = float(self.driver.find_element(By.CSS_SELECTOR, ".discountPerc").text[:-1])
        total_after_discount = float(self.driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
        total_amount = self.validate_total_amount()
        calculated_amount = total_amount - (total_amount * (discount_percentage / 100))
        assert total_after_discount == calculated_amount, "Discount amount mismatch"

    def run_test(self):
        try:
            self.search_for_product()
            self.add_products_to_cart()
            self.proceed_to_checkout()
            self.apply_promo_code()
            self.validate_total_amount()
            self.validate_discount_amount()
            print("Test passed: All validations successful!")
        except Exception as e:
            print("Test failed:", str(e))
        finally:
            self.driver.quit()

if __name__ == "__main__":
    test = E2ETest()
    test.run_test()
