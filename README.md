# README

### 项目介绍

项目分为以下两个部分：

1. code1-新闻标题关键词词云展示（位于`/code/code1`文件夹下）
2. code2-新闻类型数量统计（位于`/code/code2`文件夹下）

（`/code/result`文件夹下是作业过程中调试时的内容）

### 第一部分

（此部分实现了第一个问题的研究，即一段时间内今日头条的新闻标题关键词词云展示）

相关代码及数据文件均在`/code/code1`文件夹下，代码运行步骤如下：

1. 启动`HDFS`
2. 运行`dataAcquisition.py`爬虫文件，从今日头条网站爬取新闻文章的相关数据，爬到后以三种形式存储，分别是以`.xlsx`文件存储在代码所在目录下的`/result`子目录中、以`.json`文件存储在代码所在目录下的`/json`子目录中、写入`MongoDB`
3. 运行`Stream.py`文件，启动`PySpark`流监听，监听`HDFS`上的`/words`文件夹
4. 运行`ReadData.py`文件，从`MongoDB`中读取研究问题所需要的标题数据`title`，并调用`Python`中的`jieba.posseg`库对每一个标题进行中文分词，分词结果以`.txt`文件的形式，上传至被监听的`HDFS`中的`/words`文件夹
5. `PySpark`监听并读取`/words`文件夹中新增的文本文件，进行流处理，统计其中每个词的词频，并调用`Python`中的`wordcloud`库生成词云，词云图片以`.png`格式输出到代码所在目录下

### 第二部分

（此部分实现了第二个问题的研究，即一段时间内今日头条的新闻类型数量统计）

相关代码及数据文件均在`/code/code2`文件夹下，代码运行步骤如下：

1. 首先启动`newsCount.py`，启动`spark streaming`监听`/json`文件夹

2. 然后再运行`dataAcquisition.py`，爬取新闻数据，以`.json`格式存到`/json`文件夹下

3. 再启动`paintNewsCount.py`，根据`newsCount.py`生成的`/output`文件夹下的文件得到最新的`output`数据，调用`Python`可视化库画图

