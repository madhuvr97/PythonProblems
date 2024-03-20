from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://rahulshettyacademy.com/seleniumPractise"

# headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

# Initialize web driver
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(url)
    driver.find_element(By.LINK_TEXT, "Top Deals").click()

    tabs_opened = driver.window_handles
    driver.switch_to.window(tabs_opened[1])
    driver.find_element(By.XPATH, "//th[@role='columnheader'][1]").click()
    veg_fruits = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
    sorted_veg_fruits = sorted(veg_fruits, key=lambda x: x.text)
    assert veg_fruits == sorted_veg_fruits

    '''
    browser_sorted_list = []
    for veg in veg_fruits:
        browser_sorted_list.append(veg.text)
    original_browser_sorted_list = browser_sorted_list.copy()
    browser_sorted_list.sort()
    assert browser_sorted_list == original_browser_sorted_list
    '''

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()

