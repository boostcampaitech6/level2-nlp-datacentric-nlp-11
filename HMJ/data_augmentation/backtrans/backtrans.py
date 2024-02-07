from googletrans import Translator
import pandas as pd
from tqdm import tqdm
import re

trans = Translator()

data = pd.read_csv('/opt/ml/data/train_special_str_x.csv')
data.drop(['Unnamed: 0'], axis=1, inplace=True)

def back_trans(sentence, lang):
    ko_tran = trans.translate(sentence, dest=lang)
    tran_ko = trans.translate(ko_tran.text, dest='ko')
    
    return tran_ko.text

cnt = 0

while True:
    if cnt == 6999:
        break
    row = data.iloc[cnt]
    new_row = row.copy()
    text = row.text
    new_text = back_trans(text, 'en')
    if text == new_text:
        new_text = back_trans(text, 'ja')
    new_row.text = new_text
    data = data.append(new_row)
    cnt += 1

data.drop_duplicates(inplace=True)

data.to_csv('/content/drive/MyDrive/부스트캠프/project/data_centric/bt_aug_data.csv', encoding='utf-8')