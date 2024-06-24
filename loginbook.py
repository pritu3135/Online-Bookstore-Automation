import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def login(driver, username, password):
    driver.get('https://www.bookswagon.com/login')

    try:
        # Wait for the username field and enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Mobile/Email']"))
        ).send_keys(username)

        # Wait for the password field and enter the password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
        ).send_keys(password)

        # Wait for the login button and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='ctl00_phBody_SignIn_btnLogin']"))
        ).click()

        print("Login successful")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(5)  # Optional: To observe the logged-in state before quitting
        driver.quit()


if __name__ == "__main__":
    driver = setup_driver()
    login(driver, "6205329963", "Pritu@1234")
