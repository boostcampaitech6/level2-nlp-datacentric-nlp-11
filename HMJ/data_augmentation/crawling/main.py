import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

labels = {0:'IT과학', 1:'경제', 2:'사회', 3:'생활문화', 4:'세계', 5:'스포츠', 6:'정치'}
topics = {'정치':108, '경제':104, '사회':109, '생활문화':504, '세계':110, 'IT과학':107, '스포츠':107}
new_data = {'ID':[],'text':[],'target':[],'url':[],'date':[]}

def get_url(label: int, page_num: int):
    topic = labels[label]
    n = topics[topic]
    if topic == '스포츠':
        url = f'https://www.ytn.co.kr/news/list.php?page={page_num}&mcd=0{n}'
    else:
        url = f'https://biz.heraldcorp.com/list.php?ct=010{n}000000&ctv=&np={page_num}'
  
    return url

def get_titles_main(url:str):
    # https://www.useragentstring.com/
    res = requests.get(url, headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(res.text, 'lxml')
    titles = soup.find_all('div', {'class':'list_title ellipsis'})
    titles = [title.get_text() for title in titles]
   
    return titles

def get_titles_sports(url: str):
    res = requests.get(url, headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(res.text, 'lxml')
    titles = soup.find_all('span', {'class': 'til'})
    titles = [title.get_text() for title in titles]
    
    return titles

for label, topic in labels.items():
    text_list = set()
    for i in tqdm(range(1, 300)):
        if len(text_list) > 1000:
            break
        url = get_url(label, i)
        if label == 5:
            titles = get_titles_sports(url)
        else:
            titles = get_titles_main(url)
        if len(titles) == 0:
            break
        text_list.update(titles)
        
    new_data['text'].extend(text_list)
    new_data['ID'].extend(['id']*len(text_list))
    new_data['target'].extend([label]*len(text_list))
    new_data['url'].extend(['https']*len(text_list))
    new_data['date'].extend(['2024']*len(text_list))
    
new_df = pd.DataFrame(new_data)
new_df.to_csv('/opt/ml/data_augmentation/crawling/crawling_main2.csv', encoding='utf-8')
            
