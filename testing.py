from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from utils import extract_videos_data


url = "https://www.youtube.com/@zusmani78/videos"
driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

video_elements = soup.find_all('ytd-rich-item-renderer')
data = []
for videos in video_elements:
    title = videos.find('yt-formatted-string', {"id": "video-title"}).text
    views = videos.find('span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}).text
    upload_time = videos.find('div', {"id": "metadata-line"}).text.split('\n')[-3]
    video_duration = videos.find('span',
                                 {"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"}).text.strip()
    thumbnails = videos.find('img', {"style": "background-color: transparent;"}).get('src')
    print(upload_time)
# df = pd.DataFrame(data)
# df.to_csv('youtube_data.csv', index=False)

print("Data successfully saved to CSV file.")
