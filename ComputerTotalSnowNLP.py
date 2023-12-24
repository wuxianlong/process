import openpyxl
import pandas as pd
import os

snowNLPTargetPath = r'C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\snownlpcsv'
snownlp_level_data_list = []

# 遍历文件夹下的所有csv文件
file_names = os.listdir(snowNLPTargetPath)

# 遍历文件名列表，筛选出csv文件
csv_files = [file for file in file_names if file.endswith('.csv')]

# 遍历csv文件
for csv_file in csv_files:
    file_path = os.path.join(snowNLPTargetPath, csv_file)

    # 读取csv文件
    df = pd.read_csv(file_path, error_bad_lines=False)
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    a = 0
    b = 0
    c = 0



    # 遍历每一行
    for index, row in df.iterrows():
        info_list = row.values[0].split('$')
        if len(info_list) <= 2:
            continue

        if info_list[2] == '正面':
            a += 1
        elif info_list[2] == '负面':
            b += 1
        elif info_list[2] == '中性':
            c += 1

    print([file_name, a, b, c])
    snownlp_level_data_list.append([file_name, a, b, c])

print(snownlp_level_data_list)

workbook = openpyxl.Workbook()
sheet = workbook.active

# 将数据写入工作表
for row in snownlp_level_data_list:
    sheet.append(row)
workbook.save("output.xlsx")