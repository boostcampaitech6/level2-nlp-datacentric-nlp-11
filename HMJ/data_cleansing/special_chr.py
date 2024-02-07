# ·, 둘 다 제거한 버전은 오히려 성능 하락
# ·만 제거한 버전: F1 score 증가, accuracy 하락

import pandas as pd
import re
from tqdm import tqdm

data = pd.read_csv('/opt/ml/data/train_led_g2p.csv')

special_dict = {'↑': ' 증가', '↓':' 감소','→': '에서 ', '↔':', ',
           '…':', ', '...':'.', '㎡': ' 평', '℃': '도',
           '㎛':'mm', '㎜':'mm', '㎝':'mm', '㎞': 'm',
           '  ': ' '}   # replace
special_str = ':,%?!·~.'    # re

for i in tqdm(range(len(data))):
    sent = data.iloc[i].text
    for k, v in special_dict.items():
        sent = sent.replace(k, v)
    sent = re.sub(r'[^가-힣a-zA-Z一-龥0-9:,%?!·~. ]', '', sent)

    data.loc[i, 'text'] = sent

data.to_csv('/opt/ml/data/train_special_str_x.csv', encoding='utf-8')




