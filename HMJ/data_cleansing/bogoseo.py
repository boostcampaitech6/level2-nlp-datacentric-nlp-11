import pandas as pd
import re

data = pd.read_csv('/opt/ml/data/train_bt_special_x.csv')

for i in range(len(data)):
    text = data.iloc[i].text
    p = re.compile(r'(\s)?종합보고서(\s|\d|\w)*|(\s)?종합\s2bo')
    find = re.search(p, text)
    if find != None:
        clean_text = re.sub(r'(\s)?종합보고서(\s|\d|\w)*|(\s)?종합\s2bo', '종합', text)
        data.loc[i, 'text'] = clean_text

data.to_csv('/opt/ml/data/train_bt_special_bogoseo_x.csv', encoding='utf-8')
