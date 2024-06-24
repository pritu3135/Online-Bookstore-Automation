import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_driver():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        logger.info("WebDriver initialized and browser window maximized.")
        return driver
    except Exception as e:
        logger.error(f"Error initializing WebDriver: {e}")
        raise


def reset_password(driver, email_or_mobile, new_password):
    driver.get('https://www.bookswagon.com/login')
    logger.info("Navigated to Bookswagon login page.")

    try:
        # Click on forgot password link
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='forgotpasswordlink themecolor']"))
        )
        forgot_password_link.click()
        logger.info("Clicked on forgot password link.")

        # Enter email or mobile number
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='ctl00$phBody$ForgotPassword$txtFGEmail']"))
        )
        email_field.send_keys(email_or_mobile)
        logger.info("Entered email or mobile number.")

        # Click on continue/reset password button
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='ctl00_phBody_ForgotPassword_lnkForgotPassword']"))
        )
        reset_button.click()
        logger.info("Clicked on reset password button.")

        # Enter new password
        new_password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='ctl00_phBody_ForgotPassword_txtFGPassword']"))
        )
        new_password_field.send_keys(new_password)
        logger.info("Entered new password.")

        # Confirm new password
        confirm_password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='ctl00_phBody_ForgotPassword_txtConfirmFGPwd']"))
        )
        confirm_password_field.send_keys(new_password)
        logger.info("Confirmed new password.")

        # Enter OTP
        otp = input("Please provide the OTP: ")
        otp_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='ctl00_phBody_ForgotPassword_txtFGOTP']"))
        )
        otp_field.send_keys(otp)
        logger.info("Entered OTP.")

        # Submit the reset password form
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='ctl00$phBody$ForgotPassword$btnFGLogin']"))
        )
        submit_button.click()
        logger.info("Clicked on submit button to reset password.")


        logger.info("Password reset successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        driver.quit()
        logger.info("WebDriver closed.")


if __name__ == "__main__":
    driver = setup_driver()
    reset_password(driver, "6205329963", "Pritu@1234")
