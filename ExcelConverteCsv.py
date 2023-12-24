import os
import pandas as pd


# 获取文件夹中的所有excel文件
def get_excel_files(folder_path):
    excel_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            excel_files.append(os.path.join(folder_path, file))
    return excel_files


# 将多个excel文件合并为多个scv文件
def merge_excel_to_csv(excel_files, output_csv):
    for file in excel_files:
        data_frames = []
        csvFileName = os.path.basename(file)[:-5] + '.csv'

        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)
        second_column = df.iloc[:, 1]
        non_empty_values = second_column[second_column.notna()]
        data_frames.append(non_empty_values)
        combined_data = pd.concat(data_frames, ignore_index=True)
        combined_data.to_csv(output_csv + '\\' + csvFileName, index=False)


folder_path = r"C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\orient"
csv_path = r'C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\csv'

excel_files = get_excel_files(folder_path)
print(excel_files)
merge_excel_to_csv(excel_files, csv_path)
