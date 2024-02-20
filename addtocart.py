import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
frame_speed = 5
driver.get('https://www.bookswagon.com/login')
time.sleep(frame_speed)
driver.find_element(By.XPATH,"//input[@placeholder='Mobile/Email']").send_keys("6205329963")
time.sleep(frame_speed)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("Pritu@1234")
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//a[@id='ctl00_phBody_SignIn_btnLogin']").click()
time.sleep(frame_speed)
driver.get('https://www.bookswagon.com/fiction-books')
time.sleep(frame_speed)
driver.find_element(By.XPATH,"//input[@value='Add to cart']").click()
time.sleep(frame_speed)
driver.find_element(By.XPATH,"//label[@id='ctl00_lblTotalCartItems']").click()
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//a[@id='ctl00_phBody_BookCart_lvCart_ctrl0_btnMovetoWishlist']").click()
time.sleep(frame_speed)