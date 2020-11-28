from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from wordcloud import WordCloud
import numpy
import datetime
import PIL.Image as Image
from pyspark import RDD

res = ""


def trans(rdd: RDD):
    words = rdd.collect()
    global res
    if len(words) == 0:
        return
    res = ""
    for word in words:
        res = res + word + " "
    wordcloud = WordCloud(font_path="font.ttf", mask=mask_pic, background_color='white').generate(res)
    wordcloud.to_file(r'wordCloud-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png')  # 保存生成的词云图片
    image = wordcloud.to_image()
    image.show()


mask_pic = numpy.array(Image.open("img.png"))

conf = SparkConf()
conf.setAppName('StreamProcess')
conf.setMaster('local[2]')
sc = SparkContext(conf=conf)
ssc = StreamingContext(sc, 10)
lines = ssc.textFileStream('hdfs://localhost/words')  # 监听HDFS文件夹
lines.pprint()
lines.foreachRDD(trans)

ssc.start()
ssc.awaitTermination()
