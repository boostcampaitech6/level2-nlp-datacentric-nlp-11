import pandas as pd
import random

# CSV 파일을 읽어와 데이터프레임으로 로드
csv_file_path = '/opt/ml/data/combined_data_0129_adv.csv'
df = pd.read_csv(csv_file_path)

# 데이터를 무작위로 섞기 위해 인덱스를 리스트로 변환
index_list = df.index.tolist()
random.shuffle(index_list)

# 데이터프레임의 인덱스를 무작위로 섞인 순서로 재배열
df_shuffled = df.loc[index_list]

# 섞인 데이터프레임을 다시 CSV 파일로 저장 (선택 사항)
output_csv_file_path = 'shuffled_csv_file.csv'
df_shuffled.to_csv(output_csv_file_path, index=False)

# 무작위로 섞인 데이터프레임을 사용하거나 저장된 파일을 활용할 수 있음
