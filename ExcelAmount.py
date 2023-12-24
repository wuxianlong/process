import os
import pandas as pd


def get_excel_info(directory):
    excel_files = [f for f in os.listdir(directory) if f.endswith('.xlsx') or f.endswith('.xls')]
    excel_info = {}
    for file in excel_files:
        df = pd.read_excel(os.path.join(directory, file))
        excel_info[file] = len(df)
    return excel_info


directory = r"C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\orient"
excel_info = get_excel_info(directory)

data_list = []
total = 0
for file, rows in excel_info.items():
    print(f'文件名: {os.path.splitext(file)[0]}, 行数: {rows}')
    data_list.append((os.path.splitext(file)[0], rows))
    total += rows

df = pd.DataFrame(data_list, columns=['amount', 'local'])
df.to_excel("amount.xlsx", index=False)
print(f'total: {total}')
