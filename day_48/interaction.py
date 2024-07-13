
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

checking_url = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get(checking_url)
driver.maximize_window()

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(article_count.text)

# all_portals = driver.find_element(By.XPATH, value='//*[@id="mp-other-content"]/ul/li[7]/b/a')
# all_portals.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
search = driver.find_element(By.NAME, value="search")

# sending keyboard input to Selenium

# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# or in one line:
search.send_keys("Python", Keys.ENTER)


