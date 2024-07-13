import time
from selenium import webdriver
from selenium.webdriver.common.by import By

checking_url = "https://www.selenium.dev/selenium/web/web-form.html"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Maximize the browser window to fullscreen
driver.maximize_window()


def test_eight_components():
    driver.get(checking_url)
    title = driver.title
    assert title == "Web form"
    driver.implicitly_wait(0.5)
    time.sleep(2)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    time.sleep(2)
    submit_button.click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"
    time.sleep(3)
    # Closes Chrome
    # driver.quit()
    driver.close()


test_eight_components()
