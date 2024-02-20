import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.bookswagon.com/login?q=signup')
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='ctl00_phBody_SignUp_txtName']").send_keys("crazy")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter Mobile Number']").send_keys("6205329964")
time.sleep(4)
from undetected_chromedriver import Chrome
Chrome=Chrome

time.sleep(10)

driver.find_element(By.XPATH,"//input[@name='ctl00$phBody$SignUp$btnContinue']").click()
time.sleep(4)