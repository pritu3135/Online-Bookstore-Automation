import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

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


def login(driver, username, password):
    try:
        driver.get('https://www.bookswagon.com/login')
        logger.info("Navigated to Bookswagon login page.")

        # Wait for the username field and enter the username
        try:
            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Mobile/Email']"))
            )
            username_field.send_keys(username)
            logger.info("Entered username.")
        except TimeoutException:
            logger.error("Timeout waiting for the username field.")
            return

        # Wait for the password field and enter the password
        try:
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
            )
            password_field.send_keys(password)
            logger.info("Entered password.")
        except TimeoutException:
            logger.error("Timeout waiting for the password field.")
            return

        # Wait for the login button and click it
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@id='ctl00_phBody_SignIn_btnLogin']"))
            )
            login_button.click()
            logger.info("Clicked login button.")
        except TimeoutException:
            logger.error("Timeout waiting for the login button.")
            return

        # Wait for some element on the logged-in page to ensure login was successful
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'myaccount.aspx')]"))
            )
            logger.info("Login successful.")
        except TimeoutException:
            logger.error("Timeout waiting for the login confirmation element.")
            return

    except Exception as e:
        logger.error(f"An error occurred during the login process: {e}")
        driver.quit()
        raise


def search_book(driver, book_title):
    try:
        # Wait for the search input field and enter the book title
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Title, Author, Publisher or ISBN']"))
            )
            search_input.send_keys(book_title)
            logger.info("Entered book title into search field.")
        except TimeoutException:
            logger.error("Timeout waiting for the search input field.")
            return

        # Wait for the search button and click it
        try:
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "btnTopSearch"))
            )
            search_button.click()
            logger.info("Clicked search button.")
        except TimeoutException:
            logger.error("Timeout waiting for the search button.")
            return

        # Wait for the search results to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'search-results')]"))
            )
            logger.info("Search results loaded.")
        except TimeoutException:
            logger.error("Timeout waiting for the search results to load.")
            return

    except Exception as e:
        logger.error(f"An error occurred during the book search process: {e}")
        driver.quit()
        raise


if __name__ == "__main__":
    driver = setup_driver()
    try:
        login(driver, "6205329963", "Pritu@1234")
        search_book(driver, "Bibek Debroy")
    finally:
        driver.quit()
        logger.info("WebDriver closed.")
