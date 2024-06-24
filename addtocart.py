import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)  # WebDriverWait object with a timeout of 10 seconds

try:
    # Navigate to login page
    driver.get('https://www.bookswagon.com/login')

    # Fill in username
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Mobile/Email']")))
    username_input.send_keys("6205329963")

    # Fill in password
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    password_input.send_keys("Pritu@1234")

    # Click login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='ctl00_phBody_SignIn_btnLogin']")))
    login_button.click()

    # Wait for the page to load after login
    wait.until(EC.url_matches("https://www.bookswagon.com/"))

    # Navigate to fiction books page
    driver.get('https://www.bookswagon.com/fiction-books')

    # Click 'Add to cart' button for the first book (assuming there is one on the page)
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Add to cart']")))
    add_to_cart_button.click()

    # Click on the total cart items label to view the cart
    total_cart_items_label = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[@id='ctl00_lblTotalCartItems']")))
    total_cart_items_label.click()

    # Move the first book in the cart to wishlist
    move_to_wishlist_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='ctl00_phBody_BookCart_lvCart_ctrl0_btnMovetoWishlist']")))
    move_to_wishlist_button.click()

    # Optional: Wait for confirmation or perform further actions

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(5)  # Optional: To observe the state before quitting
    driver.quit()
