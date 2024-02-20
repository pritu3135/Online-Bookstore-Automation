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
driver.get('https://www.bookswagon.com/promo-best-seller/new-arrivals/99325F010C89')
time.sleep(4)
driver.find_element(By.XPATH, "//a[@href='https://www.bookswagon.com/book/shiva-purana-bibek-debroy/9780143459699']").click()
time.sleep(5)








