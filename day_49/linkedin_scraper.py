from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_EMAIL = os.environ.get("EMAIL_ADDRESS")
ACCOUNT_PASSWORD = os.environ.get("LINKEDIN_ACCOUNT_PASSWORD")
PHONE = os.environ.get("my_tel_number")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)



driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3975172501&distance=25&f_E=1%2C2&f_TPR=r86400&geoId=100432943&keywords=Junior%2BPython%2BDeveloper&location=Brussels")



time.sleep(3)

# accept_3parties_cookies_button = driver.find_element(By.XPATH, value='//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]')
# if accept_3parties_cookies_button:
# 	accept_3parties_cookies_button.click()
#


# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
time.sleep(2)
password_field.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

