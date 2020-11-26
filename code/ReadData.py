from pymongo import MongoClient
from pyhdfs import HdfsClient
import jieba.posseg as psg
import datetime

'''
ReadData.py文件流程：
1. 从MongoDB中读出标题数据
2. 对标题分词
3. 将分词结果以txt文件形式上传到HDFS
'''


# 从MongoDB中读标题数据，并以列表返回
def get_title_from_mongodb(db) -> list:
    myset = db.testset  # 使用test_set集合，没有则自动创建
    # 遍历查询数据
    res = []
    for i in myset.find():
        res.append(i["title"])
    return res


# 判断字符串中是否全为中文
def is_chinese(word) -> bool:
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


# 将标题字符串分词
def cut_title(titles) -> list:
    res = []
    for title in titles:
        tmp = psg.cut(title)
        for s in tmp:
            if is_chinese(s.word) and s.flag == 'n' and len(s.word) >= 2:
                res.append(s.word)
    return res


# 以txt文件形式输出分词结果到HDFS被监听文件夹
def upload_txt_to_hdfs(arr):
    client = HdfsClient(hosts="localhost:50070", user_name="Alphalbj")
    name = "/words/words-" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".txt"
    content = ""
    for word in arr:
        content += word + " "
    client.create(name, content.encode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'  # 本机ip地址
    client = MongoClient(host, 27017)  # 建立MongoDB客户端对象
    data = get_title_from_mongodb(client.mydb)  # 从MongoDB中读取标题数据
    words = cut_title(data)  # 分词，tmp为list类型，每个元素为一个词
    upload_txt_to_hdfs(words)
