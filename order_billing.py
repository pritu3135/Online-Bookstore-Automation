import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
frame_speed = 2
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
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='ctl00$phBody$BookCart$lvCart$imgPayment']").click()
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//input[@name='ctl00$cpBody$txtNewRecipientName']").send_keys("pritu kumar kaushik")
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//input[@name='ctl00$cpBody$txtNewCompanyName']").send_keys("Xindus QA ")
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//textarea[@name='ctl00$cpBody$txtNewAddress']").send_keys("Banaglore btm area ")
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//input[@name='ctl00$cpBody$txtNewLandmark']").send_keys("electronic city ")
time.sleep(frame_speed)
from selenium.webdriver.support.ui import Select

# Find the dropdown element
dropdown_element = driver.find_element(By.ID, "ctl00_cpBody_ddlNewState")

# Initialize a Select object
dropdown = Select(dropdown_element)

# Select the option by visible text
dropdown.select_by_visible_text("Karnataka")
time.sleep(4)
dropdown_element = driver.find_element(By.ID, "ctl00_cpBody_ddlNewCities")

# Initialize a Select object
dropdown = Select(dropdown_element)

# Select the option by visible text
dropdown.select_by_visible_text("Mysore")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='ctl00_cpBody_txtNewPincode']").send_keys("80024")
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//input[@id='ctl00_cpBody_txtNewMobile']").send_keys("6205329963")
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//input[@id='ctl00_cpBody_imgSaveNew']").click()
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//input[@id='ctl00_cpBody_ShoppingCart_lvCart_txtEmail']").send_keys("pritukaushik123@gmail.com")
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//input[@id='ctl00_cpBody_ShoppingCart_lvCart_btnContinue']").click()
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//input[@id='ctl00_cpBody_ShoppingCart_lvCart_txtOTP']").send_keys(input("Please provide the OTP:"))
time.sleep(frame_speed)
driver.find_element(By.XPATH, "//input[@id='ctl00_cpBody_ShoppingCart_lvCart_savecontinue']").click()
time.sleep(frame_speed)