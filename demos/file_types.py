import csv
import os
import json

TRAINER_DEMO_FILES = '../trainer_demo_files/demo_files'
# FILE_PATH = f'../{TRAINER_DEMO_FILES}/demo_files/data.txt'

cwd = os.getcwd()
demo_file_path_csv = os.path.join(cwd, TRAINER_DEMO_FILES, 'data.csv')

# with open(demo_file_path_csv) as csv_file:
#     read_csv = csv.reader(csv_file)
#     for row in read_csv:
#         print(row)
#         for cell in row:
#             print(cell)
#             print("=====")
            
data = [
    ['Name', 'Age' ],
    ['Alice', 24],
    ['Bob', 32]
]

new_file_path = os.path.join(cwd, TRAINER_DEMO_FILES, 'new_data.csv')

# with open(new_file_path, mode='w') as csv_file:
#     new_data = csv.writer(csv_file)
#     new_data.writerows(data)

# with open(new_file_path) as written_csv:
#     read_data = csv.reader(written_csv)
#     for row in read_data:
#         print(row)

'''
TSV FILES
'''

tsv_file_path = os.path.join(cwd, TRAINER_DEMO_FILES, 'data.tsv')

with open(tsv_file_path) as tsv_file:
    read_tsv = csv.reader(tsv_file, delimiter='\t')
    for row in read_tsv:
        print(row)
        
new_tsv_file_path = os.path.join(cwd, TRAINER_DEMO_FILES, 'new_data.tsv')

with open(new_tsv_file_path, mode='w') as tsv_file:
    new_data = csv.writer(tsv_file, delimiter='\t')
    new_data.writerows(data)
    
# with open(new_tsv_file_path) as written_tsv:
#     read_data = csv.reader(written_tsv, delimiter='\t')
#     for row in read_data:
#         print(row)
        
new_json_file_path = os.path.join(cwd, TRAINER_DEMO_FILES, 'new_data.json')

data = {
    'name': 'Alice',
    'age': 24,
    'address': {
        'street': '123 Fake St',
        'city': 'Springfield'
    }
}

with open(new_json_file_path, mode='w') as json_file:
    json.dump(data, json_file)
    
with open(new_json_file_path) as read_json:
    data = json.load(read_json)
    print(data)
    print(type(data))
