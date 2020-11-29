from operator import add
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
import json
def updateFunc(new_values, last_sum):
        return sum(new_values) + (last_sum or 0)
def getState1(i):
        idx=i.find("tags")
        if(idx!=-1):         
                return (i[idx+6:-1].strip())[1:]
def getState(t):
        res=[]
        for each in t:
                res.append(t[each]["tags"])
        return res
def newsCount():
        conf = SparkConf()
        conf.setAppName('TestDStream')
        conf.setMaster('local[2]')
        sc = SparkContext(conf = conf)
        ssc = StreamingContext(sc, 20)
        ssc.checkpoint("file:///home/hadoop/桌面/cloudComputing/code2/checkpoint")
        lines = ssc.textFileStream('file:///home/hadoop/桌面/cloudComputing/code2/json')
        lines_json=lines.map(lambda x: json.loads(x))
        
        b=lines_json.map(lambda x: x)
        b.pprint()
        type_res=lines_json.flatMap(getState).map(lambda type: (type,1)).updateStateByKey(updateFunc)
        # type_res=lines.map(getState1).filter(lambda x:x!=None).map(lambda type: (type,1)).updateStateByKey(updateFunc)
        type_res.saveAsTextFiles('file:///home/hadoop/桌面/cloudComputing/code2/output/output.txt')
        type_res.pprint()

        ssc.start()
        ssc.awaitTermination()
newsCount()