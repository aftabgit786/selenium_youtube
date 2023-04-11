from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from utils import scroll_to_page_end, extract_videos_data


url = "https://www.youtube.com/@zusmani78/videos"
driver = webdriver.Chrome()
driver.get(url)

scroll_to_page_end(driver)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

data = extract_videos_data(soup)

df = pd.DataFrame(data)
df.to_csv('youtube_data.csv', index=False)

print("Data successfully saved to CSV file.")
