import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.bookswagon.com/login')
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Mobile/Email']").send_keys("6205329963")
time.sleep(4)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("Pritu@1234")
time.sleep(4)
driver.find_element(By.XPATH, "//a[@id='ctl00_phBody_SignIn_btnLogin']").click()
time.sleep(5)
search_input = driver.find_element(By.XPATH, "//input[@placeholder='Title, Author, Publisher or ISBN']")
search_input.send_keys("Bibek Debroy")

# Find the search button element and click on it
search_button = driver.find_element(By.ID, "btnTopSearch")
search_button.click()
time.sleep(4)