# cloudComputing

## 项目介绍

项目分为两个部分，分别是code1-词云展示以及code2-新闻类型数量统计，result目录是先前调试内容。

### **code1-词云展示**

项目路径在code1

首先启动hdfs
进入code文件夹运行Stream.py
Stream.py会监听hdfs上的words文件夹，一旦有新文件加入，则将结果进行分词
最后会把分词结果以词云图片的形式展示出来

### **code2-新闻类型数量统计**

项目路径在code2

首先启动newsCount.py，启动spark streaming监听json文件夹

然后再运行dataAcquisition.py，爬取新闻数据，以json格式存到json文件夹下

再启动paintNewsCount.py，根据newsCount.py生成的output文件夹下的文件得到最新的output数据，调用python可视化库画图

