import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
FIRST_NAME = os.environ.get("FIRST_NAME")
LAST_NAME = os.environ.get("LAST_NAME")
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")

checking_url = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Maximize the browser window to fullscreen
driver.maximize_window()

# Navigate to Amazon in the first tab
driver.get(checking_url)

first_name = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
# print(first_name.get_attribute("placeholder"))
last_name = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
email_address = driver.find_element(By.XPATH, value='/html/body/form/input[3]')

first_name.send_keys(FIRST_NAME)
last_name.send_keys(LAST_NAME)
email_address.send_keys(EMAIL_ADDRESS)

time.sleep(3.5)

sign_up = driver.find_element(By.XPATH, value='/html/body/form/button')
sign_up.send_keys(Keys.ENTER)

time.sleep(3.5)

driver.quit()
