import os

from snownlp import SnowNLP
import csv
from collections import Counter

csvOrientPath = r'C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\csv'
keywordsList = []

def get_csv_files(folder_path):
    excel_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            excel_files.append(os.path.join(folder_path, file))
    return excel_files


# NLP 情感分析
def targetFile(dataOrient):
    commentsList = []


    # 读取过滤数据
    with open(dataOrient, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # 如果内容为评论或评论为空时，则跳过此处理
            if row[0] == "评论" or len(row[0][:-10]) == 0:
                continue
            # :10因为过滤掉xxxx-xx-xx格式的时间
            commentsList.append(row[0][:-10])

    # 分词
    for comment in commentsList:
        keywordsList.extend(SnowNLP(comment).keywords())

def main():
    csvList = get_csv_files(csvOrientPath)
    for csvPath in csvList:
        csvFileName = os.path.basename(csvPath)
        print(csvFileName)
        targetFile(csvPath)

    counter = Counter(keywordsList)
    print(counter.items())


if __name__ == '__main__':
    main()
