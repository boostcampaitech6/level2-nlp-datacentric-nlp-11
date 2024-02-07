import requests
from bs4 import BeautifulSoup
import csv
import re

url_base = 'https://www.yna.co.kr/'
"""urls = ['politics/all/',
        'north-korea/all/',
        'economy/all/',
        'industry/all/',
        'society/all/',
        'local/all/',
        'international/all/',
        'culture/all/',
        'health/all/',
        'lifestyle/all/',
        'entertainment/all/',
        'sports/all/'
       ]"""
       
urls = ['industry/technology-science/',
        'economy/all/',
        'society/all/',
        'lifestyle/all/',
        'international/all/',
        'sports/all/',
        'politics/all/'
       ]

csv_filename = 'crawled_data_0129_02.csv'
characters_to_remove = r'[,]'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['text', 'target'])
    targetnum = 0
    
    for url in urls:
        for i in range(1, 21):
            present_url = f'{url_base}{url}{i}'
            print(present_url)
            response = requests.get(present_url)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                ul = soup.select_one('#container > div > div > div.section01 > section > div.list-type038 > ul')

                for j in range(1, 27):
                    css_selector = f'li:nth-child({j}) > div > div.news-con > a > strong'
                    titles = ul.select(css_selector)
                    for title in titles:
                        crawled_text = title.get_text()
                        cleaned_text = re.sub(characters_to_remove, '', crawled_text)
                        csv_writer.writerow([cleaned_text, targetnum])
            else: 
                print(response.status_code)
        targetnum += 1