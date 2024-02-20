import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.bookswagon.com/login')
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='forgotpasswordlink themecolor']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//input[@name='ctl00$phBody$ForgotPassword$txtFGEmail']").send_keys("6205329963")
time.sleep(4)
driver.find_element(By.XPATH, "//a[@id='ctl00_phBody_ForgotPassword_lnkForgotPassword']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='ctl00_phBody_ForgotPassword_txtFGPassword']").send_keys("Pritu@1234")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='ctl00_phBody_ForgotPassword_txtConfirmFGPwd']").send_keys("Pritu@1234")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='ctl00_phBody_ForgotPassword_txtFGOTP']").send_keys(input("Please provide the OTP:"))
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='ctl00$phBody$ForgotPassword$txtFGEmail']").send_keys("6205329963")
time.sleep(4)
driver.find_element(By.XPATH, "//input[@name='ctl00$phBody$ForgotPassword$btnFGLogin']").click()
time.sleep(5)
