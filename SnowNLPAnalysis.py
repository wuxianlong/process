import os

from snownlp import SnowNLP
import csv

csvOrientPath = r'C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\csv'
snowNLPTargetPath = r'C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\snownlpcsv'


def get_csv_files(folder_path):
    excel_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            excel_files.append(os.path.join(folder_path, file))
    return excel_files


# NLP 情感分析
def targetFile(dataOrient, tarfile):
    commentsList = []
    rateData = []

    # 读取过滤数据
    with open(dataOrient, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # 如果内容为评论或评论为空时，则跳过此处理
            if row[0] == "评论" or len(row[0][:-10]) == 0:
                continue
            # :10因为过滤掉xxxx-xx-xx格式的时间
            commentsList.append(row[0][:-10])

    # 情感分析
    for comment in commentsList:
        value = SnowNLP(comment).sentiments
        # print(comment, value)
        if value > 0.5:
            rateData.append([comment, value, '正面'])
        elif value == 0.5:
            rateData.append([comment, value, '中性'])
        elif value < 0.5:
            rateData.append([comment, value, '负面'])

    # 写入目标函数
    for i in rateData:
        with open(tarfile, 'a+', encoding='utf8', newline='') as f:
            writer = csv.writer(f, delimiter='$')
            writer.writerow(i)


def main():
    csvList = get_csv_files(csvOrientPath)
    for csvPath in csvList:
        csvFileName = os.path.basename(csvPath)
        print(csvFileName)
        targetFileName = snowNLPTargetPath + "\\" + csvFileName
        # print(targetFileName)
        targetFile(csvPath, targetFileName)


if __name__ == '__main__':
    main()
