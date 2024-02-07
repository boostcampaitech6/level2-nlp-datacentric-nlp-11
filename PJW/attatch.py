import csv

# 기존 CSV 파일 이름
a_csv_filename = 'train_delcol.csv'

# 추가할 CSV 파일 이름
b_csv_filename = 'crawled_data_0129_02.csv'

# 결과를 저장할 새로운 파일 이름
output_csv_filename = 'combined_data_0129.csv'

# 'ID' 값 시작
start_id = 7000  # 'ynat-v1_train_07000'부터 시작

# 열 이름 (컬럼 헤더)
columns_to_keep = ['ID', 'text', 'target']

# 기존 CSV 파일을 읽어옵니다.
data_to_append = []

with open(a_csv_filename, mode='r', encoding='utf-8') as a_csv:
    csv_reader = csv.DictReader(a_csv)
    for row in csv_reader:
        data_to_append.append(row)

# 추가할 CSV 파일을 읽어옵니다.
with open(b_csv_filename, mode='r', encoding='utf-8') as b_csv:
    csv_reader = csv.DictReader(b_csv)
    for row in csv_reader:
        row['ID'] = f'ynat-v1_train_{start_id:05d}'  # 'ID' 값을 업데이트
        data_to_append.append(row)
        #row['target'] = '0'
        start_id += 1

# 수정된 데이터를 새로운 CSV 파일에 저장합니다.
with open(output_csv_filename, mode='w', newline='', encoding='utf-8') as output_csv:
    csv_writer = csv.DictWriter(output_csv, fieldnames=columns_to_keep)
    
    # 헤더를 쓰기
    csv_writer.writeheader()
    
    # 데이터를 쓰기
    csv_writer.writerows(data_to_append)

print(f'Data has been saved to {output_csv_filename}')