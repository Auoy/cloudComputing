import matplotlib.pyplot as plt
import os
import datetime
import time
# import matplotlib
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签

def paint():
    outputs = []

    for filepath, dirnames, filenames in os.walk(r'/home/hadoop/桌面/cloudComputing/code2/output'):
        for dirname in dirnames:
            outputs.append(dirname)
            #print(':' + dirname)
    #print(outputs)
    output_path = max(outputs)

    #print(outputs)
    #print(output_path)
    filenames = os.listdir(r'/home/hadoop/桌面/cloudComputing/code2/output/' + output_path)
    #print(filenames)
   
        
    filenames2=[]
    for s in filenames:
        if not('.crc' in s) or ('_' in s):
            filenames2.append(s)
    filenames=filenames2
    index = []
    values = []
    #print(filenames)
    for p in filenames:
        #print(p)
        f = open('/home/hadoop/桌面/cloudComputing/code2/output/' + output_path + '/' + p, "rt", encoding="UTF-8")
        content = f.read()
        lines = content.splitlines()
        for i in range(len(lines)):
            lines[i] = lines[i][1:len(lines[i]) - 1]
            if ',' in lines[i]:
                s = lines[i].split(',')
                s[0] = s[0][1:len(s[0]) - 1]  # 新闻类型名
                s[1] = int(s[1][1:])  # 该类型的新闻个数
                #print(s)
                index.append(s[0])
                values.append(s[1])
        f.close()
    plt.bar(index, values,color='orange', alpha=0.9)
    plt.xlabel('新闻类型')
    plt.ylabel('数量')
    plt.title('现段时间头条热搜新闻类型-数量情况')
    #plt.savefig('/home/hadoop/桌面/cloudComputing/code2/painting/新闻类型-数量直方图.png')
    plt.savefig('/home/hadoop/桌面/cloudComputing/code2/painting/新闻类型-数量直方图-'+datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png")
    #plt.show()
    return


if __name__ == "__main__":
    while(1):
        paint()
        time.sleep(20)
        
