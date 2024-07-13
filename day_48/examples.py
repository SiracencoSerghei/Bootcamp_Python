# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# checking_url = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1&ref_=nav_ya_signin"
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
#
# # Maximize the browser window to fullscreen
# driver.maximize_window()
#
# # Navigate to Amazon in the first tab
# driver.get(checking_url)
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# # print("Dollar part HTML:")
# # print(price_dollar.get_attribute('outerHTML'))
# # price_dollar_html = price_dollar.get_attribute('outerHTML').split(">")[1].split("<")[0]
# # print(price_dollar_html)
# print(f"The price is {price_dollar.text}.{price_cents.text}")
#
# search_bar = driver.find_element(By.NAME, value="field-keywords")
# print(search_bar.get_attribute("placeholder"))
# submit_button = driver.find_element(By.ID, value="nav-search-submit-button")
# print(submit_button.get_attribute("value"))
# print(submit_button.size)
#
#
#
# # # Open a new tab using JavaScript execution
# # driver.execute_script("window.open('');")
#
# # # Switch to the new tab
# # driver.switch_to.window(driver.window_handles[1])
# #
# # # Navigate to a different URL in the new tab
# # driver.get("https://google.com")
# # print("Title of the second tab:", driver.title)
#
#
#
#
# # for close browser tab:
# # driver.close()
# # for close entire browser:
# # driver.quit()


# ============  example 2  ======================

from selenium import webdriver
from selenium.webdriver.common.by import By

checking_url = "https://www.python.org"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Maximize the browser window to fullscreen
driver.maximize_window()

driver.get(checking_url)

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR,  value='.event-widget time')
times = [time.text for time in event_times]
print(times)
# event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget a')
# titles = [title.text for title in event_names[1::]]
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
titles = [title.text for title in event_names]
print(titles)
events = {}
for n in range(len(event_times)):
	events[n] = {
		"time" : event_times[n].text,
		"name": event_names[n].text,
	}
print(events)




driver.quit()
