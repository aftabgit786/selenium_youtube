from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@zusmani78/videos")

last_height = driver.execute_script("return document.documentElement.scrollHeight")
scroll_attempt = 0

while True:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        scroll_attempt += 1

        if scroll_attempt == 3:
            break
    else:
        scroll_attempt = 0

    last_height = new_height

driver.quit()
