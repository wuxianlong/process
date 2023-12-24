import os
import pandas as pd


# 将某文件夹中所有excel中的评论内容转换为一个统一的csv文件
def get_non_empty_second_column(folder_path, output_csv):
    all_files = os.listdir(folder_path)
    excel_files = [file for file in all_files if file.endswith('.xlsx') or file.endswith('.xls')]

    data_frames = []
    for file in excel_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)
        second_column = df.iloc[:, 1]
        non_empty_values = second_column[second_column.notna()]
        data_frames.append(non_empty_values)

    combined_data = pd.concat(data_frames, ignore_index=True)
    combined_data.to_csv(output_csv, index=False)


folder_path = r"C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\orient"
output_csv = r'C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\data\data.csv'
get_non_empty_second_column(folder_path, output_csv)
