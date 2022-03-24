import os

def get_txt_files():
    path = os.getcwd()
    list_txt = []
    for f in os.listdir(path):
        if f.endswith('.txt'):
            list_txt.append(f)
    return list_txt

def str_count(file:str):
    with open(file, encoding='utf-8') as f:
        count = 0
        for line in f:
            count += 1
    return count

# def write_file(file1:str, file2:str, file3:str):
#     f4 = open('new.txt', 'a', encoding='utf-8')
#     values = [str_count(file1), str_count(file2), str_count(file3)]
#     keys = [file1, file2, file3]
#     data = dict(zip(keys, values))
#     sorted_keys = sorted(data, key=data.get)
#     sorted_data = {}
#     for key in sorted_keys:
#         sorted_data[key] = data[key]
#     for file, count in sorted_data.items():
#         f = open(file, 'r', encoding='utf-8')
#         read_file = f.read()
#         f4.write(f.name + '\n' + str(count) + '\n' + read_file + '\n')

def write_file(files):
    f4 = open('new.txt', 'a', encoding='utf-8')
    values = []
    keys = []
    for txt in files:
        values.append(str_count(txt))
        keys.append(txt)
    data = dict(zip(keys, values))
    sorted_keys = sorted(data, key=data.get)
    sorted_data = {}
    for key in sorted_keys:
        sorted_data[key] = data[key]
    for file, count in sorted_data.items():
        f = open(file, 'r', encoding='utf-8')
        read_file = f.read()
        f4.write(f.name + '\n' + str(count) + '\n' + read_file + '\n')

write_file(get_txt_files())
