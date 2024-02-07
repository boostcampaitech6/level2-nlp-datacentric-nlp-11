# label3(생활문화)에 해당되는 날씨 데이터 보강을 위함

import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

new_data = pd.read_csv('/opt/ml/data_augmentation/crawling/crawling_main2.csv')
weather_data = {'ID':[],'text':[],'target':[],'url':[],'date':[]}

def get_titles_weather(url: str):
    # https://www.useragentstring.com/
    res = requests.get(url, headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(res.text, 'lxml')
    titles = soup.find_all('span', {'class': 'til'})
    titles = [title.get_text() for title in titles]
    
    return titles

weather_text_set = set()
for i in tqdm(range(1, 300)):
    if len(weather_text_set) > 200:
        break
    url = f'https://www.ytn.co.kr/weather/list_weather.php?page={i}'
    titles = get_titles_weather(url)
    if len(titles) == 0:
        break
    weather_text_set.update(titles)
weather_text_list = list(weather_text_set)

cnt = 0
for i in range(len(new_data)):
    if cnt == 200:
        break
    row = new_data.iloc[i]
    if row.target == 3:
        new_data.loc[i, 'text'] = weather_text_list[cnt]
        cnt += 1
    
new_data.to_csv('/opt/ml/data_augmentation/crawling/crawling_main3.csv', encoding='utf-8')

