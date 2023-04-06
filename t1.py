from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@zusmani78/videos")

last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    time.sleep(2)

    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

driver.quit()
