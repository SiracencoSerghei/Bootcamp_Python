from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

load_dotenv()

FB_EMAIL = os.environ.get("EMAIL_ADDRESS")
FB_PASSWORD = os.environ.get("FB_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

time.sleep(3)

cookies_accept_button = driver.find_element(By.XPATH,
                                            value='//*[@id="t41619109"]/div/div[2]/div/div/div[1]/div[1]/button')
if cookies_accept_button:
	cookies_accept_button.click()

time.sleep(2)
log_in_button = driver.find_element(By.XPATH,
                                    value='//*[@id="t41619109"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()

time.sleep(2)
login_with_fb = driver.find_element(By.XPATH,
                                    value='//*[@id="t-1686761967"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
login_with_fb.click()

#Switch to Facebook login window
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
print(driver.window_handles)
driver.switch_to.window(fb_login_window)
print(driver.title)

allow_all_cookies_button = driver.find_element(By.XPATH, value='//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div')
print(allow_all_cookies_button.text)
allow_all_cookies_button.click()

time.sleep(2)

#Login and hit enter
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
time.sleep(3)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)


#Delay by 5 seconds to allow page to load.
time.sleep(5)

time.sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="t-1686761967"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="t-1686761967"]/div/div/div/div/div[3]/button[1]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()



# #Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
# for n in range(100):
#
#     #Add a 1 second delay between likes.
#     sleep(1)
#
#     try:
#         print("called")
#         like_button = driver.find_element(By.XPATH, value=
#             '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
#         like_button.click()
#
#     #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
#     except ElementClickInterceptedException:
#         try:
#             match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
#             match_popup.click()
#
#         #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
#         except NoSuchElementException:
#             time.sleep(2)
#
# driver.quit()