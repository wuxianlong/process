import os
import pandas as pd


# 获取文件夹中的所有excel文件
def get_excel_files(folder_path):
    excel_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            excel_files.append(os.path.join(folder_path, file))
    return excel_files


# 将多个excel文件合并为一个scv文件
def merge_excel_to_csv(excel_files, output_csv):
    all_data = pd.DataFrame()
    for file in excel_files:
        df = pd.read_excel(file)
        all_data = all_data.append(df, ignore_index=True)
    all_data.to_csv(output_csv, index=False)


folder_path = r"C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\orient"
output_csv = r'C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\data\data.csv'

excel_files = get_excel_files(folder_path)
merge_excel_to_csv(excel_files, output_csv)
