from snownlp import SnowNLP
import csv

dataOrient = r'C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\data\test.csv'
tarfile = r'C:\Users\Administrator\Desktop\课程\数据仓库与数据挖掘\数据\DataProcess\data\data.csv'


# NLP 情感分析
def targetFile():
    commentsList = []
    rateData = []

    # 读取数据
    with open(dataOrient, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            commentsList.append(row[0][:-10])

    # 情感分析
    for comment in commentsList:
        value = SnowNLP(comment).sentiments
        print(comment, value)
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
    targetFile()


if __name__ == '__main__':
    main()
